from django.db import models


class Sample(models.Model):
    title = models.CharField(max_length=20)
    image = models.FileField(max_length=30)
