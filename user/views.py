from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView

from user.forms import userform, userprofileform
from user.models import user
from erp.mixins import validatePermissionRequiredMixin


# vista basada en clases(se debe hacer por este medio)
class userlistview(LoginRequiredMixin, validatePermissionRequiredMixin, ListView):
    model = user
    template_name = 'user/list.html'
    permission_required = 'view_user'

    # decoradores:csrf_exempt==Excluir la validacion csrf
    @method_decorator(csrf_exempt)
    # decoradores:login_required== si un usuario esta logeado
    # @method_decorator(login_required)
    # Sobreescribir metodo con dispatch(Internamente se encarga de redireccionar el request al metodo GET)
    def dispatch(self, request, *args, **kwargs):
        # INICIO Consultamos si en el request existe un metodo GET entonces ejecuta lo siguiente(redirect):
        # if request.method=="GET":
        #     return redirect("erp:category_list2")
        # FIN Consultamos si en el request existe un metodo GET entonces ejecuta lo siguiente(redirect):

        # Mixin(issuperuserMixin)==clases creadas por nosotros mismo, lo cuales tiene metodos heredados en nuestra vista al momento
        # de implementarse y tendra prioridad alta.
        # ej de mixin:Si un usuario que esta logeado es un superusuario le vamos a dar acceso a nuestra vista
        # caso contrario se redireccionara a index
        return super().dispatch(request, *args, **kwargs)

    # sobreescribir el metodo POST
    def post(self, request, *args, **kwargs):
        data = {}
        # Inicio imprime metodo post para saber que le esta llegando.
        # Print(request.POST)
        # fin imprime metodo post para saber que le esta llegando.
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in user.objects.all():
                    data.append(i.tojson())
            else:
                data['error'] = "ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Usuarios"
        context['create_url'] = reverse_lazy('user:user_create')
        context['list_url'] = reverse_lazy('user:user_list')
        context['entity'] = 'Usuarios'
        return context


class usercreateview(LoginRequiredMixin, validatePermissionRequiredMixin, CreateView):
    model = user
    form_class = userform
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:user_list')
    permission_required = 'add_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Para imprimir el error y sus detalles
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form = categoryform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object=None
    #     context=self.get_context_data(**kwargs)
    #     context['form']=form
    #     return render(request,self.template_name,context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Creacion de un Usuario"
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class userUpdateView(LoginRequiredMixin, validatePermissionRequiredMixin, UpdateView):
    model = user
    form_class = userform
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:user_list')
    permission_required = 'change_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # Para imprimir el error y sus detalles
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form=categoryform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object=None
    #     context=self.get_context_data(**kwargs)
    #     context['form']=form
    #     return render(request,self.template_name,context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de un Usuario"
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class userdeleteView(DeleteView):
    model = user
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user:user_list')
    permission_required = 'delete_user'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de un Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        return context


class userchangegroup(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            # Guardar el objeto en la session
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])

        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:dashboard'))


class userprofileView(LoginRequiredMixin, UpdateView):
    model = user
    form_class = userprofileform
    template_name = 'user/profile.html'
    success_url = reverse_lazy('erp:dashboard')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    # Para imprimir el error y sus detalles
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Perfil"
        context['entity'] = 'Perfil'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class userchangepasswordView(LoginRequiredMixin, FormView):
    model = user
    form_class = PasswordChangeForm
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('login')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Inicio sobreescribir el metodo get_form, el cual es el metodo inicializador del formulario actual
    def get_form(self, form_class=None):
        # inicializando con el usuario actual
        form = PasswordChangeForm(user=self.request.user)
        form.fields['old_password'].widget.attrs['placeholder'] = 'Ingrese su contraseña actual'
        form.fields['new_password1'].widget.attrs['placeholder'] = 'Ingrese su nueva contraseña'
        form.fields['new_password2'].widget.attrs['placeholder'] = 'Repita su contraseña'

        return form
    # Fin sobreescribir el metodo get_form, el cual es el metodo inicializador del formulario actual

    # Para imprimir el error y sus detalles
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    # Inicio se ha actualizado el password pero no se deslogea
                    update_session_auth_hash(request, form.user)
                    # Fin sse ha actualizado el password pero no se deslogea
                else:
                    data['error'] = form.errors

            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edicion de Password"
        context['entity'] = 'Password'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
