# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('movie_id', models.PositiveSmallIntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('X', 'X')], default='X', max_length=1)),
                ('zipcode', models.CharField(max_length=15)),
                ('occupation', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(to='database.Movie')),
                ('rater', models.ForeignKey(to='database.Rater')),
            ],
        ),
    ]
