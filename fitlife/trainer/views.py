from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from trainer.models import Trainer
from client.models import Client, IlerlemeKaydi , BeslenmePlani, EgzersizPlani
# Create your views here.

def trainer_login(request):
    if request.method == 'POST':
        # Kullanıcının girdiği değerleri al
        trainer_email = request.POST['emailTrainerLogin']
        trainer_password = request.POST['passTrainerLogin']
        try:
            trainer = Trainer.objects.get(trainer_email=trainer_email, trainer_password=trainer_password)
            return render(request, "trainer/profil.html", {'trainer':trainer})
        except Trainer.DoesNotExist:
            return render(request, "trainer/trainer_login.html")
        
    return render(request, "trainer/trainer_login.html")

def profil_info(request, pk):
    trainer = Trainer.objects.get(id=pk)
    return render(request, "trainer/profil.html", {'trainer':trainer})

def trainer_guncelle(request, pk):
    trainer = Trainer.objects.get(id=pk)
    if request.method == 'POST':
        trainer.trainer_first_name = request.POST['inputTrainerFirstName']
        trainer.trainer_last_name = request.POST['inputTrainerLN']
        trainer.trainer_birthdate = request.POST['inputTrainerBD']
        trainer.trainer_gender = request.POST['inputTrainerGender']
        trainer.trainer_phone_number = request.POST['inputTrainerPhone']
        trainer.trainer_experiences = request.POST['inputTrainerTecrube']
        trainer.trainer_email = request.POST['inputTrainerEmail']
        trainer.trainer_password = request.POST['inputTrainerPassword']
        trainer.save() 
        return render(request, "trainer/profil.html",{'trainer':trainer})
    return render(request, "trainer/trainer_guncelle.html", {'trainer':trainer})

def danisan_info(request, pk):
    trainer = Trainer.objects.get(id=pk)
    assigned_clients = Client.objects.filter(assigned_trainer=trainer)
    return render(request, "trainer/danisan_info.html", {'assigned_clients':assigned_clients , 'trainer':trainer})

def danisan_detail(request, pk):
    client = Client.objects.get(id=pk)
    trainer = client.assigned_trainer
    ilerleme_kaydi = IlerlemeKaydi.objects.filter(assigned_client = client)
    context = {'client':client ,'trainer':trainer ,'ilerleme_kaydi':ilerleme_kaydi}
    return render(request, "trainer/danisan_detail.html", context)

def beslenme_plani(request, pk):
    trainer = Trainer.objects.get(id = pk)
    assigned_clients = Client.objects.filter(assigned_trainer=trainer)
    beslenme_plani = BeslenmePlani.objects.filter(beslenme_gonderen_trainer = trainer)
    context = {'trainer': trainer, 'beslenme_plani': beslenme_plani}
    print(beslenme_plani)
    return render(request, "trainer/beslenme_plani.html",context)

def beslenme_hazirla(request, pk):
    trainer = Trainer.objects.get(id=pk)
    beslenme_plani = BeslenmePlani.objects.filter(beslenme_gonderen_trainer = trainer)
    assigned_clients = Client.objects.filter(assigned_trainer=trainer)
    if request.method == 'POST':
        beslenme_gonderen_trainer = trainer
        beslenme_hedef = request.POST['inputBeslenmeHedef']
        gunluk_ogun = request.POST['inputGunlukOgun']
        kalori_hedef = request.POST['inputKaloriHedef']
        beslenme_alan_client_id = request.POST['inputGonDanisan']

        beslenme_alan_client = Client.objects.get(id=beslenme_alan_client_id)

        new_user = BeslenmePlani(
            beslenme_gonderen_trainer=beslenme_gonderen_trainer,
            beslenme_hedef=beslenme_hedef,
            gunluk_ogun=gunluk_ogun,
            kalori_hedef = kalori_hedef,
            beslenme_alan_client=beslenme_alan_client,
        )  
        new_user.save()
        return render(request, "trainer/beslenme_plani.html",{'trainer': trainer, 'assigned_clients': assigned_clients, 'beslenme_plani': beslenme_plani}) 
    return render(request, "trainer/beslenme_hazirla.html", {'trainer': trainer, 'assigned_clients': assigned_clients,'beslenme_plani': beslenme_plani}) 

def beslenme_guncelle(request, pk):
    beslenme_plani_tek = BeslenmePlani.objects.get(id=pk)
    trainer = beslenme_plani_tek.beslenme_gonderen_trainer
    
    if request.method == 'POST':
        beslenme_plani_tek.beslenme_hedef = request.POST['inputBeslenmeHedef']
        beslenme_plani_tek.gunluk_ogun = request.POST['inputGunlukOgun']
        beslenme_plani_tek.kalori_hedef = request.POST['inputKaloriHedef']
        beslenme_plani_tek.save() 


        beslenme_plani = BeslenmePlani.objects.filter(beslenme_gonderen_trainer = trainer)
        return render(request, "trainer/beslenme_plani.html",{'trainer':trainer, 'beslenme_plani':beslenme_plani})

    return render(request, "trainer/beslenme_guncelle.html", {'trainer': trainer, 'beslenme_plani_tek': beslenme_plani_tek})

