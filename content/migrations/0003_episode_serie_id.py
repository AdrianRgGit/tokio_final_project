# Generated by Django 5.0 on 2023-12-26 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_season_serie_alter_movie_options_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='serie_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='content.serie'),
            preserve_default=False,
        ),
    ]
