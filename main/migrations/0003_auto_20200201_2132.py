# Generated by Django 3.0 on 2020-02-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_artist_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='author',
        ),
        migrations.AddField(
            model_name='artist',
            name='background_image',
            field=models.ImageField(null=True, upload_to='media/background-image'),
        ),
    ]
