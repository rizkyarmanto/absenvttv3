from django.contrib import admin

from .models import *

# Register your models here.

class AbsensiAdmin(admin.ModelAdmin):
    readonly_fields = [
                        'id',
                        'checkin',
                        'checkout',
    ]


admin.site.register(MasterSiswa)
admin.site.register(MasterJurusan)
admin.site.register(MasterKelas)
admin.site.register(Absensi, AbsensiAdmin)


