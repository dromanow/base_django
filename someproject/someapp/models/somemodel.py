from django.db import models


class SomeModel(models.Model):
    value = models.CharField(max_length=64)

    def __str__(self):
        return self.value
