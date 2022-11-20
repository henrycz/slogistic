from django import forms
from user.models import user


class resetpasswordform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        if not user.objects.filter(username=cleaned['username']).exists():
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('El usuario no existe')
            # raise forms.ValidationError('El usuario no existe')
        return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username')
        return user.objects.get(username=username)


class changepasswordform(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un Password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita el password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        xpassword = cleaned['password']
        xconfirmpassword = cleaned['confirmpassword']

        if xpassword != xconfirmpassword:
            self._errors['error'] = self._errors.get('error', self.error_class())
            self._errors['error'].append('Las contraseñas deben ser iguales')
            # raise forms.ValidationError('El usuario no existe')
        return cleaned

