# Generated by Django 2.2.10 on 2021-04-07 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0002_auto_20210407_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='description',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='question',
        ),
        migrations.AddField(
            model_name='poll',
            name='attribute',
            field=models.CharField(choices=[('text', 'Текст'), ('one', 'Один вариант'), ('many', 'Несколько вариантов')], default='text', max_length=4),
        ),
        migrations.AddField(
            model_name='poll',
            name='question_text',
            field=models.CharField(default=2, max_length=500, verbose_name='Сам вопрос'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variant',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='pools.Poll'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
