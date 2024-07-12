from django.db import models
from trainer.models import Trainer
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.utils import timezone

class Client(AbstractUser):
    GENDER_CHOICES = [
        ('erkek', 'Erkek'),
        ('kadin', 'Kadın'),
        ('diger', 'Diğer'),
    ]
    SPECIALIZATION_CHOICES = [
        ('kilo_alma', 'Kilo Alma'),
        ('kilo_verme', 'Kilo Verme'),
        ('kilo_koruma', 'Kilo Koruma'),
        ('kas_kazanma', 'Kas Kazanma'),
    ]
    username = None
    client_first_name = models.CharField(max_length=255)
    client_last_name = models.CharField(max_length=255)
    client_email = models.EmailField(unique=True)
    client_birthdate = models.DateField()
    client_hedef = models.CharField(max_length=20, choices=SPECIALIZATION_CHOICES, default="kilo_kazanma")
    client_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)  
    client_phone_number = models.CharField(max_length=15)
    assigned_trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'client_email'
    groups = models.ManyToManyField(Group, related_name='client_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='client_permissions')
    
# İlerleme kaydı modeli
class IlerlemeKaydi(models.Model):
    assigned_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ilerleme_kayitlari')
    boy = models.DecimalField(max_digits=5, decimal_places=2)  # Örnek olarak boyu decimal olarak saklıyoruz.
    kilo = models.DecimalField(max_digits=5, decimal_places=2)
    yag_orani = models.DecimalField(max_digits=5, decimal_places=2)
    kas_kutlesi = models.DecimalField(max_digits=5, decimal_places=2)
    vucut_kitle_endeksi = models.DecimalField(max_digits=5, decimal_places=2)
    tarih = models.DateField(auto_now_add=True)


## Antrenör - Danışan ilişkisi
class Eslesme(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


## Mesajlaşma
class ClientMesaj(models.Model):
    gonderen_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    alan_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

class TrainerMesaj(models.Model):
    gonderen_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    alan_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

## Beslenme planı modeli
class BeslenmePlani(models.Model):
    BESLENME_GOAL_CHOICES = [
        ('kilo_alma', 'Kilo Alma'),
        ('kilo_verme', 'Kilo Verme'),
        ('kilo_koruma', 'Kilo Koruma'),
        ('kas_kazanma', 'Kas Kazanma'),
    ]

    beslenme_gonderen_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    beslenme_alan_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    beslenme_hedef = models.CharField(max_length=20, choices=BESLENME_GOAL_CHOICES)
    gunluk_ogun = models.TextField()  # Günlük öğünlerin açıklamalarını içerir
    kalori_hedef = models.PositiveIntegerField()
    tarih = models.DateTimeField( default=timezone.now)


## Egzersiz planı modeli
class EgzersizPlani(models.Model):
    EGZERSİZ_GOAL_CHOICES = [
        ('kilo_alma', 'Kilo Alma'),
        ('kilo_verme', 'Kilo Verme'),
        ('kilo_koruma', 'Kilo Koruma'),
        ('kas_kazanma', 'Kas Kazanma'),
    ]

    egzersiz_gonderen_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    egzersiz_alan_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    egzersiz_adi = models.CharField(max_length=255)
    egzersiz_hedef = models.CharField(max_length=20, choices=EGZERSİZ_GOAL_CHOICES)
    set_sayisi = models.PositiveIntegerField()
    tekrar_sayisi = models.PositiveIntegerField()
    video_url = models.URLField(blank=True, null=True)
    baslangic_tarihi = models.DateField()
    program_suresi = models.PositiveIntegerField()
    gonderilen_tarih = models.DateTimeField(default=timezone.now)