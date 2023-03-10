# Generated by Django 4.1.4 on 2022-12-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matter', models.CharField(max_length=80)),
                ('date', models.DateField()),
                ('timeStart', models.DateTimeField()),
                ('timeEnd', models.DateTimeField()),
                ('meals', models.DecimalField(decimal_places=3, max_digits=3)),
                ('local', models.CharField(max_length=50)),
            ],
        ),
    ]
