# Generated by Django 4.1.4 on 2022-12-09 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_eventos_registrationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='registrationDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
