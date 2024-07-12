from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from client.models import Client , IlerlemeKaydi, BeslenmePlani, EgzersizPlani
import plotly.express as px




def profil(request, pk):
    client = Client.objects.get(id=pk)
    return render(request, "client/profile.html", {'client':client})

def danisan_guncelle(request, pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.client_first_name = request.POST['inputClientFN']
        client.client_last_name = request.POST['inputClientLN']
        client.client_email = request.POST['inputClientEmail']
        client.client_birthdate = request.POST['inputClientBD']
        client.client_gender = request.POST['inputClintGender']
        client.client_phone_number = request.POST['inputClientPhone']
        client.save() 
        return render(request, "client/profile.html",{'client':client})
    return render(request, "client/danisan_guncelle.html", {'client':client})

def ilerleme_kayit(request, pk):
    client = Client.objects.get(id=pk)
    ilerleme_kayitlari = client.ilerleme_kayitlari.all()
    context = {'client': client, 'ilerleme_kayitlari': ilerleme_kayitlari}
    return render(request, "client/ilerleme_kayit.html",context)

def ilerleme_ekle(request, pk):
    
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        # POST verilerini al
        boy = request.POST['inputBoy']
        kilo = request.POST['inputKilo']
        yag_orani = request.POST['inputYagOrani']
        kas_kutlesi = request.POST['inputKasKutlesi']
        vucut_kitle_endeksi = request.POST['inputVKE']
        
        # İlerlemeKaydi modelini kullanarak veritabanına kaydet
        ilerleme_kaydi = IlerlemeKaydi.objects.create(
            assigned_client=client,
            boy=boy,
            kilo=kilo,
            yag_orani=yag_orani,
            kas_kutlesi=kas_kutlesi,
            vucut_kitle_endeksi=vucut_kitle_endeksi
        )
        return render(request, "client/ilerleme_kayit.html",{'client':client} )
    return render(request, "client/ilerleme_ekle.html",{'client':client} )

def ilerleme_detail(request, pk):
    ilerleme_kayit = IlerlemeKaydi.objects.get(id=pk)
    client_id = ilerleme_kayit.assigned_client.id
    client = Client.objects.get(id = client_id)
    context = {'client': client, 'ilerleme_kayit': ilerleme_kayit}
    return render(request, "client/ilerleme_detail.html",context)

def beslenme_planlari(request, pk):
    client= Client.objects.get(id=pk)
    beslenme_plani = BeslenmePlani.objects.filter(beslenme_alan_client=client.id)
    context = {'client':client, 'beslenme_plani':beslenme_plani}
    return render(request, "client/beslenme_planlari.html", context)

def egzersiz_planlari(request, pk):
    client = Client.objects.get(id=pk)
    egzersiz_plani = EgzersizPlani.objects.filter(egzersiz_alan_client=client.id)
    context = {'client':client , 'egzersiz_plani':egzersiz_plani}
    return render(request, "client/egzersiz_planlari.html", {'client':client , 'egzersiz_plani':egzersiz_plani})

def egzersiz_detail(request, pk):
    egzersiz_plani = EgzersizPlani.objects.get(id=pk)
    client = egzersiz_plani.egzersiz_alan_client
    print(egzersiz_plani)
    return render(request, "client/egzersiz_detail.html", {'client':client, 'egzersiz_plani':egzersiz_plani})

def gorsel_kayit(request, pk):
    client = Client.objects.get(id=pk)
    data = client.ilerleme_kayitlari.all()

    fig = px.bar(
        x = [ c.tarih for c in data],
        y = [ c.kilo for c in data],
        labels = {'x':'Tarih', 'y':'boy'}
    )

    chart = fig.to_html()
    context = {'client':client , 'chart': chart}
    return render(request, "client/gorsel_kayit.html", context)

def logout(request):
    return render(request, "account/login.html")