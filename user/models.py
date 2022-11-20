import uuid

from crum import get_current_request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import model_to_dict

from core.settings import MEDIA_URL, STATIC_URL


class user(AbstractUser):
    image = models.ImageField(upload_to='user/%Y/%m/%d', null=True, blank=True)
    # Inicio Se generar un token cada vez que exista un cambio de contraseña
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    # Fin Se generar un token cada vez que exista un cambio de contraseña

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def tojson(self):
        item = model_to_dict(self, exclude=['password','user_permissions','last_login'])
        # Consulta si existe un valor el campo: last_login
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': xgrupo.id, 'name': xgrupo.name } for xgrupo in self.groups.all()]

        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            vargroups = self.groups.all()
            if vargroups.exists():
                if 'group' not in request.session:
                    request.session['group'] = vargroups[0]
        except:
            pass
