# Generated by Django 5.1.2 on 2024-10-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0006_remove_takecare_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]