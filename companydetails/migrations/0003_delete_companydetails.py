# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0002_auto_20151014_1142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyDetails',
        ),
    ]
