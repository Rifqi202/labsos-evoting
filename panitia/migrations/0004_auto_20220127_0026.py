# Generated by Django 3.2.8 on 2022-01-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitia', '0003_alter_daftarkandidat_tanggallahir'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daftarkandidat',
            name='alamat',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='misi',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='namakandidat',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='pengalaman',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='prestasi',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='programkerja',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='tempatlahir',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='daftarkandidat',
            name='visi',
            field=models.TextField(max_length=100),
        ),
    ]
