from django.db import models


class SomeOtherModel(models.Model):
    value = models.CharField(max_length=64)

    def __str__(self):
        return self.value


class SomeModel(models.Model):
    value = models.CharField(max_length=64)
    other = models.ForeignKey(SomeOtherModel, null=True, on_delete=models.CASCADE)
    other1 = models.ManyToManyField(SomeOtherModel, related_name='other1')

    def __str__(self):
        return self.value
