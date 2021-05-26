from django.db import models


class Table(models.Model):
    date = models.DateField(verbose_name="Дата")
    title = models.CharField(max_length=255, verbose_name="Название")
    count = models.IntegerField(verbose_name="Количество")
    distance = models.IntegerField(verbose_name="Расстояние")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"
