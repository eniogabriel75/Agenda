# Generated by Django 4.1.3 on 2023-02-05 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_alter_eventos_local_alter_eventos_meals_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salas',
            old_name='tipo',
            new_name='tam',
        ),
    ]
