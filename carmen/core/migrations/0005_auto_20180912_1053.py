# Generated by Django 2.0 on 2018-09-12 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180912_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pergunta',
            name='relaciona',
        ),
        migrations.AddField(
            model_name='relaciona',
            name='relaciona',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='relaciona', to='core.Pergunta'),
            preserve_default=False,
        ),
    ]