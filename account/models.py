from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.

class MasterKelas(models.Model):
    category_kelas          = (
                                ('10', '10'),
                                ('11', '11'),
                                ('12', '12'),
                                ('13', '13'),
                            )
    id_kelas                   = models.CharField(primary_key=True, max_length=100, choices=category_kelas)

    def __str__(self):
        return f'{self.id_kelas}'
    
class MasterJurusan(models.Model):
    category_jurusan        = (
                                ('KGSP', 'KGSP'),
                                ('SIJA', 'SIJA'),
                                ('TEDK', 'TEDK'),
                                ('TFLM', 'TFLM'),
                                ('TMPO', 'TMPO'),
                                ('TTL', 'TTL'),
                            )
    id_jurusan                 = models.CharField(primary_key=True, max_length=100, choices=category_jurusan)

    def __str__(self):
        return f'{self.id_jurusan}'

class MasterSiswa(models.Model):
    nisn                    = models.CharField(primary_key=True, unique=True,  max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    name                    = models.CharField(max_length=100)
    username                = models.CharField(max_length=16, unique=True)
    password                = models.CharField(max_length=32)
    id_kelas                = models.ForeignKey(MasterKelas, on_delete=models.CASCADE)
    id_jurusan              = models.ForeignKey(MasterJurusan, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nisn}'

class Absensi(models.Model):
    id_absensi              = models.CharField(max_length=100)
    daily                   = models.DateField(null=True, blank=True, default=None)
    status                  = models.BooleanField()
    checked_in              = models.BooleanField()
    checked_out             = models.BooleanField()   
    checkin                 = models.DateTimeField(null=True, blank=True, default=None)
    checkout                = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.id_absensi}'

class Akun(models.Model):
    nama = models.CharField(blank=True, null=True, max_length=225)
    password = models.CharField(blank=True, null=True, max_length=225)
