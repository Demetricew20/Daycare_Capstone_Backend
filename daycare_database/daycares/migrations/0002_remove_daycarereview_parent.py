# Generated by Django 3.1.8 on 2021-06-04 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daycarereview',
            name='parent',
        ),
    ]