def beslenme_sil(request, pk):
    delete_beslenme = BeslenmePlani.objects.get(id=pk)
    delete_beslenme.delete()
    trainer = delete_beslenme.beslenme_gonderen_trainer
    beslenme_plani = BeslenmePlani.objects.filter(beslenme_gonderen_trainer = trainer)
    return render(request, "trainer/beslenme_plani.html",{'trainer': trainer, 'beslenme_plani': beslenme_plani})

def egzersiz_plani(request, pk):
    trainer = Trainer.objects.get(id = pk)
    assigned_clients = Client.objects.filter(assigned_trainer=trainer)
    egzersiz_plani = EgzersizPlani.objects.filter(egzersiz_gonderen_trainer= trainer)
    context = {'trainer': trainer, 'egzersiz_plani': egzersiz_plani, 'assigned_clients':assigned_clients}
    return render(request, "trainer/egzersiz_plani.html", context)

def egzersiz_hazirla(request, pk):
    trainer = Trainer.objects.get(id=pk)
    egzersiz_plani = EgzersizPlani.objects.filter(egzersiz_gonderen_trainer = trainer)
    assigned_clients = Client.objects.filter(assigned_trainer=trainer)
    if request.method == 'POST':
        egzersiz_gonderen_trainer = trainer
        egzersiz_adi = request.POST['inputEgzersizAd']
        egzersiz_hedef = request.POST['inputEgzersizHedef']
        set_sayisi = request.POST['inputSet']
        tekrar_sayisi = request.POST['inputTekrar']
        video_url = request.POST['inputVideo']
        baslangic_tarihi = request.POST['inputBaslangicTarihi']
        program_suresi = request.POST['inputProgSure']
        egzersiz_alan_client_id = request.POST['inputGonDanisan']

        egzersiz_alan_client = Client.objects.get(id=egzersiz_alan_client_id)

        new_user = EgzersizPlani(
            egzersiz_gonderen_trainer=egzersiz_gonderen_trainer,
            egzersiz_adi=egzersiz_adi,
            egzersiz_hedef=egzersiz_hedef,
            set_sayisi = set_sayisi,
            tekrar_sayisi = tekrar_sayisi,
            video_url = video_url,
            baslangic_tarihi = baslangic_tarihi,
            program_suresi = program_suresi,
            egzersiz_alan_client=egzersiz_alan_client,
        )  
        new_user.save()
        return render(request, "trainer/egzersiz_plani.html",{'trainer': trainer, 'assigned_clients': assigned_clients, 'egzersiz_plani': egzersiz_plani}) 
    return render(request, "trainer/egzersiz_hazirla.html", {'trainer': trainer, 'assigned_clients': assigned_clients,'egzersiz_plani': egzersiz_plani}) 

def trainer_egzersiz_detail(request, pk):
    egzersiz_plani = EgzersizPlani.objects.get(id=pk)
    trainer = egzersiz_plani.egzersiz_gonderen_trainer
    print(egzersiz_plani)
    return render(request, "trainer/trainer_egzersiz_detail.html", {'egzersiz_plani':egzersiz_plani, 'trainer':trainer})

def egzersiz_guncelle(request, pk):
    egzersiz_plani_tek = EgzersizPlani.objects.get(id=pk)
    trainer = egzersiz_plani_tek.egzersiz_gonderen_trainer
    
    if request.method == 'POST':
        egzersiz_plani_tek.egzersiz_adi = request.POST['inputEgzersizAd']
        egzersiz_plani_tek.egzersiz_hedef = request.POST['inputEgzersizHedef']
        egzersiz_plani_tek.set_sayisi = request.POST['inputSet']
        egzersiz_plani_tek.tekrar_sayisi = request.POST['inputTekrar']
        egzersiz_plani_tek.video_url = request.POST['inputVideo']
        egzersiz_plani_tek.baslangic_tarihi = request.POST['inputBaslangicTarihi']
        egzersiz_plani_tek.program_suresi = request.POST['inputProgSure']
        egzersiz_plani_tek.save() 



        egzersiz_plani = EgzersizPlani.objects.filter(egzersiz_gonderen_trainer = trainer)
        return render(request, "trainer/egzersiz_plani.html",{'trainer':trainer, 'egzersiz_plani':egzersiz_plani})

    return render(request, "trainer/egzersiz_guncelle.html", {'trainer': trainer, 'egzersiz_plani_tek': egzersiz_plani_tek})
    

def egzersiz_sil(request, pk):
    delete_egzersiz = EgzersizPlani.objects.get(id=pk)
    delete_egzersiz.delete()
    trainer = delete_egzersiz.egzersiz_gonderen_trainer
    egzersiz_plani = EgzersizPlani.objects.filter(egzersiz_gonderen_trainer = trainer)
    return render(request, "trainer/egzersiz_plani.html",{'trainer': trainer, 'egzersiz_plani': egzersiz_plani})

def trainer_logout(request):
    return render(request,"trainer/trainer_login.html")