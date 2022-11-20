from django import forms
from django.forms import ModelForm

from user.models import user


class userform(ModelForm):
    # Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'
        #     form.field.widget.attrs['autocomplete']='off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    # Fin Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    class Meta:
        model = user
        # orden
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image', 'groups'
        # Personalizar controles del formulario:
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(render_value=True, attrs={
                    'placeholder': 'Ingrese su password',
                }
            ),
            'groups': forms.SelectMultiple(
                attrs={
                    'Class': 'form-control select2',
                    'style': 'width: 100%',
                    'multiple': 'multiple',
                }
            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']
    # fin Personalizar controles del formulario

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                # inicio password actual (extraerla)
                pwd = self.cleaned_data['password']
                # fin password actual (extraerla)
                # commit=False == pausa a la creacion del objecto
                user_activo = form.save(commit=False)
                if user_activo.pk is None:
                    # para encriptar el password
                    user_activo.set_password(pwd)
                else:
                    # para cuando editar la clave o password
                    userx = user.objects.get(pk=user_activo.pk)
                    if userx.password != pwd:
                        # para encriptar el password
                        user_activo.set_password(pwd)
                user_activo.save()
                # Inicio Eliminar la relacion para que luego se registre
                user_activo.groups.clear()
                # Fin Eliminar la relacion para que luego se registre
                # Inicio para poder grabar groups
                for xgroup in self.cleaned_data['groups']:
                    user_activo.groups.add(xgroup)
                # Fin para poder grabar groups
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self):
        cleaned = super().clean()
        # validando si el campo name
        # if len(cleaned['name']) <= 50:
        # raise forms.ValidationError('Validacion xxx')
        # self.add_error('name', 'Le faltan caracteres')
        return cleaned


class userprofileform(ModelForm):
    # Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'
        #     form.field.widget.attrs['autocomplete']='off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    # Fin Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    class Meta:
        model = user
        # orden
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image'
        # Personalizar controles del formulario:
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
            'password': forms.PasswordInput(render_value=True, attrs={
                    'placeholder': 'Ingrese su password',
                }
            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff','groups']
    # fin Personalizar controles del formulario

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                # inicio password actual (extraerla)
                pwd = self.cleaned_data['password']
                # fin password actual (extraerla)
                # commit=False == pausa a la creacion del objecto
                user_activo = form.save(commit=False)
                if user_activo.pk is None:
                    # para encriptar el password
                    user_activo.set_password(pwd)
                else:
                    # para cuando editar la clave o password
                    userx = user.objects.get(pk=user_activo.pk)
                    if userx.password != pwd:
                        # para encriptar el password
                        user_activo.set_password(pwd)
                user_activo.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    def clean(self):
        cleaned = super().clean()
        # validando si el campo name
        # if len(cleaned['name']) <= 50:
        # raise forms.ValidationError('Validacion xxx')
        # self.add_error('name', 'Le faltan caracteres')
        return cleaned