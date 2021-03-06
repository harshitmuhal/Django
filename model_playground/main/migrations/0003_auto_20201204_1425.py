# Generated by Django 3.1.4 on 2020-12-04 14:25

import django.core.validators
from django.db import migrations, models
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201204_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0), main.validators.validate_even_number]),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.EmailValidator('Email address is not valid')]),
        ),
    ]
