# Generated by Django 5.0.2 on 2024-05-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospAdmin', '0008_remove_session_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]