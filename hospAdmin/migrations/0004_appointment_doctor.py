# Generated by Django 5.0.2 on 2024-03-08 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospAdmin', '0003_remove_appointment_doctor'),
        ('hospDoctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospDoctor.doctor'),
        ),
    ]
