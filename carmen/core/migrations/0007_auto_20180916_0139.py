# Generated by Django 2.0 on 2018-09-16 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180912_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='user',
            new_name='usuario',
        ),
    ]
