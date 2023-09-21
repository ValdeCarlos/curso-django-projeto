from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(response):
    return render(response, 'recipes/home.html', context={
        'name': 'Valdemar Carlos',
    })


def contato(response):
    return HttpResponse('CONTATO')


def sobre(response):
    return HttpResponse('SOBRE')
