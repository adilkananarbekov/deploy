# Generated by Django 5.1.2 on 2024-10-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0005_takecare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takecare',
            name='title',
        ),
    ]
