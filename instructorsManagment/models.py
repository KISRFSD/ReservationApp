from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.


class Instructor(models.Model):
    inst = models.OneToOneField(User)
    mobile = models.BigIntegerField(max_length=8,
                                    validators=[
                                        RegexValidator(
                                            regex='[2]\d{7}|[5]\d{7}|[6]\d{7}|[9]\d{7}',
                                            message='Invalid mobile number'),])
    membership = models.BigIntegerField()

    def __unicode__(self):
        return u"{}".format(self.inst.get_full_name())
