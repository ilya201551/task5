# Generated by Django 3.0.3 on 2020-02-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_homework_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='finishedhomework',
            name='mark',
        ),
        migrations.AlterField(
            model_name='finishedhomework',
            name='solution',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]
