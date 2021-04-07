# Generated by Django 2.2.10 on 2021-04-07 11:37

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('pools', '0003_auto_20210407_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=500, verbose_name='Ответ')),
                ('poll', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='pools.Poll')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='pools.Person')),
            ],
        ),
    ]
