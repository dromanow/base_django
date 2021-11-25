from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class SomeOtherModel(models.Model):
    value = models.CharField(max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    # objects = CurrentSiteManager()

    def __str__(self):
        return self.value


class CustomQuerySet(models.QuerySet):
    def value_filter(self):
        return self.filter(value='value1')


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

    def value_filter(self):
        return self.get_queryset().value_filter()


class SomeModel(models.Model):
    value = models.CharField(max_length=64)
    other = models.ForeignKey(SomeOtherModel, null=True, on_delete=models.CASCADE)
    other1 = models.ManyToManyField(SomeOtherModel, related_name='others')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    # objects = CustomManager()
    # objects = models.Manager()
    # on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.value
