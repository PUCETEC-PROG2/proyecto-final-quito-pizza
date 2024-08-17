from django import forms
from .models import Pizza, Category, Client, Product, Purchase, Purchase_Detail
from django.core.validators import RegexValidator
from django.forms import formset_factory

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        labels = {
            'pizza_name': 'Pizza',
            'pizza_size': 'Tamaño',
            'pizza_dough': 'Tipo de masa',
            'ingredient_1': 'Ingrediente 1',
            'ingredient_2': 'Ingrediente 2',
            'ingredient_3': 'Ingrediente 3',
            'ingredient_4': 'Ingrediente 4',
            'description': 'Descripción',
            'category': 'Categoría',
            'price_pizza': 'Precio',
            'picture_pizza': 'Foto'
        }
        widgets = {
            'pizza_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingresa el nombre de la pizza'
            }),
            'pizza_size': forms.Select(attrs={
                'class':'form-control',
            }),
            'pizza_dough': forms.Select(attrs={
                'class':'form-control'
            }),
            'ingredient_1': forms.Select(attrs={
                'class':'form-control',
                'required':'False'
            }),
            'ingredient_2': forms.Select(attrs={
                'class':'form-control',
                'required':'False'
            }),
            'ingredient_3': forms.Select(attrs={
                'class':'form-control',
                'required':'False'
            }),
            'ingredient_4': forms.Select(attrs={
                'class':'form-control',
                'required':'False'
            }),
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'required':'False',
                'placeholder': 'Ingresa una descripción'
            }),
            'category': forms.Select(attrs={
                'class':'form-control'
            }),
            'price_pizza': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingresa el precio'
            }),
            'picture_pizza': forms.ClearableFileInput(attrs={
                'class':'form-control'
            })
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name_category': 'Categoría'
        }
        widgets = {
            'name_category': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Ingresa una categoría'
            }),
        }

class ClientForm(forms.ModelForm):
    dni = forms.CharField(
        label='Número de cedula',
        validators=[
            RegexValidator(
                regex=r'^\d{1,10}$',
                message='El DNI debe contener solo números.'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su número de cédula',
            'maxlength': '10'
        })
    )
    
    phone_number = forms.CharField(
        label='Número de Teléfono',
        validators=[
            RegexValidator(
                regex=r'^\d{1,10}$',
                message='El número de teléfono debe contener solo números.'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su número de teléfono',
            'maxlength': '10'
        })
    )
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'address': 'Dirección'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingrese el nombre del cliente',
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingrese el apellido del cliente',
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingrese su correo electrónico',
            }),
            'dni': forms.TextInput(attrs={
                'class':'form-control',
                'maxlength': '10'
            }),
            'phone_number': forms.TextInput(attrs={
                'class':'form-control',
                'maxlength': '10'
            }),
            'address': forms.TextInput(attrs={
                'class':'form-control',
                'required':'False',
                'placeholder': 'Ingrese la dirección del cliente',
            })
        }
    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not Client().validate_dni(dni):
            raise forms.ValidationError('La cédula proporcionada no es válida.')
        return dni
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not Client().validate_phone_number(phone_number):
            raise forms.ValidationError('El número de teléfono no es válido.')
        return phone_number

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_name': 'Producto',
            'category': 'Categoría',
            'price_product': 'Precio',
            'picture_products': 'Foto'
        }
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingresa el producto'
            }),
            'category': forms.Select(attrs={
                'class':'form-control'
            }),
            'price_product': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingresa el precio'
            }),
            'stock': forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Ingresa el stock'
            }),
            'picture_products': forms.ClearableFileInput(attrs={
                'class':'form-control'
            })
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['client', 'date']  # Agregar el campo cliente
        widgets = {
            'client': forms.Select(attrs={
                'class':'form-control'
            }),
            'date': forms.DateTimeInput(attrs={
                'class':'form-control',
                'type': 'datetime-local'
            })
        }

class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = Purchase_Detail
        fields = ['pizza', 'amount_pizza', 'product', 'amount_product']
        widgets = {
            'pizza': forms.Select(attrs={
                'class':'form-control'
            }),
            'amount_pizza': forms.NumberInput(attrs={
                'class':'form-control',
                'min': 1
            }),
            'product': forms.Select(attrs={
                'class':'form-control'
            }),
            'amount_product': forms.NumberInput(attrs={
                'class':'form-control',
                'min': 1
            }),
        }

DetailPurchaseFormSet = formset_factory(PurchaseDetailForm, extra=1)
