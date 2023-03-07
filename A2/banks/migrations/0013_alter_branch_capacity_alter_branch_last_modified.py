# Generated by Django 4.1.7 on 2023-03-07 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0012_alter_branch_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='capacity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
