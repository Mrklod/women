from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView

from .forms import *
from .models import *

menu =[{'title':'О сайте','url_name':'about'},
       {'title':'Добавить статью','url_name':'add_page'},
       {'title':'Обратная связь','url_name':'contact'},
       {'title':'Войти','url_name':'login'}]

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#
#
#     context = {'posts':posts,
#
#                'menu':menu,
#                'title':'Главная страница',
#                'cat_selected':0}
#     return render(request,'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html',{'menu':menu,'title':'О странице'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    else:
        form = AddPostForm()
    return render(request,'women/addpage.html',{'form':form,'menu':menu,'title':'Добавление статьи'})

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Not found</h1>')

def show_post(request,post_id):
    post = get_object_or_404(Women,pk=post_id)

    context = {
        'post':post,
        'menu':menu,
        'title':post.title,
        'cat_selected':post.cat_id
    }

    return render(request,'women/post.html',context=context)

def show_category(request,cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)