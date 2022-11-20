from django.urls import path
from erp.views.oaperturadas.views import *
from erp.views.onumeradas.views import *
from erp.views.dashboard.views import *

app_name = "erp"

urlpatterns = [
    # oaperturadas
    path('oaperturadas/list/', oaperturadasListView.as_view(), name="oaperturadas_list"),
    path('oaperturadas/add/', oaperturadasCreateView.as_view(), name="oaperturadas_create"),
    path('oaperturadas/edit/<int:pk>/', oaperturadasUpdateView.as_view(), name="oaperturadas_update"),
    path('oaperturadas/delete/<int:pk>/', oaperturadasDeleteView.as_view(), name="oaperturadas_delete"),
    # product
    # path('product/list/', productlistview.as_view(),name="product_list"),
    # path('product/add/', productcreateview.as_view(),name="product_create"),
    # path('product/edit/<int:pk>/', productUpdateView.as_view(),name="product_update"),
    # path('product/delete/<int:pk>/', productdeleteView.as_view(),name="product_delete"),
    # client
    # onumeradas
    path('onumeradas/list/', onumeradasView.as_view(), name="onumeradas"),
    path('onumeradas/add/', onumeradasCreateView.as_view(), name="onumeradas_create"),
    path('onumeradas/edit/<int:pk>/', onumeradasUpdateView.as_view(), name="onumeradas_update"),
    path('onumeradas/delete/<int:pk>/', onumeradasDeleteView.as_view(), name="onumeradas_delete"),
    # home
    path('dashboard/', DashboardView.as_view(),name='dashboard'),
    # test
    # path('test/', testview.as_view(),name='test'),

]