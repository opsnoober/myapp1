# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cs', models.IntegerField(max_length=10)),
                ('bcs', models.IntegerField(max_length=10)),
                ('result', models.IntegerField(max_length=100)),
            ],
        ),
    ]
