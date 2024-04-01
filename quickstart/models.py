from django.db import models

class RouteToRes(models.Model):
    payload = models.CharField(max_length=50, verbose_name="Ссылка на урок")
