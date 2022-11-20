from django.shortcuts import redirect
from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from crum import get_current_request


# Si el usuario logeado es superusuario:
class issuperuserMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

    # para poder enviar valores adicionales en get_context_data
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now()
        return context


# Validar permisos
class validatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    # Obtener los permisos que llegaban de la vista y lo transformaba a manera dupla
    def get_perms(self):
        # creando un array
        perms = []
        if isinstance(self.permission_required, str):
            # llega como string
            perms.append(self.permission_required)
        else:
            # llega como dupla, y lo convierte en un listado.
            perms = list(self.permission_required)
        return perms

    # Te redireccionaba a una pagina, en caso de que no tenga permisos
    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('erp:dashboard')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if 'group' in request.session:
            var_group = request.session['group']
            # var_group = Group.objects.get(pk=1)
            perms = self.get_perms()
            # codename__in=se usa si el usuario tiene uno de los permisos que tiene asignados
            # if var_group.permissions.filter(codename__in=perms):
            for p in perms:
                if not var_group.permissions.filter(codename=p).exists():
                    messages.error(request, 'No tiene permiso para ingresar a este modulo')
                    # messages. Error(request,'No tiene permiso para ingresar a este módulo')
                    # fin Texto del mensaje
                    return redirect(self.get_url_redirect())
            return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este modulo')
        # messages. Error(request,'No tiene permiso para ingresar a este módulo')
        # fin Texto del mensaje
        return redirect(self.get_url_redirect())

