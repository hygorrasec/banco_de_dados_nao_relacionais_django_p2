from django.contrib import admin
from django.urls import path, include
from autenticacao import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
    path('chat/', views.chat, name='chat'),
]
