# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companydetails', '0008_ownerdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ownerdetails',
            old_name='company_id',
            new_name='company',
        ),
    ]
