from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home')

def contato(request):
    return HttpResponse('contatos')

def sobre(request):
    return HttpResponse('Sobre')
