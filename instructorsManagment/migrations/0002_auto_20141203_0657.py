# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('instructorsManagment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='mobile',
            field=models.BigIntegerField(max_length=8, validators=[django.core.validators.RegexValidator(regex=b'[2]\\d{7}|[5]\\d{7}|[6]\\d{7}|[9]\\d{7}', message=b'Invalid mobile number')]),
            preserve_default=True,
        ),
    ]
