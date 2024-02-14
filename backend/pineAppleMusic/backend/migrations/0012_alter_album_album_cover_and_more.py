# Generated by Django 4.1.4 on 2023-01-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0011_alter_user_gender_alter_user_is_artist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="album_cover",
            field=models.ImageField(blank=True, upload_to="album_covers/"),
        ),
        migrations.AlterField(
            model_name="playlist",
            name="playlist_cover",
            field=models.ImageField(blank=True, upload_to="playlist_covers/"),
        ),
        migrations.AlterField(
            model_name="song",
            name="song_cover",
            field=models.ImageField(blank=True, upload_to="song_covers/"),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="profile_pictures/"),
        ),
    ]