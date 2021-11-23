from django.db import models
from django.db.models.signals import post_save, ModelSignal
from django.dispatch import receiver, Signal

some_signal = Signal()


class HitCount(models.Model):
    path = models.CharField(max_length=256, primary_key=True)
    hits = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.path} ({self.hits})'

    def save(self, *args, **kwargs):
        some_signal.send(self, test=1)
        return super().save(*args, **kwargs)


@receiver(post_save, sender=HitCount)
def post_save_hit(sender, instance, *args, **kwargs):
    print(instance)


@receiver(some_signal)
def some_signal_hit(sender, *args, **kwargs):
    print(sender)


