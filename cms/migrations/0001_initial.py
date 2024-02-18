# Generated by Django 5.0.2 on 2024-02-18 14:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-published_date'],
            },
        ),
    ]
