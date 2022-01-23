import imp
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sekolah)
admin.site.register(Profile)
admin.site.register(Universitas)
admin.site.register(Jurusan)
admin.site.register(Pilihan1)
admin.site.register(Pilihan2)