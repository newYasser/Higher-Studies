# Generated by Django 4.0.4 on 2022-05-20 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_students_university'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='staue',
            new_name='status',
        ),
    ]
