# Generated by Django 3.0.3 on 2020-03-01 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20200301_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='lecture',
        ),
    ]
