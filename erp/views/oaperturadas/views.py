from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from erp.forms import oaperturadasform
from erp.mixins import validatePermissionRequiredMixin
from erp.models import oaperturadas


class oaperturadasListView(LoginRequiredMixin, validatePermissionRequiredMixin, ListView):
    model = oaperturadas
    template_name = 'oaperturadas/list.html'
    permission_required = 'view_oaperturadas'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in oaperturadas.objects.filter(fch_dam__isnull=True):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ordenes Aperturadas'
        context['create_url'] = reverse_lazy('erp:oaperturadas_create')
        context['list_url'] = reverse_lazy('erp:oaperturadas_list')
        context['entity'] = 'oaperturadas'
        # context['form'] = 'oaperturadas'
        return context


class oaperturadasCreateView(LoginRequiredMixin, validatePermissionRequiredMixin, CreateView):
    model = oaperturadas
    form_class = oaperturadasform
    template_name = 'oaperturadas/create.html'
    success_url = reverse_lazy('erp:oaperturadas_list')
    permission_required = 'add_oaperturadas'
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
        context['title'] = 'Creación una Ordenes Aperturadas'
        context['entity'] = 'oaperturadas'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class oaperturadasUpdateView(LoginRequiredMixin, validatePermissionRequiredMixin, UpdateView):
    model = oaperturadas
    form_class = oaperturadasform
    template_name = 'oaperturadas/create.html'
    success_url = reverse_lazy('erp:oaperturadas_list')
    permission_required = 'change_oaperturadas'
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
        context['title'] = 'Edición de una orden'
        context['entity'] = 'oaperturadas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class oaperturadasDeleteView(LoginRequiredMixin, validatePermissionRequiredMixin, DeleteView):
    model = oaperturadas
    template_name = 'oaperturadas/delete.html'
    success_url = reverse_lazy('erp:oaperturadas_list')
    permission_required = 'erp.delete_oaperturadas'
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
        context['title'] = 'Eliminación de una orden Aperturada'
        context['entity'] = 'oaperturadas'
        context['list_url'] = self.success_url
        return context