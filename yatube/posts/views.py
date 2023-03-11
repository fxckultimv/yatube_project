from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Функция для отображения главной страницы проекта."""
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    """Функция для отображения страницы сообщества."""
    return HttpResponse('Список постов отфильтрованных по группам')