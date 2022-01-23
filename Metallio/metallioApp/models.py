from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sekolah(models.Model):
    nama_sekolah = models.CharField(max_length=50)
    kota = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nama_sekolah
  


class Profile(models.Model):
    SUDAH = 'SUDAH'
    BELUM = 'BELUM'
    
    PEMBAYARAN = (
        (SUDAH, 'SUDAH'),
        (BELUM, 'BELUM')
    )
    
    fullName = models.CharField(null=True, max_length=100)
    nickName = models.CharField(null=True ,max_length=30)
    umur = models.IntegerField(null=True)
    asal_sekolah = models.ForeignKey(Sekolah, on_delete=models.CASCADE, null=True)
    no_telepon = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bukti_pembayaran = models.ImageField(null=True)
    pembayaran = models.CharField(max_length=10, choices=PEMBAYARAN, default=BELUM)
    profile_pic = models.ImageField(default="undraw_profile.svg", null=True)
    
    def __str__(self):
        return self.fullName
    
class Universitas(models.Model):
    nama_univ = models.CharField(max_length=100)
    kota = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama_univ
    
    
class Jurusan(models.Model):
    
    KATEGORI = (
        ('SAINTEK', 'SAINTEK'),
        ('SOSHUM', 'SOSHUM')
    )
    
    nama_jurusan = models.CharField(max_length=30)
    univ = models.ForeignKey(Universitas, on_delete=models.CASCADE)
    kategori = models.CharField(max_length=10, choices=KATEGORI)  
    
    def __str__(self):
        return self.nama_jurusan + " - " + str(self.univ)  
    
    
class Pilihan1(models.Model):
    id_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    pilihan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    
    
    
          
class Pilihan2(models.Model):
    id_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    pilihan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    
        
    
    
        
    

  