from django.forms import *

from erp.models import *


class oaperturadasform(ModelForm):
    # Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'
        #     form.field.widget.attrs['autocomplete']='off'
        self.fields['fch_eta'].widget.attrs['autofocus'] = True
    # Fin Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos

    class Meta:
        model = oaperturadas
        fields = 'orden','nomb_cliente','referencia', 'mercaderia', 'nave', 'fch_eta', 'vcto_alm', 'fch_sobrstadia', 'status_ultimo'
# Personalizar controles del formulario:
        widgets = {
            'orden': TextInput(
                attrs={
                    'placeholder': 'Ingrese una Orden, por favor',
                    'readonly': True,
                }
            ),
            'nomb_cliente': TextInput(
                attrs={
                    'placeholder': 'Ingrese un cliente, por favor',
                }
            ),
            'referencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese una Referencia, por favor',
                }
            ),
            'mercaderia': TextInput(
                attrs={
                    'placeholder': 'Ingrese la Descripcion de la Mercaderia, por favor',
                }
            ),
            'nave': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre de la Nave, por favor',
                }
            ),
            'fch_eta': DateInput(format='%d/%m/%Y',
                attrs={
                    'placeholder': 'Ingrese Fecha ETA (d/m/YYYY), por favor',
                }
            ),
            'vcto_alm': DateInput(format='%d/%m/%Y',
                  attrs={
                    'placeholder': 'Ingrese fecha Vcto Almacenaje (d/m/YYYY), por favor',
                    # 'value': datetime.now().strftime('%d/%m/%Y'),
                  }
            ),
            'fch_sobrstadia': DateInput(format='%d/%m/%Y',
                  attrs={
                      'placeholder': 'Ingrese fecha Vcto Sobrestadia (d/m/YYYY), por favor',
                  }
            ),
            'status_ultimo': Textarea(
                attrs={
                    'placeholder': 'Ingrese Status para el Cliente, por favor',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
        
        exclude = ['user_updated', 'user_creation']
# fin Personalizar controles del formulario

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     # validando si el campo name
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         self.add_error('name', 'Le faltan caracteres')
    #     return cleaned


class onumeradasform(ModelForm):
    # Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class']='form-control'
        #     form.field.widget.attrs['autocomplete']='off'
        self.fields['referencia'].widget.attrs['autofocus'] = True

    # Fin Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos

    class Meta:
        model = oaperturadas
        fields = 'orden', 'nomb_cliente', 'referencia', 'mercaderia', 'nave', 'fch_eta', 'cod_alm', 'vcto_alm', 'fch_sobrstadia', 'status_ultimo'
        # Personalizar controles del formulario:
        widgets = {
            'orden': TextInput(
                attrs={
                    'placeholder': 'Ingrese una Referencia, por favor',
                    'readonly': True,
                }
            ),
            'referencia': TextInput(
                attrs={
                    'placeholder': 'Ingrese una Referencia, por favor',
                }
            ),
            'mercaderia': TextInput(
                attrs={
                    'placeholder': 'Ingrese la Descripcion de la Mercaderia, por favor',
                }
            ),
            'nave': TextInput(
                attrs={
                    'placeholder': 'Ingrese Nombre de la Nave, por favor',
                }
            ),
            'fch_eta': DateInput(format='%d/%m/%Y',
                attrs={
                 'placeholder': 'Ingrese Fecha ETA (d/m/YYYY), por favor',
                }
                ),
            'cod_alm': TextInput(
                attrs={
                    'placeholder': 'Ingrese Almacen, por favor',
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'vcto_alm': DateInput(format='%d/%m/%Y',
                attrs={
                  'placeholder': 'Ingrese fecha Vcto Almacenaje (d/m/YYYY), por favor',
                  # 'value': datetime.now().strftime('%d/%m/%Y'),
                }
                ),
            'fch_sobrstadia': DateInput(format='%d/%m/%Y',
                attrs={
                    'placeholder': 'Ingrese fecha Vcto Sobrestadia (d/m/YYYY), por favor',
                }
                ),
            'status_ultimo': Textarea(
                attrs={
                    'placeholder': 'Ingrese Status para el Cliente, por favor',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }

        exclude = ['user_updated', 'user_creation']

    # fin Personalizar controles del formulario

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data




# class Productform(ModelForm):
# # Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)s
#         # for form in self.visible_fields():
#         #     form.field.widget.attrs['class']='form-control'
#         #     form.field.widget.attrs['autocomplete']='off'
#         self.fields['name'].widget.attrs['autofocus']=True
# # Fin Adicionar los atributos de los campos cuando se inicializa. Metodo para cuando tiene muchos campos

#     class Meta:
#         model=Product
#         fields='__all__'
# # Personalizar controles del formulario:
#         widgets={
#             'name': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese un nombre',
#                 }
#             ),
#         }
# #fin Personalizar controles del formulario

#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 form.save()
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data


# class testform(Form):
#     # componente selec, con atributos
#     # queryset==listado de objectos que se va a mostrar.
#     categories=ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width:100%'
#     }))

#     products=ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width:100%'
#     }))

#     # search=CharField(widget=TextInput(attrs={
#     #     'class': 'form-control',
#     #     'placeholder': 'Ingrese una descripcion'
#     # }))

#     search=ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
#         'class': 'form-control select2',
#         'style': 'width:100%'
#     }))


# class ClientForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['names'].widget.attrs['autofocus'] = True

#     class Meta:
#         model = Client
#         fields = '__all__'
#         widgets = {
#             'names': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus nombres',
#                 }
#             ),
#             'surnames': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus apellidos',
#                 }
#             ),
#             'dni': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su dni',
#                 }
#             ),
#             'date_birthday': DateInput(format='%Y-%m-%d',
#                 attrs={
#                     'value': datetime.now().strftime('%Y-%m-%d'),
#                 }
#             ),
#             'address': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su dirección',
#                 }
#             ),
#             'gender': Select()
#         }
#         exclude = ['user_updated', 'user_creation']

#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 form.save()
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data
#
#     def clean(self):
#         cleaned = super().clean()
#         if len(cleaned['name']) <= 50:
#             raise forms.ValidationError('Validacion xxx')
#             # self.add_error('name', 'Le faltan caracteres')
#         return cleaned