# Generated by Django 3.1.1 on 2020-09-10 18:44

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20200910_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposition',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
