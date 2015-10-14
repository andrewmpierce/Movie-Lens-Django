# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='text',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
