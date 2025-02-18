# Generated by Django 5.0.2 on 2024-03-14 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0004_alter_clothingmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingmodel',
            name='manufacture',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(30)]),
        ),
        migrations.AlterField(
            model_name='clothingmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0, 'Price cant be negative'), django.core.validators.MaxValueValidator(500)]),
        ),
    ]
