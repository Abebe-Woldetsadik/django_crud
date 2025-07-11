# Generated by Django 5.2.3 on 2025-06-28 15:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudapp.gender')),
            ],
        ),
    ]
