# Generated by Django 2.2.10 on 2021-04-07 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0010_remove_variant_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='pools.Poll'),
        ),
    ]