# Generated by Django 4.1.7 on 2023-03-06 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0005_alter_branch_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='last_modified',
            field=models.TimeField(default=datetime.datetime(2023, 3, 6, 0, 41, 17, 52135)),
        ),
    ]
