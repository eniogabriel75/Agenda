# Generated by Django 4.1.4 on 2022-12-12 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('events', '0011_tipos_alter_salas_options_eventos_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.user'),
            preserve_default=False,
        ),
    ]
