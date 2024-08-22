from django.contrib.auth.models import AbstractUser
from django.db import models

from lessons.models import Lesson, Course

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    phone = models.CharField(max_length=55, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='аватар', **NULLABLE)
    city = models.CharField(max_length=55, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        # Строковое отображение объекта
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Pay(models.Model):
    pay_type = {
        'Cash': "наличные",
        'Card': "перевод ",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    summ = models.IntegerField(verbose_name='')
    type_of_payment = models.CharField(choices=pay_type, verbose_name="Способ Оплаты")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.user
