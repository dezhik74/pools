# Generated by Django 2.2.10 on 2021-04-11 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0017_auto_20210411_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollResultQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500, verbose_name='Текст вопроса')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='poll_result',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(default='', max_length=500, verbose_name='Текст варианта ответа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pollresult',
            name='poll_result_name',
            field=models.CharField(default='', max_length=250, verbose_name='Название опроса'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AnswerVariant',
        ),
        migrations.AddField(
            model_name='pollresultquestion',
            name='poll_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.PollResult', verbose_name='Результаты опроса'),
        ),
        migrations.AddField(
            model_name='answer',
            name='poll_result_question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='pools.PollResultQuestion', verbose_name='Ответ'),
            preserve_default=False,
        ),
    ]
