# Generated by Django 4.0.4 on 2022-05-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_courses_alter_students_course1_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='students',
            name='course1_id',
            field=models.IntegerField(default=None),
        ),
    ]
