from django.urls import path
from login.views import *

urlpatterns = [
    path('', LoginFormView2.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('reset/password', resetpasswordView.as_view(),name='reset_password'),
    path('change/password/<str:token>/', changepasswordView.as_view(),name='change_password'),
]
