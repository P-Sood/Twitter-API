# Generated by Django 3.0.5 on 2020-08-04 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('text', models.CharField(max_length=280)),
                ('emoji', models.CharField(max_length=30)),
                ('likes', models.PositiveIntegerField()),
                ('search_term', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_data',
            fields=[
                ('keyData', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='search.data')),
                ('is_retweet', models.CharField(max_length=5)),
                ('is_thread', models.CharField(max_length=5)),
                ('media', models.CharField(max_length=30)),
                ('retweets', models.CharField(max_length=30)),
                ('related_hashtags', models.CharField(max_length=30)),
                ('external_links', models.TextField()),
                ('tweet_link', models.TextField()),
            ],
        ),
    ]