# Generated by Django 5.2 on 2025-05-09 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_student_studenteducation'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.PositiveBigIntegerField()),
                ('city', models.CharField(max_length=30)),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.student')),
            ],
        ),
    ]
