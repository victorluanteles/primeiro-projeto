# Generated by Django 2.2.1 on 2019-05-28 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APLICACAO', '0002_auto_20190528_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='peso1',
            new_name='peso',
        ),
    ]
