# Generated by Django 2.1.7 on 2019-03-21 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_profile_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(blank=True, max_length=255, verbose_name='LinkedIn'),
        ),
    ]
