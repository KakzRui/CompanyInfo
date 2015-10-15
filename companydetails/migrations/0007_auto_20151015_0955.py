# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0006_auto_20151015_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='company_id',
            field=models.IntegerField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
    ]
