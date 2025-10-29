from django.db import models

# импортируем стандартную модель пользователя
from django.contrib.auth import get_user_model

# автоматически создаём класс пользователя
Юзер = get_user_model()
# потом этого юзера будем привязывать в качестве свойства для других людей


# каждая модель (каждый класс) наследуются от стандартного класс джанго(принимает его стандартные свойства). 
class Отзыв(models.Model):
    автор = models.ForeignKey(Юзер, on_delete=models.CASCADE)
    # каждая переменная класса - это название поля(колонки и таблицы)
    дата_поста = models.DateTimeField(
        # это поле автоматически считывает время компьютера и присваевает его тв качестве6 значения в момент создания записи в БД
        auto_now=True
    )
    картинка = models.ImageField(
        # в скобках указываем, в какую папку загружать новые картинки
        upload_to="медиа"
    )

    текст = models.TextField()

    class Meta:
            verbose_name = "Отзыв"
            verbose_name_plural = "Отзывы"

    def __str__(self):
          if len(self.текст) > 50:
                return self.текст[:50] + "..."
          return self.текст
