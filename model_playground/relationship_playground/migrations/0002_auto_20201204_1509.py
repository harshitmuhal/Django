# Generated by Django 3.1.4 on 2020-12-04 15:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desgination', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('toppings', models.ManyToManyField(to='relationship_playground.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('societies', models.ManyToManyField(through='relationship_playground.Membership', to='relationship_playground.Society')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='society_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.society'),
        ),
    ]
