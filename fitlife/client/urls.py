from django.urls import path
from . import views

urlpatterns = [
    path("profil/<int:pk>",views.profil, name="profil"),
    path("danisan_guncelle/<int:pk>", views.danisan_guncelle, name= "danisan_guncelle"),
    path("ilerleme_kayit/<int:pk>", views.ilerleme_kayit, name="ilerleme_kayit"),
    path("ilerleme_ekle/<int:pk>", views.ilerleme_ekle, name="ilerleme_ekle"),
    path("ilerleme_detail/<int:pk>", views.ilerleme_detail, name="ilerleme_detail"),
    path("beslenme_planlari/<int:pk>", views.beslenme_planlari, name ='beslenme_planlari'),
    path("egzersiz_planlari/<int:pk>", views.egzersiz_planlari, name = "egzersiz_planlari"),
    path("egzersiz_detail/<int:pk>", views.egzersiz_detail, name = "egzersiz_detail"),
    path("gorsel_kayit/<int:pk>", views.gorsel_kayit, name ='gorsel_kayit'),
    path("logout", views.logout, name="logout"),
]