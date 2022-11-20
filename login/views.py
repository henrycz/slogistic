import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, RedirectView

import core.settings as setting
from core import settings
from login.forms import resetpasswordform, changepasswordform
from user.models import user


class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'
    # setting.LOGIN_REDIRECT_URL
    success_url = reverse_lazy('erp:oaperturadas_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class resetpasswordView(FormView):
    form_class = resetpasswordform
    template_name = 'login/resetpwd.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def send_email_reset_pwd(self, user):
        data = {}
        try:
            # if not settings.DEBUG == Si el Debug es falso
            URL = settings.DOMAIN if not settings.DEBUG else self.request.META['HTTP_HOST']
            user.token = uuid.uuid4()
            user.save()

            mailServer = smtplib.SMTP(setting.EMAIL_HOST, settings.EMAIL_PORT)
            mailServer.starttls()
            mailServer.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            email_to = user.email    #'henry-carlosz@hotmail.com'

            # Construimos el mensaje simple
            mensaje = MIMEMultipart()
            mensaje['From'] = settings.EMAIL_HOST_USER
            mensaje['To'] = email_to
            mensaje['Subject'] = "Reseteo de contraseña"
            # render_to_spring = permite ponerle como parametro el codigo del template como spring,
            # adicionalmente enviarle parametros
            content = render_to_string('login/send_email.html', {
                'user': user,
                'link_resetpwd': 'http://{}/login/change/password/{}/'.format(URL, str(user.token)),
                'link_home': 'http://{}'.format(URL)
            })
            # se le adjunta al mensaje con el tipo
            mensaje.attach(MIMEText(content, 'html'))
            # Envio del mensaje
            mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
            # mailServer.sendmail(settings.EMAIL_HOST_USER, email_to, mensaje.as_string())
            # print('correo enviado correctamente')
        except Exception as e:
            data['error'] = str(e)
        return data

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            var_form = resetpasswordform(request.POST)
            if var_form.is_valid():
                userxx = var_form.get_user()
                data = self.send_email_reset_pwd(userxx)
            else:
                data['error'] = var_form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        return context


class changepasswordView(FormView):
    form_class = changepasswordform
    template_name = 'login/changepwd.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        xtoken = self.kwargs['token']
        if user.objects.filter(token=xtoken).exists():
            return super().get(request, *args, **kwargs)
        # redirecciona a la raiz
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            form = changepasswordform(request.POST)
            if form.is_valid():
                xuser = user.objects.get(token=self.kwargs['token'])
                xuser.set_password(request.POST['password'])
                # generar otra vez el token para que no pueda ser usado el link de nuevo.
                xuser.token = uuid.uuid4()
                xuser.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reseteo de Contraseña'
        context['login_url'] = settings.LOGIN_URL
        return context


