from django.contrib import admin

# Register your models here.

from .models import *

# Register your models here.
admin.site.register(oaperturadas)
admin.site.register(depositos)
admin.site.register(history_alm)
admin.site.register(history_eta)
admin.site.register(history_nave)
admin.site.register(history_sobrstadia)


