# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Company Details',
            },
            bases=(models.Model,),
        ),
    ]
