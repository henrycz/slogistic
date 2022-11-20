from django.urls import path
from user.views import *

app_name = "user"

urlpatterns = [
    path('list/', userlistview.as_view(),name="user_list"),
    path('add/', usercreateview.as_view(),name="user_create"),
    path('edit/<int:pk>/', userUpdateView.as_view(),name="user_update"),
    path('delete/<int:pk>/', userdeleteView.as_view(),name="user_delete"),
    path('profile/', userprofileView.as_view(), name="user_profile"),
    path('change/password', userchangepasswordView.as_view(), name="user_change_password"),
]