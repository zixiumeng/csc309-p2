# Generated by Django 4.1.7 on 2023-03-07 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0010_bank_owner_alter_bank_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='banks.bank'),
        ),
    ]