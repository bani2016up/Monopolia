from django.db import models

# Create your models here.
class Banck_account(models.Model):
    name = models.CharField(max_length=64, verbose_name="Фамилия Имя")
    balanc = models.BigIntegerField(verbose_name='Баланс', default=10000)
    pin = models.IntegerField(max_length=4, verbose_name="Секретный Пин")
    
    def __str__(self):
        return self.name