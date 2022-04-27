from django.db import models


class Kupac(models.Model):
    pib = models.IntegerField(primary_key=True)
    nazivkupca = models.CharField(max_length=25)
    brojulice = models.IntegerField()
    nazivulice = models.CharField(max_length=25)
    tekuciracun = models.IntegerField()

class Artikal(models.Model):
    sifraartikla = models.IntegerField(primary_key=True)
    nazivartikla = models.CharField(max_length=25)
    aktuelnacena = models.IntegerField()

class Otpremnica(models.Model):
    brojotpremnice = models.IntegerField(primary_key=True)
    napomena = models.CharField(max_length=25)
    ukupno = models.IntegerField()
    pib = models.IntegerField()
    sifrazaposlenog = models.IntegerField()
    brojnarudzbenice = models.IntegerField()
    date = models.DateField(auto_now=False)
    brojracuna = models.IntegerField()

class SOtpremnice(models.Model):
    rednibroj = models.IntegerField(primary_key=True)
    brojotpremnice = models.IntegerField()
    sifraartikla = models.IntegerField()
    kolicina = models.IntegerField()
    pdv = models.IntegerField()
    cena = models.IntegerField()
    napomena = models.CharField(max_length=25)
    nazivartikla = models.CharField(max_length=25)
    ukupnacena = models.IntegerField()

class Search(models.Model):
    brojotpremnice = models.IntegerField()
    cena = models.IntegerField()
    cena1 = models.IntegerField()
    cena2 = models.IntegerField()
    
    
class Narudzbenica(models.Model):
    brojnarudzbenice = models.IntegerField(primary_key=True)
    brojkataloga = models.IntegerField()
    sifrazaposlenog = models.IntegerField()
    pib = models.IntegerField()
    brojracuna = models.IntegerField()
    date = models.DateField(auto_now=False)
    napomena = models.CharField(max_length=25)


class SNarudzbenice(models.Model):
    rednibroj = models.IntegerField(primary_key=True)
    brojnarudzbenice = models.IntegerField()
    sifraartikla = models.IntegerField()
    kolicina = models.IntegerField()
    pdv = models.IntegerField()
    cena = models.IntegerField()
    napomena = models.CharField(max_length=25)
    nazivartikla = models.CharField(max_length=25)

class Zaposleni(models.Model):
    sifrazaposlenog = models.IntegerField(primary_key=True)
    ime = models.CharField(max_length=25)
    prezime = models.CharField(max_length=25)

class Katalog(models.Model):
    brojkataloga = models.IntegerField(primary_key=True)
    naziv = models.CharField(max_length=25)

class SKataloga(models.Model):
    rednibroj = models.IntegerField(primary_key=True)
    brojkataloga = models.IntegerField()
    sifraartikla = models.IntegerField()
    dimenzija = models.IntegerField()
    cena = models.IntegerField()
    pdv = models.IntegerField()
    naziv = models.CharField(max_length=25)
    naziartikla = models.CharField(max_length=25)

class Faktura(models.Model):
    brojfakture = models.IntegerField(primary_key=True)
    sifrazaposlenog = models.IntegerField() 
    brojotpremnice = models.IntegerField()
    pib = models.IntegerField()
    dpd = models.DateField(auto_now=False)
    datumdospeca = models.DateField(auto_now=False)
    napomena = models.CharField(max_length=25)
    nazivkupca = models.CharField(max_length=25)

class SFaktura(models.Model):
    rednibroj = models.IntegerField(primary_key=True)
    brojfakture = models.IntegerField() 
    kolicina = models.IntegerField() 
    cena = models.IntegerField() 
    pdv = models.IntegerField() 
    napomena = models.CharField(max_length=25)
    sifraartikla = models.IntegerField()

class CenaArtikla(models.Model):
    idcene = models.IntegerField(primary_key=True)
    sifraartikla = models.IntegerField() 
    datumod = models.DateField(auto_now=False)
    iznos = models.IntegerField() 
