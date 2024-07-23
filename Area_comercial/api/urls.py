from django.contrib import admin
from django.urls import path
from . import views
from . import getdata
from django.contrib.auth import views as auth_views
from Area_comercial.api.cargararchivo import Cargararchivo
from Area_comercial.api.contar import Contarestados
from Area_comercial.api.getdata import Save,Update
urlpatterns = [
    path('login/', views.login ),
    path('register/', views.register ),
    path('contact/', Save.as_view()),
    path('update/<int:id>', Update.as_view()),
    # path('update_estado/<int:id>', getdata.Hablitar),
    # path('get_informe/', getdata.informe_list),
    path('cargar-archivos/', Cargararchivo),
    path('contar/', Contarestados.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]



