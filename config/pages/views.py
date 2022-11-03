from django.shortcuts import render
from django.http import HttpResponse # додаємо імпорт для роботи з Http-запросами

# Create your views here.

def homePageView(request): # стоврюємо функцію яка повертає наш запрос
    return HttpResponse("Hello world")



