# Generated by Django 3.0 on 2020-02-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200201_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='link',
            field=models.URLField(null=True),
        ),
    ]
