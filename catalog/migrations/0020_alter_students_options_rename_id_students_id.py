# Generated by Django 4.0.4 on 2022-05-24 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_students_options_rename_id_students_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['ID']},
        ),
        migrations.RenameField(
            model_name='students',
            old_name='id',
            new_name='ID',
        ),
    ]
