# Generated by Django 4.2.1 on 2023-06-21 00:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_alter_comments_news_alter_favorites_news_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newsfeel",
            name="feeling",
        ),
        migrations.RemoveField(
            model_name="newsfeel",
            name="news",
        ),
        migrations.RemoveField(
            model_name="newsfeel",
            name="user",
        ),
        migrations.DeleteModel(
            name="Feeling",
        ),
        migrations.DeleteModel(
            name="NewsFeel",
        ),
    ]
