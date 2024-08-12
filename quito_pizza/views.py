from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from quito_pizza.forms import PizzaForm, CategoryForm, ClientForm
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

class CustomLoginView(LoginView):
    template_name = 'login.html'