# Generated by Django 5.1.2 on 2024-10-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0003_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('we_help', models.TextField()),
            ],
        ),
    ]
