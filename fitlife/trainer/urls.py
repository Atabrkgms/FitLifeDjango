from django.urls import path
from . import views

urlpatterns = [
    path("login", views.trainer_login, name = "trainer_login"),
    path("profil_info/<int:pk>", views.profil_info, name ="profil_info"),
    path("trainer_guncelle/<int:pk>", views.trainer_guncelle, name = "trainer_guncelle"),
    path("danisan_info/<int:pk>", views.danisan_info, name = "danisan_info"),
    path("danisan_detail/<int:pk>", views.danisan_detail, name = "danisan_detail"),
    path("beslenme_plani/<int:pk>", views.beslenme_plani, name="beslenme_plani"),
    path("beslenme_hazirla/<int:pk>", views.beslenme_hazirla, name="beslenme_hazirla"),
    path("beslenme_guncelle/<int:pk>", views.beslenme_guncelle, name = "beslenme_guncelle"),
    path("beslenme_sil/<int:pk>", views.beslenme_sil, name = "beslenme_sil"),
    path("egzersiz_plani/<int:pk>", views.egzersiz_plani, name='egzersiz_plani'),
    path("egzersiz_hazirla/<int:pk>", views.egzersiz_hazirla, name='egzersiz_hazirla'),
    path("trainer_egzersiz_detail/<int:pk>", views.trainer_egzersiz_detail, name='trainer_egzersiz_detail'),
    path("egzersiz_guncelle/<int:pk>", views.egzersiz_guncelle, name='egzersiz_guncelle'),
    path("egzersiz_sil/<int:pk>", views.egzersiz_sil, name='egzersiz_sil'),
    path("trainer_logout", views.trainer_logout, name="trainer_logout"),
]