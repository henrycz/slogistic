from django.contrib import admin
from django.urls import path, include
from homepage.views import IndexView
from login.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('erp/', include("erp.urls")),
]
# pueda leer los archivos medias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
