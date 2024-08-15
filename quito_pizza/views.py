from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from quito_pizza.forms import PizzaForm, CategoryForm, ClientForm, ProductForm, PurchaseDetailForm, PurchaseForm, DetailPurchaseFormSet
from .models import Category, Client, Pizza, Product, Purchase, Purchase_Detail
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'user': request.user,
        'logged_in': request.user.is_authenticated
    }
    return render(request, 'index.html', context)

def pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk = pizza_id)
    template = loader.get_template('display_pizza.html')
    context = {
        'pizza': pizza
    }
    return HttpResponse(template.render(context, request))

def product(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

def client(request, client_id):
    client = get_object_or_404(Client, pk = client_id)
    template = loader.get_template('display_client.html')
    context = {
        'client': client
    }
    return HttpResponse(template.render(context, request))

def list_pizza(request):
    pizzas = Pizza.objects.order_by('pizza_name')
    template = loader.get_template('list_pizza.html')
    return HttpResponse(template.render({'pizzas': pizzas}, request))

def list_product(request):
    products = Product.objects.order_by('product_name')
    template = loader.get_template('list_product.html')
    return HttpResponse(template.render({'products': products}, request))

@login_required
def add_pizza(request):
    if request.method =='POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_pizza')
    else:
        form = PizzaForm()
    return render(request, 'pizza_form.html', {'form':form})

@login_required
def add_product(request):
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_product')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form':form})

def list_category(request):
    categorys = Category.objects.order_by('name_category')
    template = loader.get_template('list_category.html')
    context = {
        'categorys': categorys
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_category(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_category')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form':form})

@login_required
def edit_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk = pizza_id) 
    if request.method =='POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_pizza')
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizza_form.html', {'form':form})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk = product_id) 
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form':form})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk = category_id) 
    if request.method =='POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form':form})

@login_required
def delete_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk = pizza_id)
    pizza.delete()
    return redirect("quito_pizza:list_pizza")

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    product.delete()
    return redirect("quito_pizza:list_product")

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    category.delete()
    return redirect("quito_pizza:list_category")

@login_required
def list_client(request):
    clients = Client.objects.order_by('name')
    template = loader.get_template('list_client.html')
    return HttpResponse(template.render({'clients': clients}, request))

@login_required
def add_client(request):
    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_client')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form':form})

@login_required
def edit_client(request, client_id):
    client = get_object_or_404(Client, pk = client_id) 
    if request.method =='POST':
        form = CategoryForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('quito_pizza:list_client')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form':form})

@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk = client_id)
    client.delete()
    return redirect("quito_pizza:list_client")

@login_required
def list_purchase(request):
    purchases = Purchase_Detail.objects.order_by('purchase')
    template = loader.get_template('list_purchase.html')
    return HttpResponse(template.render({'purchases': purchases}, request))

def add_purchase(request):
    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        formset = DetailPurchaseFormSet(request.POST)

        if purchase_form.is_valid() and formset.is_valid():
            # Crear una nueva venta con la fecha y cliente proporcionados por el usuario
            purchase = purchase_form.save()

            # Procesar cada formulario del formset
            for form in formset:
                if form.cleaned_data:
                    pizza = form.cleaned_data['pizza']
                    amount_pizza = form.cleaned_data['amount_pizza']
                    product = form.cleaned_data['product']
                    amount_product = form.cleaned_data['amount_product']
                    
                    # Crear el detalle de venta
                    Purchase_Detail.objects.create(
                        purchase=purchase,
                        pizza=pizza,
                        amount_pizza=amount_pizza,
                        unit_price_pizza=pizza.price_pizza,
                        product=product,
                        amount_product=amount_product,
                        unit_price_product=product.price_product
                    )
            
            # Actualizar el total de la venta
            purchase.update_total()
            
            return redirect('quito_pizza:list_purchase')  # Redirigir a la vista de detalles o confirmación
    else:
        purchase_form = PurchaseForm()
        formset = DetailPurchaseFormSet()

    return render(request, 'purchase_form.html', {'purchase_form': purchase_form, 'formset': formset})

def purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase_Detail, pk = purchase_id)
    template = loader.get_template('display_purchase.html')
    context = {
        'purchase': purchase
    }
    return HttpResponse(template.render(context, request))

class CustomLoginView(LoginView):
    template_name = 'login.html'