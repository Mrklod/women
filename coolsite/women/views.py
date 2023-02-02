from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

from .models import *

menu =['О сайте','Добавить статью','Обратная связь','Войти']

def index(request):
    posts = Women.objects.all()
    return render(request,'women/index.html',{'posts':posts,'menu':menu,'title':'Главная страница'})

def about(request):
    return render(request, 'women/about.html',{'menu':menu,'title':'О странице'})

def categories(request,catid):
    return HttpResponse(f'<h1>Категории</h1><p>{catid}</p>')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Not found</h1>')