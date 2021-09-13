from rest_framework.fields import ReadOnlyField
from account.models import *
from rest_framework import serializers

# Serializers define the API representation.
class MasterSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterSiswa
        fields = ['nisn', 'name', 'username', 'password', 'id_kelas', 'id_jurusan']

class MasterKelasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterKelas
        fields = ['id_kelas']

class MasterJurusanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterJurusan
        fields = ['id_jurusan']

class AbsensiSerializer(serializers.ModelSerializer):
    class Meta:
        id_absensi = MasterSiswaSerializer(read_only=False)
        model = Absensi
        fields = ['id','id_absensi', 'daily', 'status', 'checkin', 'checkout', 'checked_in', 'checked_out']

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Absensi
        fields = ['id','id_absensi', 'daily', 'status', 'checkin', 'checkout', 'checked_in', 'checked_out']

