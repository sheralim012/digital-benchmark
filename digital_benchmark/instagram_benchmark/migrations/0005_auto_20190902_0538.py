# Generated by Django 2.2.4 on 2019-09-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram_benchmark', '0004_auto_20190902_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagrammediacomments',
            name='comment_by',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='instagrammediacomments',
            name='comment_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='instagrammediainsight',
            name='filter_used',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='instagrammediainsight',
            name='media_caption',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='instagrammediainsight',
            name='media_tags',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='instagrammediainsight',
            name='people_tagged',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='instagramusermedia',
            name='media_url',
            field=models.TextField(default=''),
        ),
    ]