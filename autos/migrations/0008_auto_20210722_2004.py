# Generated by Django 3.2.5 on 2021-07-22 14:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0007_alter_makecreate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoscreate',
            name='mileage',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='autoscreate',
            name='nickname',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Nickname Must be greater than 1 character')]),
        ),
        migrations.AlterField(
            model_name='makecreate',
            name='name',
            field=models.CharField(help_text='Enter a Make (e.g. Dodge)', max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Make Must be greater than 1 character')]),
        ),
    ]