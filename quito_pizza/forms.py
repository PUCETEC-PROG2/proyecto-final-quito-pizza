from django import forms
from .models import Pizza, Category, Client, Product, Purchase, Purchase_Detail
from django.core.validators import RegexValidator
from django.forms import formset_factory

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        widgets = {
            'pizza_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'pizza_size': forms.Select(attrs={
                'class':'form-control'
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
                'required':'False'
            }),
            'category': forms.Select(attrs={
                'class':'form-control'
            }),
            'price_pizza': forms.NumberInput(attrs={
                'class':'form-control'
            }),
            'picture_pizza': forms.ClearableFileInput(attrs={
                'class':'form-control'
            })
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name_category': forms.TextInput(attrs={
                'class':'form-control'
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
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control'
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
                'required':'False'
            })
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'category': forms.Select(attrs={
                'class':'form-control'
            }),
            'price_product': forms.NumberInput(attrs={
                'class':'form-control'
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
                'type': 'date',
                'class':'form-control'
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
                'class':'form-control'
            }),
            'product': forms.Select(attrs={
                'class':'form-control'
            }),
            'amount_product': forms.NumberInput(attrs={
                'class':'form-control'
            }),
        }

DetailPurchaseFormSet = formset_factory(PurchaseDetailForm, extra=1)
