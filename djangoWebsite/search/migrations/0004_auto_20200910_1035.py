# Generated by Django 2.0.13 on 2020-09-10 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200910_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='emoji',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='user_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='media',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='related_hashtags',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='twitter_data',
            name='retweets',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='twitterjson',
            name='_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]