# Generated by Django 3.2.11 on 2022-02-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220204_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='panitia',
            field=models.BooleanField(default=False, verbose_name='panitia'),
        ),
    ]
