from django.contrib import admin
from django.urls import path
from . import views
from . import ofertas
from django.contrib.auth import views as auth_views
from Area_comercial.api.cargararchivo import Cargararchivo
from Area_comercial.api.contar import Contarestados, ContarestadoMes, FiltrarTipificacion
from Area_comercial.api.ofertas import Showofertas,Update_ofertas
from Area_comercial.api.notas import  *
from Area_comercial.api.empresas import *
from Area_comercial.api.Descargar import Exportecomercial
from .procesos import get_notas_comercial
urlpatterns = [
    path('login/', views.login ),
    path('logout/',views.logout),
    path('register/', views.register ),
    path('ofertas/', Showofertas.as_view()),
    path('ofertas/<int:id>', Update_ofertas.as_view()),
    path('notas/', noterequest.as_view()),
    path('notas/<int:id>', Update_notas.as_view()),
    path('contact/', empresa_request.as_view()),
    path('contact/<int:id>', Update_empresa.as_view()),
    path('descargar/', Exportecomercial.as_view()),
    path('cargar-archivos/', Cargararchivo),
    path('contar/', Contarestados.as_view()),
    path('contar_mes/', ContarestadoMes.as_view()),
    path('filtrar/', FiltrarTipificacion.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('notas_get/',get_notas_comercial)
]



