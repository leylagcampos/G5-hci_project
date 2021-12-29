from django.urls import path
from . import views
from .views import autosuggest
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("patient_list/", views.patient_list, name="patient_list"),
    path("patient/<str:pk>", views.patient, name="patient"),
    path("autosuggest/", views.autosuggest, name="autosuggest"),
    path("autodoctor/", views.autodoctor, name="autodoctor"),
    path("bed_list/", views.bed_list, name="bed_list"),
    #path("consulta/", views.consulta, name="consulta"),
    path("delete_patient/<str:pk>", views.delete_patient, name="delete_patient"),
    path("doctor_list/", views.doctor_list, name="doctor_list"),
    path("enfm_list/", views.enfm_list, name="enfm_list"),

]
