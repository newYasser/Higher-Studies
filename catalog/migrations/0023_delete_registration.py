# Generated by Django 4.0.4 on 2022-05-24 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
    ]