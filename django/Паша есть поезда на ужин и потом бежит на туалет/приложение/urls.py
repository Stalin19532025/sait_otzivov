from django.urls import path

# из файла вьюз импортируем все функции
from .views import *

urlpatterns = [
    path('', домашняя),
]
