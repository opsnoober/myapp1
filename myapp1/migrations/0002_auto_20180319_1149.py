# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cal',
            name='bcs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cal',
            name='cs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cal',
            name='result',
            field=models.IntegerField(),
        ),
    ]
