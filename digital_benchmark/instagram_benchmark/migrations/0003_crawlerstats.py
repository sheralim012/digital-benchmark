# Generated by Django 2.2.4 on 2019-08-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_benchmark', '0002_auto_20190807_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlerStats',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('task_id', models.CharField(max_length=255)),
                ('unique_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=255)),
                ('user_scrapped', models.CharField(max_length=255)),
                ('no_of_media_scrapped', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]