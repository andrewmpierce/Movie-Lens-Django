# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_rating_timestamp'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ratings',
            field=models.ManyToManyField(null=True, to='database.Rating'),
        ),
    ]
