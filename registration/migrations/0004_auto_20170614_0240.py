# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170613_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinfo',
            name='company_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='company_mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
