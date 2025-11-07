from django.contrib import admin
from .models import *


class ОтзывыТегиИнлайн(admin.TabularInline):
    model = ОтзывыТеги

class ОтзывАдмин(admin.ModelAdmin):
    inlines = [ОтзывыТегиИнлайн]

admin.site.register(Отзыв, ОтзывАдмин)
admin.site.register([Аватарка, Тег])

