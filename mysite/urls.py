"""PersonalWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name='home'),
    path('', views.index, name='home'),
    path('florina/', views.index2),
    path('portofolio/', views.portofolio, name='portofolio'),
    path('contact/', views.contact, name='contact'),
    path('home_virginia/', views.index3, name='home_virginia'),
    path('scratch/', views.scratch, name='scratch'),
    path('linia-traditionala/', views.liniaTraditionala, name='liniaTraditionala'),
    path('linia-traditionala1/', views.liniaTraditionala1, name='liniaTraditionala1'),
    path('about/', views.about, name='about'),

]
