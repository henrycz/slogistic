from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from erp.forms import onumeradasform
from erp.mixins import validatePermissionRequiredMixin
from erp.models import oaperturadas


class onumeradasView(LoginRequiredMixin, validatePermissionRequiredMixin, ListView):
    model = oaperturadas
    template_name = 'onumeradas/list.html'
    permission_required = 'erp.view_onumeradas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in oaperturadas.objects.filter(fch_dam__isnull=False, fch_culminado__isnull=True):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ordenes (Numeradas hasta Concluidas) del año presente'
        context['create_url'] = reverse_lazy('erp:onumeradas_create')
        context['list_url'] = reverse_lazy('erp:onumeradas')
        context['entity'] = 'onumeradas'
        # context['form'] = 'oaperturadas'
        return context


class onumeradasCreateView(LoginRequiredMixin, validatePermissionRequiredMixin, CreateView):
    model = oaperturadas
    form_class = onumeradasform
    template_name = 'onumeradas/create.html'
    success_url = reverse_lazy('erp:onumeradas')
    permission_required = 'erp.add_onumeradas'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación una Ordenes Numeradas'
        context['entity'] = 'onumeradas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class onumeradasUpdateView(LoginRequiredMixin, validatePermissionRequiredMixin, UpdateView):
    model = oaperturadas
    form_class = onumeradasform
    template_name = 'onumeradas/create.html'
    success_url = reverse_lazy('erp:onumeradas')
    permission_required = 'erp.change_onumeradas'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de una orden'
        context['entity'] = 'onumeradas'
        context['list_url'] = reverse_lazy('erp:onumeradas')  # self.success_url
        context['action'] = 'edit'
        return context


class onumeradasDeleteView(LoginRequiredMixin, validatePermissionRequiredMixin, DeleteView):
    model = oaperturadas
    template_name = 'onumeradas/delete.html'
    success_url = reverse_lazy('erp:onumeradas')
    permission_required = 'erp.delete_onumeradas'
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
        context['title'] = 'Eliminación de una orden Numeradas'
        context['entity'] = 'onumeradas'
        context['list_url'] = self.success_url
        return context