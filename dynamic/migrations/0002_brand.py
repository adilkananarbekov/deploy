# Generated by Django 5.1.2 on 2024-10-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]