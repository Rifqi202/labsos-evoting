# Generated by Django 3.2.8 on 2022-02-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0005_alter_vote_judul'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='Judul',
            field=models.TextField(),
        ),
    ]
