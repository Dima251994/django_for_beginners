from django.urls import path # імпорт для роботи зі ссилками
from .views import homePageView # імпортуємо нашу функцію для ссилки

urlpatterns = [ # патерни ссилок
    path("", homePageView, name="home"), # перший аргумент це шлях ссилки, друге - функція для запроса, третє назва цієї ссилки для подальшої роботи

]