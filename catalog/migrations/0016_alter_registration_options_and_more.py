# Generated by Django 4.0.4 on 2022-05-24 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_remove_registration_id_alter_registration_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['student_ID']},
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='ID',
            new_name='student_ID',
        ),
    ]