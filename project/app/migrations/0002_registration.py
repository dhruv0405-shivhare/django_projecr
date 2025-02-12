# Generated by Django 5.1.6 on 2025-02-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('cpassword', models.CharField(max_length=50)),
            ],
        ),
    ]
