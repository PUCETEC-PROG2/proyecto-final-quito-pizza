from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
#from pokedex.forms import 
from .models import Pokemon, Trainer
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