from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Instructor(models.Model):
    inst = models.OneToOneField(User)
    mobile = models.BigIntegerField(max_length=8)
    membership = models.BigIntegerField()

    def __unicode__(self):
        return u"{}".format(self.inst.get_full_name())
