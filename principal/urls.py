from django.contrib import admin
from django.urls import path
from principal import views as view_principal

urlpatterns = [
    path('', view_principal.Index.as_view(), name='Index'),
]
