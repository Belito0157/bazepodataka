"""bazepodataka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from pages.views import artikal_list
from pages.views import new
from pages.views import dele
from pages.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home_view, name='home'),
    path('', kupac, name='kupac'),
    path('', narudzbenica, name='narudzbenica'),
    path('', artikal, name='artikal'),
    path('', otpremnica_view, name='otpremnica'),
    path('', zaposleni, name="zaposleni"),
    path('', katalog, name="katalog"),
    path('', faktura, name="faktura"),
    path('', stavkanarudzbenice, name="stavkanarudzbenice"),
    path('', stavkaotpremnice_view, name="stavkaotpremnice"),
    path('', stavkakataloga_view, name="stavkakataloga"),
    path('', cenaartikla, name="cenaartikla"),
    path('', stavkafakture, name="stavkafakture"),
    path('', search_view, name="search"),

    
    path('artikal_update/', artikal_update),
    path('otpremnica/', otpremnica_list, name='otpremnica'),  
    path('insertO/', insertO), 
    path('updateO/', updateO), 

    path('updateN/', updateN, name='narudzbenica'),
    path('deleteN/', deleteN, name='narudzbenica'),
    path('narudzbenica/', narudzbenica_list, name='narudzbenica'),

    path('zaposleni/', zaposleni_list, name='zaposleni'),

    path('faktura/', faktura_list, name='faktura'),

    
    path('kupac/', kupac_list, name='kupac'),


    path('cenaartikla/', cenaartikla_list, name='cenaartikla'),
    path('deleteO/', deleteO),
    path('stavkaotpremnice/', stavkaO_list, name='stavkaotpremnice'),
    path('stavkakataloga/', stavkaK_list, name='stavkakataloga'),
    path('katalog/', katalog_list, name='katalog'),
    path('insertN/', insertN), 
    path('stavkanarudzbenice/', stavkanaru_list, name='stavkanarudzbenice'),
    path('new/', new),
    path('dele/', dele),
    path('artikal/', artikal_list, name='artikal'),
    path('stavkafakture/', stavkafakture_list, name='stavkafakture'),

    path('insertK/', insertK),
    path('updateK/', updateK),
    path('deleteK/', deleteK),

    path('insertStaO/', insertStaO),
    path('updateStaO/', updateStaO),
    path('deleteStaO/', deleteStaO),

    path('insertF/', insertF),
    path('updateF/', updateF),
    path('deleteF/', deleteF),

    path('insertStaF/', insertStaF),
    path('updateStaF/', updateStaF),
    path('deleteStaF/', deleteStaF),

    path('insertCA/', insertCA),
    path('updateCA/', updateCA),
    path('deleteCA/', deleteCA),
    

    path('insertStaN/', insertStaN),
    path('updateStaN/', updateStaN),
    path('deleteStaN/', deleteStaN),

    path('insertStaK/', insertStaK),
    path('updateStaK/', updateStaK),
    path('deleteStaK/', deleteStaK),

    path('insertZ/', insertZ),
    path('updateZ/', updateZ),
    path('deleteZ/', deleteZ),

    path('insertKupac/', insertKupac),
    path('updateKupac/', updateKupac),
    path('deleteKupac/', deleteKupac),

    path('search/', search, name="search"),
 
    
    
    
    
    
    
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
