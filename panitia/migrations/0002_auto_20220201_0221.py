# Generated by Django 3.2.8 on 2022-02-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tgl_Bln_Thn', models.DateField()),
                ('Nama_pemilihan', models.TextField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='judul',
        ),
    ]
