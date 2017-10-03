from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    descriptions = models.TextField()

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.phone)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'
