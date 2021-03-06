# Generated by Django 3.2.6 on 2021-09-09 04:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterJurusan',
            fields=[
                ('id_jurusan', models.CharField(choices=[('KGSP', 'KGSP'), ('SIJA', 'SIJA'), ('TEDK', 'TEDK'), ('TFLM', 'TFLM'), ('TMPO', 'TMPO'), ('TTL', 'TTL')], max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MasterKelas',
            fields=[
                ('id_kelas', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12'), ('13', '13')], max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MasterSiswa',
            fields=[
                ('nisn', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('id_jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.masterjurusan')),
                ('id_kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.masterkelas')),
            ],
        ),
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily', models.DateField(blank=True, default=None, null=True)),
                ('status', models.BooleanField()),
                ('checked_in', models.BooleanField()),
                ('checked_out', models.BooleanField()),
                ('checkin', models.DateTimeField(blank=True, default=None, null=True)),
                ('checkout', models.DateTimeField(blank=True, default=None, null=True)),
                ('id_absensi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.mastersiswa')),
            ],
        ),
    ]
