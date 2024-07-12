from django.shortcuts import render, redirect
from django.http.response import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from django.contrib import messages
from firebase_admin import auth
from django.contrib.auth import authenticate
from .auth_manager import AuthMenager
import pyrebase
from client.models import Client
from client.forms import ClientRegistrationForm
from django.contrib.auth import authenticate, login
from trainer.models import Trainer



def login_request(request):
    if request.method == 'POST':
        client_email = request.POST['emailLogin']
        password = request.POST['passLogin']
        
        user = authenticate(request, client_email=client_email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Kullanıcı başarıyla oluşturuldu ve giriş yapıldı.')
            return render(request,"client/profile.html", {'user': user})  # Başka bir sayfaya yönlendirme
        else:
            messages.error(request, 'Giriş yapılırken bir hata oluştu.')
            return render(request,"account/login.html")
    return render(request,"account/login.html")

def signup_request(request):

    if request.method == 'POST':
        # HTML formundan gelen bilgileri al
        client_first_name = request.POST['first_name']
        client_last_name = request.POST['last_name']
        client_birthdate = request.POST['birth_date']
        client_gender = request.POST['gender']
        client_phone_number = request.POST['phone_number']
        client_email = request.POST['email']
        client_hedef = request.POST['hedef']
        password = request.POST['password']
        # Antrenör - Danışan Eşleştirme
        matching_trainers = Trainer.objects.filter(trainer_uzmanlık=client_hedef, trainer_kont__gt=0)
        selected_trainer = None
        for trainer in matching_trainers:
            if trainer.trainer_kont > 0:
                selected_trainer = trainer
                break

        if selected_trainer:
            selected_trainer.trainer_kont -= 1
            selected_trainer.save()

            new_user = Client.objects.create(
                client_first_name=client_first_name,
                client_last_name=client_last_name,
                client_birthdate=client_birthdate,
                client_hedef=client_hedef,
                client_gender=client_gender,
                client_phone_number=client_phone_number,
                client_email=client_email,
                assigned_trainer=selected_trainer
            )

            
            new_user.set_password(password)  # Şifreyi ayarla
            new_user.save()  # Veritabanına kaydet

            messages.success(request, 'Kullanıcı başarıyla oluşturuldu.')
            return render(request, "account/login.html")  # Başka bir sayfaya yönlendirme
        
    return render(request, 'account/register.html')    

def forgotpass_request(request):
    
    return render(request, "account/forgotpass.html")

def profil(request):
    if request.method == 'POST':
        client_email = request.POST['emailLogin']
        password = request.POST['passLogin']
        
        user = authenticate(request, client_email=client_email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Kullanıcı başarıyla oluşturuldu ve giriş yapıldı.')
            return render(request,"client/profile.html", {'user': user})  # Başka bir sayfaya yönlendirme
        else:
            messages.error(request, 'Giriş yapılırken bir hata oluştu.')
            return render(request,"account/login.html")
    return render(request, "account/login.html") 