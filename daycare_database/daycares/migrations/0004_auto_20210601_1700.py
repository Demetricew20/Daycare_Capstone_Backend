# Generated by Django 3.1.8 on 2021-06-02 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daycares', '0003_auto_20210601_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='age_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycares.agegroup'),
        ),
    ]
