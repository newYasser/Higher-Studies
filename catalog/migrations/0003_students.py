# Generated by Django 4.0.4 on 2022-05-19 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('birth', models.DateField()),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('gender', models.CharField(max_length=6)),
                ('level', models.IntegerField()),
                ('staue', models.BooleanField(default=True)),
                ('dep', models.CharField(max_length=20)),
            ],
        ),
    ]