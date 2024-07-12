from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from trainer.models import Trainer
from client.models import Client
from yonetici.yonetici_info import YoneticiInfo



def yonetici_login(request):
    if request.method == 'POST':
        # Kullanıcının girdiği değerleri al
        yonetici_email = request.POST['emailYonLogin']
        yonetici_password = request.POST['passYonLogin']

        # SabitDegerler sınıfından bir nesne oluştur
        yonetici_infolari = YoneticiInfo()

        # Sabit değerlerle karşılaştırma yap
        if yonetici_email == yonetici_infolari.yonetici_email and yonetici_password == yonetici_infolari.yonetici_password:
            # Değerler eşleşirse başka bir sayfaya yönlendir
            return render(request, "yonetici/trainer_add.html")
        else:
            # Değerler eşleşmezse aynı sayfada kal ve bir hata mesajı göster
            return render(request, 'yonetici/yonetici_login.html')

    return render(request, "yonetici/yonetici_login.html")

def trainer_add(request):
    if request.method == 'POST':
        
                trainer_first_name = request.POST['inputTrainerFN']
                trainer_last_name = request.POST['inputTrainerLN']
                trainer_birthdate = request.POST['inputTrainerBD']
                trainer_gender = request.POST['inputTrainerGender']
                trainer_phone_number = request.POST['inputTrainerPhone']
                trainer_uzmanlık = request.POST['inputTrainerUzmanlik']
                trainer_experiences = request.POST['inputTrainerTecrube']
                trainer_kont = request.POST['inputTrainerKont']
                trainer_email = request.POST['inputTrainerEmail']
                trainer_password = request.POST['inputTrainerPassword']

                new_user = Trainer(
                    trainer_first_name=trainer_first_name,
                    trainer_last_name=trainer_last_name,
                    trainer_birthdate=trainer_birthdate,
                    trainer_gender=trainer_gender,
                    trainer_phone_number=trainer_phone_number,
                    trainer_uzmanlık=trainer_uzmanlık,
                    trainer_experiences=trainer_experiences,
                    trainer_kont=trainer_kont,
                    trainer_email=trainer_email,
                    trainer_password=trainer_password,
                )
                
                new_user.save()  # Veritabanına kaydet

                messages.success(request, 'Antrenör başarıyla oluşturuldu.')
                return render(request, "yonetici/trainer_add.html")  # Başka bir sayfaya yönlendirme
    return render(request, "yonetici/trainer_add.html")

def client_add(request):
    if request.method == 'POST':
        # HTML formundan gelen bilgileri al
        client_first_name = request.POST['inputClientFN']
        client_last_name = request.POST['inputClientLN']
        client_birthdate = request.POST['inputClientBD']
        client_gender = request.POST['inputClintGender']
        client_phone_number = request.POST['inputClientPhone']
        client_hedef = request.POST['inputClientHedef']
        client_email = request.POST['inputClientEmail']
        password = request.POST['inputClientPassword']

        matching_trainers = Trainer.objects.filter(trainer_uzmanlık=client_hedef, trainer_kont__gt=0)
        selected_trainer = None
        for trainer in matching_trainers:
            if trainer.trainer_kont > 0:
                selected_trainer = trainer
                break

        if selected_trainer:
            selected_trainer.trainer_kont -= 1
            selected_trainer.save()

            new_user = Client(
                client_first_name=client_first_name,
                client_last_name=client_last_name,
                client_birthdate=client_birthdate,
                client_hedef = client_hedef,
                client_gender=client_gender,
                client_phone_number=client_phone_number,
                client_email=client_email,
                assigned_trainer=selected_trainer,
            )

            new_user.set_password(password)  # Şifreyi ayarla
            new_user.save()  # Veritabanına kaydet

    return render(request, "yonetici/client_add.html")

def trainer_info(request):
    trainers= Trainer.objects.all()
    return render(request, "yonetici/trainer_info.html",{'trainers':trainers})

def client_info(request):
    clients= Client.objects.all()
    return render(request, "yonetici/client_info.html", {'clients':clients})

def client_detail(request, pk):

    client_details = Client.objects.get(id=pk)
    return render(request, "yonetici/client_detail.html", {"client_details":client_details})

def trainer_detail(request, pk):

    trainer_details = Trainer.objects.get(id=pk)
    return render(request, "yonetici/trainer_detail.html", {"trainer_details":trainer_details})

def delete_client(request, pk):
    delete_clnt = Client.objects.get(id=pk)
    delete_clnt.delete()
    return render(request, "yonetici/client_info.html")

def delete_trainer(request, pk):
    delete_trn = Trainer.objects.get(id=pk)
    delete_trn.delete()
    return render(request, "yonetici/trainer_info.html")

def update_client(request, pk):
    client = get_object_or_404(Client, id=pk)

    if request.method == 'POST':
        client.client_first_name = request.POST['inputClientFN']
        client.client_last_name = request.POST['inputClientLN']
        client.client_email = request.POST['inputClientEmail']
        client.client_birthdate = request.POST['inputClientBD']
        client.client_hedef = request.POST['inputClientHedef']
        client.client_gender = request.POST['inputClintGender']
        client.client_phone_number = request.POST['inputClientPhone']
        client.save() 
    return render(request, 'yonetici/update_client.html', {'client': client})

def update_trainer(request, pk):
    trainer = get_object_or_404(Trainer, id=pk)

    if request.method == 'POST':
        trainer.trainer_first_name = request.POST['inputTrainerFN']
        trainer.trainer_last_name = request.POST['inputTrainerLN']
        trainer.trainer_birthdate = request.POST['inputTrainerBD']
        trainer.trainer_gender = request.POST['inputTrainerGender']
        trainer.trainer_phone_number = request.POST['inputTrainerPhone']
        trainer.trainer_uzmanlık = request.POST['inputTrainerUzmanlik']
        trainer.trainer_experiences = request.POST['inputTrainerTecrube']
        trainer.trainer_kont = request.POST['inputTrainerKont']
        trainer.trainer_email = request.POST['inputTrainerEmail']
        trainer_password = request.POST['inputTrainerPassword']
        trainer.save()
    return render(request, 'yonetici/update_trainer.html', {'trainer': trainer})

def yonetici_logout(request):
    return render(request, "yonetici/yonetici_login.html")