# Generated by Django 2.2.10 on 2021-04-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0005_auto_20210407_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='pools.Poll'),
        ),
    ]
