from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.

menu = ["О Сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    #return HttpResponse("Страница приложения women")
    return render(request, 'women/index.html', { 'posts': posts,
                                                'menu': menu,
                                                'title': 'Главная страница'})


def about(request):
    #return HttpResponse("Страница приложения women")
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, cat):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")


def archive(request, year):
    if int(year) > 2021:
        raise Http404()
    elif int(year) < 2000:
        # home - псевдоним, описывается в разделе urls
        return redirect(permanent=True, to="home")

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найденa </h1>")
