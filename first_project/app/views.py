from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime as dt
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = dt.now()
    msg = f'Текущее время: {current_time.strftime("%H:%M")}'
    return HttpResponse(f'{msg} <br> <a href={reverse("home")}> Главная страница </a>')


def workdir_view(request):
    w_dir = f'Папки и файлы:{os.listdir()}'
    return HttpResponse(f'{w_dir} <br> <a href={reverse("home")}> Главная страница </a>')
