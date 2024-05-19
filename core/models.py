from django.db import models
import datetime

class Animal(models.Model):
    TYPE_CHOICES = (
        ('mammal', 'Млекопитающее'),
        ('fish', 'Рыба'),
        ('reptile', 'Рептилия'),
        ('birds', 'Пернатые'),
    )

    name = models.CharField('Название', max_length=100)
    type = models.CharField('Род', max_length=100, choices=TYPE_CHOICES, default='mammal')

    information = models.TextField('Информация', blank=True)
    population = models.PositiveIntegerField('Популяция', default=0)
    is_rare = models.BooleanField('Вымерающие животные', default=False)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name

class Sot(models.Model):
    first_name = models.CharField('', max_length=30)
    last_name = models.CharField('', max_length=30)
    patronymic = models.CharField('', max_length=30, blank=True)

    date_of_birth = models.DateField('Дата рождения')
    picture = models.ImageField('Фото сотрудника', upload_to='pictures', null=True, blank=True)
    salary = models.DecimalField('Заработная плата', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Matematic(models.Model):
    name = models.CharField('Слово', max_length=100)
    long_text = models.TextField('Длинный текст', blank=True)
    class Meta:
        verbose_name = 'Переворот'
        verbose_name_plural = 'Переворот'

    def __str__(self) -> str:
        return self.name[::-1]

