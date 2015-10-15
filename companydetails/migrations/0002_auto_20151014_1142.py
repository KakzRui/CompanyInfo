# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='email',
            field=models.EmailField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='phone',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
