# Generated by Django 3.2.3 on 2021-05-26 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0011_alter_parent_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='child',
            field=models.ManyToManyField(to='daycares.Child'),
        ),
    ]