# стандартный вид
from django.forms import ModelForm, CheckboxSelectMultiple

from .models import *

class ФормаОтзыва(ModelForm):
    class Meta:
        # привязываем модель
        model = Отзыв

        # указываем поля, которые должен закончить юзер
        fields = ["текст", "картинка", "тег"]

        # если надо привязать значение Многие-Ко-Многим, то используем виджет
        widgets = {"тег": CheckboxSelectMultiple()}