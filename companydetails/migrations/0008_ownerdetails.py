# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0007_auto_20151015_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('company_id', models.ForeignKey(to='companydetails.CompanyDetails')),
            ],
            options={
                'verbose_name': 'OwnerDetails',
            },
            bases=(models.Model,),
        ),
    ]
