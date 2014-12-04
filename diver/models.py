from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SIZE_CHOICES = (
    ('s', u'Small'),
    ('m', u'medium'),
)


class Diver(models.Model):
    diver = models.OneToOneField(User) # username, firstname, lastname, password, email, is_active, is_staff, ...etc
    phone = models.PositiveIntegerField()
    age = models.PositiveSmallIntegerField()
    size = models.CharField(max_length=30, choices=SIZE_CHOICES)

    def __unicode__(self):
        return u"{}".format(self.diver.get_full_name())