from django.db import models

# импортируем стандартную модель пользователя
from django.contrib.auth import get_user_model

# автоматически создаём класс пользователя
Юзер = get_user_model()
# потом этого юзера будем привязывать в качестве свойства для других людей


# каждая модель (каждый класс) наследуются от стандартного класс джанго(принимает его стандартные свойства). 
class Тег(models.Model):
    текст = models.TextField()

    class Meta:
            verbose_name = "Тег"
            verbose_name_plural = "Теги"

    def __str__(self):
          if len(self.текст) > 50:
                return self.текст[:50] + "..."
          return self.текст
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

    тег = models.ManyToManyField(Тег, through="ОтзывыТеги", blank=True)

    class Meta:
            verbose_name = "Отзыв"
            verbose_name_plural = "Отзывы"

    def __str__(self):
          if len(self.текст) > 50:
                return self.текст[:50] + "..."
          return self.текст
class Аватарка(models.Model):
    юзер = models.OneToOneField(Юзер, on_delete=models.CASCADE)
    картинка = models.ImageField(
        upload_to="аватарки"
    )

    class Meta:
            verbose_name = "Аватарка"
            verbose_name_plural = "Аватарки"
    def __str__(self):
          return self.юзер.username
    
    
class ОтзывыТеги(models.Model):
      отзыв = models.ForeignKey(Отзыв, on_delete=models.CASCADE)
      тег = models.ForeignKey(Тег, on_delete=models.CASCADE)