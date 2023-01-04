# Generated by Django 3.2.3 on 2022-05-24 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_rename_staue_students_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['ID']},
        ),
        migrations.RenameField(
            model_name='students',
            old_name='status',
            new_name='is_active',
        ),
        migrations.RemoveField(
            model_name='students',
            name='gpa',
        ),
        migrations.RemoveField(
            model_name='students',
            name='level',
        ),
        migrations.RemoveField(
            model_name='students',
            name='register',
        ),
        migrations.AlterField(
            model_name='students',
            name='course1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='catalog.courses'),
        ),
        migrations.AlterField(
            model_name='students',
            name='course2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='catalog.courses'),
        ),
        migrations.AlterField(
            model_name='students',
            name='course3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='catalog.courses'),
        ),
    ]
