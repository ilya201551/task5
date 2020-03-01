# Generated by Django 3.0.3 on 2020-03-01 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200229_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='homework',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='courses.Homework'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solution',
            name='lecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_solution', to='courses.Lecture'),
        ),
    ]