# Generated by Django 5.0.6 on 2024-05-24 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('intake_date', models.DateTimeField(auto_now_add=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dog_shelters.shelter')),
            ],
        ),
    ]
