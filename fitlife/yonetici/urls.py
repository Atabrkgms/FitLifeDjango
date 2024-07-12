from django.urls import path
from . import views

urlpatterns = [
    path("login" , views.yonetici_login, name = "yonetici_login"),
    path("trainer_info", views.trainer_info, name ="trainer_info"),
    path("client_info", views.client_info, name ="client_info"),
    path("trainer_add", views.trainer_add,name = "trainer_add"),
    path("client_add", views.client_add, name = "client_add"),
    path("client_detail/<int:pk>", views.client_detail, name = "client_detail"),
    path("trainer_detail/<int:pk>", views.trainer_detail, name = "trainer_detail"),
    path("delete_client/<int:pk>", views.delete_client, name= "delete_client"),
    path("delete_trainer/<int:pk>", views.delete_trainer, name= "delete_trainer"),
    path("update_client/<int:pk>", views.update_client, name= "update_client"),
    path("update_trainer/<int:pk>", views.update_trainer, name="update_trainer"),
    path("yonetici_logout", views.yonetici_logout, name ="yonetici_logout"),
]