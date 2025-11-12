from django.urls import path

# из файла вьюз импортируем все функции
from .views import *

urlpatterns = [
    path('', домашняя),
    path('отзыв/<int:айди_отзыва>/', один_отзыв, name="один_отзыв"),
]
