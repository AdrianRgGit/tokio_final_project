# Generated by Django 5.0 on 2024-01-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_remove_movie_duration_remove_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=12321),
            preserve_default=False,
        ),
    ]
