# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ratings',
            field=models.ManyToManyField(to='database.Rating'),
        ),
    ]
