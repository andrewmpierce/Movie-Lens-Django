# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rating_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
