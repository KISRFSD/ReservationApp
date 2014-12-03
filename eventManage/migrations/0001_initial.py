# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructorsManagment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('destination', models.CharField(max_length=100)),
                ('event_status', models.BooleanField(default=True)),
                ('gathering_point', models.CharField(max_length=100)),
                ('max_seats', models.IntegerField()),
                ('note', models.TextField()),
                ('instructor', models.ForeignKey(to='instructorsManagment.Instructor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
