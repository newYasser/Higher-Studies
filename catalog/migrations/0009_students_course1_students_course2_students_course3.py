# Generated by Django 4.0.4 on 2022-05-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_students_course1_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='course1',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='course2',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='course3',
            field=models.CharField(max_length=8, null=True),
        ),
    ]