from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    photo = models.ImageField(upload_to='static/items', verbose_name="Фото")
    description = models.CharField(max_length=500, verbose_name="Описание фото", default="", null=True, blank=True)
