# Generated by Django 4.0.4 on 2022-05-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_students_options_rename_id_students_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]
