# Generated by Django 3.0 on 2020-02-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200205_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
