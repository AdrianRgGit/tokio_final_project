# Generated by Django 5.0 on 2024-01-10 10:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_movie_image'),
        ('user', '0004_rename_movie_id_favorite_movie_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='View',
            new_name='UserViewedContent',
        ),
    ]
