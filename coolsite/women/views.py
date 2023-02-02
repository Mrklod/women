from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

from .models import *

menu =[{'title':'О сайте','url_name':'about'},
       {'title':'Добавить статью','url_name':'add_page'},
       {'title':'Обратная связь','url_name':'contact'},
       {'title':'Войти','url_name':'login'}]

def index(request):
    posts = Women.objects.all()
    context = {'posts':posts,
               'menu':menu,
               'title':'Главная страница'}
    return render(request,'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html',{'menu':menu,'title':'О странице'})

def addpage(request):
    return HttpResponse('Добавить статью')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Not found</h1>')

def show_post(request,post_id):
    return HttpResponse(f'Статья номер {post_id}')