from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'recipes/home.html', context={
        'Name': 'Wander de castro',
    })

def contato(request):
    return HttpResponse('contatos')

def sobre(request):
    return HttpResponse('Sobre')
