# Generated by Django 3.2.8 on 2022-02-01 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0003_merge_0002_auto_20220201_0221_0002_auto_20220201_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='Nama_pemilihan',
            new_name='Judul',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='Tgl_Bln_Thn',
            new_name='Waktu',
        ),
    ]
