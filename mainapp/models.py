from django.db import models

# Create your models here.
class Joint_training(models.Model):
    DAY_CHOICES = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)

    trenning = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return f'{self.get_day_display()} - Задачи: {self.tasks}'

class Events(models.Model):
    date = models.DateField()
    event = models.CharField()
    icon = models.ImageField()
    description = models.CharField()

class Galery(models.Model):
    image = models.ImageField()
    description = models.CharField()
