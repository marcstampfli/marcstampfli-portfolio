# Generated by Django 2.1.7 on 2019-03-21 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20190320_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.Client', verbose_name='Client Name'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/projects'),
        ),
    ]
