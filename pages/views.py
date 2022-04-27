from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.db.models import Q
from baze.models import *
from django.utils.dateparse import parse_date
from datetime import datetime
from django.contrib import messages

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def otpremnica_list(request):
    cursor = connection.cursor()
    cursor.execute("select * from otpremnica_View")
    r = dictfetchall(cursor)
    return render(request, 'otpremnica.html', {'data': r})

def search(request):
    cursor = connection.cursor()
    cursor.execute("select * from stavkaotpremnice")
    r = dictfetchall(cursor)

    if request.method =='POST':
        try:
            brojotpremnice = request.POST.get('brojotpremnice')
            cena = request.POST.get('cena')
            cena1 = request.POST.get('cena1')
            cena2 = request.POST.get('cena2')

            if brojotpremnice and cena:
                Search.brojotpremnice = int(brojotpremnice)
                Search.cena = int(cena)
                cursor = connection.cursor()
                query = "select * from stavkaotpremnice where BROJOTPREMNICE={} AND CENA={}".format(Search.brojotpremnice, Search.cena)
                cursor.execute(query)
                r = dictfetchall(cursor)
                return render(request, 'search.html', {'data': r})

            elif cena1 and cena2:
                Search.cena1 = int(cena1)
                Search.cena2 = int(cena2)

        except Exception as ex:
            messages.error(request, ex)
            print(ex)
            return render(request, 'search.html')  
    return render(request, 'search.html', {'data': r})
      
                





def stavkafakture_list(request):

    cursor = connection.cursor()
    cursor.execute("SELECT  rednibroj, brojfakture, kolicina, cena, pdv ,napomena, sifraartikla FROM stavkafakture")
    r = dictfetchall(cursor)
    return render(request, 'stavkafakture.html', {'data': r})

def updateO(request):
    if request.method == 'POST':
        try:
            brojotpremnice = request.POST.get('brojotpremnice')
            napomena = request.POST.get('napomena')
            ukupno = request.POST.get('ukupno')
            pib = request.POST.get('pib')
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            if brojotpremnice and napomena and ukupno and pib and brojnarudzbenice:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.napomena = napomena 
                Otpremnica.ukupno = int(ukupno)
                Otpremnica.pib = int(pib)
                Otpremnica.brojnarudzbenice = int(brojnarudzbenice)
                
                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET NAPOMENA = '{}', UKUPNO = {}, PIB = {}, BROJNARUDZBENICE = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.napomena, Otpremnica.ukupno, Otpremnica.pib, Otpremnica.brojnarudzbenice, Otpremnica.brojotpremnice)
                cursor.execute(query)
                
                return render(request, 'otpremnica.html')
            elif brojotpremnice and napomena and ukupno and pib:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.napomena = naziv_artikla 
                Otpremnica.ukupno = int(ukupno)
                Otpremnica.pib = int(pib)

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET NAPOMENA = '{}', UKUPNO = {}, PIB = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.napomena, Otpremnica.ukupno, Otpremnica.pib, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
            elif brojotpremnice and napomena and ukupno:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.napomena = napomena 
                Otpremnica.ukupno = int(ukupno)

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET NAPOMENA = '{}', UKUPNO = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.napomena, Otpremnica.ukupno, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
            elif brojotpremnice and napomena:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.napomena = napomena 

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET NAPOMENA = '{}' WHERE BROJOTPREMNICE = {}".format(Otpremnica.napomena, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
            elif brojotpremnice and ukupno:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.ukupno = int(ukupno)

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_DESC SET UKUPNO = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.ukupno, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
            elif brojotpremnice and pib:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.pib = int(pib)

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET PIB = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.pib, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
            elif brojotpremnice and brojnarudzbenice:
                Otpremnica.brojotpremnice = int(brojotpremnice)
                Otpremnica.brojnarudzbenice = int(brojnarudzbenice)

                cursor = connection.cursor()
                query = "UPDATE OTPREMNICA_VIEW SET BROJNARUDZBENICE = {} WHERE BROJOTPREMNICE = {}".format(Otpremnica.pib, Otpremnica.brojotpremnice)
                cursor.execute(query)

                return render(request, 'otpremnica.html')
        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'otpremnica.html')
    else:
        return render(request, 'otpremnica.html')

def insertKupac(request):
    if request.method == 'POST':
        try:
            pib = request.POST.get('pib')
            nazivkupca = request.POST.get('nazivkupca')
            brojulice = request.POST.get('brojulice')
            nazivulice = request.POST.get('nazivulice')
            tekuciracun = request.POST.get('tekuciracun')


            Kupac.pib = int(pib)
            Kupac.nazivkupca = nazivkupca
            Kupac.brojulice = int(brojulice)
            Kupac.nazivulice = nazivulice
            Kupac.tekuciracun = tekuciracun

            cursor = connection.cursor()
            query = "INSERT INTO KUPAC(PIB, NAZIVKUPCA, ADRESA, TEKUCIRACUN) VALUES({},'{}',obj_adresa_kupca('{}', {}),{})".format(
                Kupac.pib, Kupac.nazivkupca, Kupac.nazivulice, Kupac.brojulice, Kupac.tekuciracun)
            cursor.execute(query)
            return render(request, 'kupac.html')
        except Exception as ex: 
            messages.error(request, ex)           
            print(ex)
            return render(request, 'kupac.html', extra_tags='insert')    
    else:
        return render(request, 'kupac.html')


def updateKupac(request):
    if request.method == 'POST':
        try:
            pib = request.POST.get('pib')
            nazivkupca = request.POST.get('nazivkupca')
            brojulice = request.POST.get('brojulice')
            nazivulice = request.POST.get('nazivulice')
            tekuciracun = request.POST.get('tekuciracun')

            if pib and nazivkupca:
                Kupac.pib = int(pib)
                Kupac.nazivkupca = nazivkupca
                
                cursor = connection.cursor()
                query = "UPDATE KUPAC SET NAZIVKUPCA = '{}' WHERE PIB = {}".format(Kupac.nazivkupca, Kupac.pib)
                cursor.execute(query)                
                return render(request, 'kupac.html')

            elif pib and brojulice:
                Kupac.pib = int(pib)
                Kupac.brojulice = int(brojulice)
                
                cursor = connection.cursor()
                query = "UPDATE KUPAC a SET a.adresa.broj = {} WHERE a.PIB = {}".format(Kupac.brojulice, Kupac.pib)
                cursor.execute(query)
                return render(request, 'kupac.html')
            elif pib and nazivulice:
                Kupac.pib = int(pib)
                Kupac.nazivulice = nazivulice
                
                cursor = connection.cursor()
                query = "UPDATE KUPAC a SET a.adresa.ulica = '{}' WHERE a.PIB = {}".format(Kupac.nazivulice, Kupac.pib)
                cursor.execute(query)
                return render(request, 'kupac.html')
            elif pib and tekuciracun:
                Kupac.pib = int(pib)
                Kupac.tekuciracun = int(tekuciracun)
                
                cursor = connection.cursor()
                query = "UPDATE KUPAC SET TEKUCIRACUN = {} WHERE PIB = {}".format(Kupac.tekuciracun, Kupac.pib)
                cursor.execute(query)
                return render(request, 'kupac.html')

        except Exception as ex:
            print(ex)
            messages.error(request, ex)
            return render(request, 'kupac.html', extra_tags='update')



def deleteKupac(request):
    try:
        if(request.method == 'POST'):
            pib = request.POST.get('pib')
            nazivkupca = request.POST.get('nazivkupca')
            brojulice = request.POST.get('brojulice')
            nazivulice = request.POST.get('nazivulice')
            tekuciracun = request.POST.get('tekuciracun')

            if pib:
                Kupac.pib = int(pib)

                cursor = connection.cursor()
                query = "DELETE FROM KUPAC WHERE PIB = {}".format(Kupac.pib)
                cursor.execute(query)
                return render(request, 'kupac.html')

            elif nazivulice:
                Kupac.nazivkupca = nazivkupca 

                cursor = connection.cursor()
                query = "DELETE FROM KUPAC WHERE NAZIVKUPCA = '{}'".format(Kupac.nazivkupca)
                cursor.execute(query)
                return render(request, 'kupac.html')

            elif tekuciracun:
                Kupac.tekuciracun = int(tekuciracun)

                cursor = connection.cursor()
                query = "DELETE FROM KUPAC WHERE TEKUCIRACUN = {}".format(Kupac.tekuciracun)
                cursor.execute(query)
                return render(request, 'kupac.html')
    except Exception as ex:
        print(ex)
        messages.error(request, ex)
        return render(request, 'kupac.html', extra_tags='delete')


def insertZ(request):
    if request.method == 'POST':
        try:
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            ime = request.POST.get('ime')
            prezime = request.POST.get('prezime')
            
            Zaposleni.sifrazaposlenog = int(sifrazaposlenog)
            Zaposleni.ime = ime
            Zaposleni.prezime = prezime

            cursor = connection.cursor()
            query = "INSERT INTO ZAPOSLENI(SIFRAZAPOSLENOG, IME, PREZIME) VALUES({},'{}','{}')".format(
                Zaposleni.sifrazaposlenog, Zaposleni.ime, Zaposleni.prezime)
            cursor.execute(query)
            return render(request, 'zaposleni.html')
        except Exception as ex: 
            messages.error(request, ex, extra_tags='insert')           
            print(ex)
            return render(request, 'zaposleni.html')    
    else:
        return render(request, 'zaposleni.html')


def updateZ(request):
    if request.method == 'POST':
        try:
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            ime = request.POST.get('ime')
            prezime = request.POST.get('prezime')
            if sifrazaposlenog and ime:
                Zaposleni.sifrazaposlenog = int(sifrazaposlenog)
                Zaposleni.ime = ime 
                
                
                cursor = connection.cursor()
                query = "UPDATE ZAPOSLENI SET IME = '{}' WHERE SIFRAZAPOSLENOG = {}".format(Zaposleni.ime, Zaposleni.sifrazaposlenog)
                cursor.execute(query)                
                return render(request, 'zaposleni.html')

            elif sifrazaposlenog and prezime:
                Zaposleni.sifrazaposlenog = int(sifrazaposlenog)
                Zaposleni.prezime = prezime
                
                cursor = connection.cursor()
                query = "UPDATE artikal SET PREZIME = '{}' WHERE SIFRAZAPOSLENOG = {}".format(Zaposleni.prezime, Zaposleni.sifrazaposlenog)
                cursor.execute(query)
                return render(request, 'zaposleni.html')
        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            return render(request, 'zaposleni.html')


def deleteZ(request):
    try:
        if(request.method == 'POST'):
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            ime = request.POST.get('ime')
            prezime = request.POST.get('prezime')

            if sifrazaposlenog:
                Zaposleni.sifrazaposlenog = int(sifrazaposlenog)

                cursor = connection.cursor()
                query = "DELETE FROM ZAPOSLENI WHERE SIFRAZAPOSLENOG = {}".format(Zaposleni.sifrazaposlenog)
                cursor.execute(query)
                return render(request, 'zaposleni.html')

            elif ime:
                Zaposleni.ime = ime  

                cursor = connection.cursor()
                query = "DELETE FROM ZAPOSLENI WHERE IME = '{}'".format(Zaposleni.ime)
                cursor.execute(query)
                return render(request, 'zaposleni.html')

            elif prezime:
                Zaposleni.prezime = prezime

                cursor = connection.cursor()
                query = "DELETE FROM ZAPOSLENI WHERE PREZIME = {}".format(Zaposleni.prezime)
                cursor.execute(query)
                return render(request, 'zaposleni.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'zaposleni.html')


def insertStaK(request):
    if request.method == 'POST':
        try:
            rednibroj = request.POST.get('rednibroj')
            brojkataloga = request.POST.get('brojkataloga')
            sifraartikla = request.POST.get('sifraartikla')
            dimenzija = request.POST.get('dimenzija')
            cena = request.POST.get('cena')
            pdv = request.POST.get('pdv')          
            naziv = request.POST.get('naziv')
            nazivartikla = request.POST.get('nazivartikla')

            SKataloga.rednibroj = int(rednibroj)
            SKataloga.brojkataloga = int(brojkataloga)
            SKataloga.sifraartikla = int(sifraartikla)
            SKataloga.dimenzija = int(dimenzija)
            SKataloga.cena = int(cena)
            SKataloga.pdv = int(pdv)          
            SKataloga.naziv = naziv
            SKataloga.nazivartikla = nazivartikla

            cursor = connection.cursor()
            query = "INSERT INTO STAVKAKATALOGA(REDNIBROJ, BROJKATALOGA, SIFRAARTIKLA, DIMENZIJA, CENA, PDV, NAZIV, NAZIVARTIKLA) VALUES({}, {} ,{} , {}  ,{}, {} ,'{}','{}')".format(
                SKataloga.rednibroj, SKataloga.brojkataloga, SKataloga.sifraartikla, SKataloga.dimenzija, SKataloga.cena, SKataloga.pdv, SKataloga.naziv, SKataloga.nazivartikla)
            cursor.execute(query)
            return render(request, 'stavkakataloga.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'stavkakataloga.html')    
    else:
        return render(request, 'stavkakataloga.html')


def updateStaK(request):
    if request.method == 'POST':
        rednibroj = request.POST.get('rednibroj')
        brojkataloga = request.POST.get('brojnarudzbenice')
        sifraartikla = request.POST.get('sifraartikla')
        dimenzija = request.POST.get('dimenzija')
        cena = request.POST.get('cena')
        pdv = request.POST.get('pdv')          
        naziv = request.POST.get('naziv')
        nazivartikla = request.POST.get('nazivartikla')
        try:
            if rednibroj and brojkataloga:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.brojkataloga = int(brojkataloga)

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET BROJKATALOGA ={} WHERE REDNIBROJ = {}".format(SKataloga.brojkataloga,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif rednibroj and sifraartikla:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET SIFRAARTIKLA ={} WHERE REDNIBROJ = {}".format(SKataloga.sifraartikla,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif rednibroj and dimenzija:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.dimenzija = int(dimenzija)

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET DIMENZIJA ={} WHERE REDNIBROJ = {}".format(SKataloga.dimenzija,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif rednibroj and cena:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.pdv = int(cena)

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET CENA ={} WHERE REDNIBROJ = {}".format(SKataloga.cena,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif rednibroj and pdv:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.cena = int(cena)

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET PDV ={} WHERE REDNIBROJ = {}".format(SKataloga.pdv,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif rednibroj and naziv:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.naziv = napomena

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET NAZIV ='{}' WHERE REDNIBROJ = {}".format(SKataloga.naziv,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')
            
            elif rednibroj and nazivartikla:
                SKataloga.rednibroj = int(rednibroj)
                SKataloga.nazivartikla = nazivartikla

                cursor = connection.cursor()
                query = "UPDATE STAVKAKATALOGA SET NAZIVARTIKLA ='{}' WHERE REDNIBROJ = {}".format(SKataloga.nazivartikla,SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            else:
                return render(request, 'stavkakataloga.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'stavkakataloga.html')


def deleteStaK(request):
    try:
        if(request.method == 'POST'):
            rednibroj = request.POST.get('rednibroj')
            brojkataloga = request.POST.get('brojkataloga')
            sifraartikla = request.POST.get('sifraartikla')

            if rednibroj:
                SKataloga.rednibroj = int(rednibroj)

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAKATALOGA WHERE REDNIBROJ = {}".format(SKataloga.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif brojotpremnice:
                SKataloga.brojkataloga = int(brojkataloga) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAKATALOGA WHERE BROJKATALOGA = {}".format(SKataloga.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')

            elif brojotpremnice:
                SKataloga.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAKATALOGA WHERE SIFRAARTIKLA = {}".format(SKataloga.sifraartikla)
                cursor.execute(query)
                return render(request, 'stavkakataloga.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'stavkakataloga.html')



def insertStaN(request):
    if request.method == 'POST':
        try:
            rednibroj = request.POST.get('rednibroj')
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            sifraartikla = request.POST.get('sifraartikla')
            kolicina = request.POST.get('kolicina')
            pdv = request.POST.get('pdv')
            cena = request.POST.get('cena')
            napomena = request.POST.get('napomena')
            nazivartikla = request.POST.get('nazivartikla')

            SNarudzbenice.rednibroj = int(rednibroj)
            SNarudzbenice.brojnarudzbenice = int(brojnarudzbenice)
            SNarudzbenice.sifraartikla = int(sifraartikla)
            SNarudzbenice.kolicina = int(kolicina)
            SNarudzbenice.pdv = int(pdv)
            SNarudzbenice.cena = int(cena)
            SNarudzbenice.napomena = napomena
            SNarudzbenice.nazivartikla = nazivartikla

            cursor = connection.cursor()
            query = "INSERT INTO STAVKANARUDZBENICE(REDNIBROJ, BROJNARUDZBENICE, SIFRAARTIKLA, KOLICINA, PDV, CENA, NAPOMENA, NAZIVARTIKLA) VALUES({}, {} ,{} , {}  ,{}, {} ,'{}','{}')".format(
                SNarudzbenice.rednibroj, SNarudzbenice.brojnarudzbenice, SNarudzbenice.sifraartikla, SNarudzbenice.kolicina, SNarudzbenice.pdv, SNarudzbenice.cena, SNarudzbenice.napomena, SNarudzbenice.nazivartikla)
            cursor.execute(query)
            return render(request, 'stavkanarudzbenice.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'stavkanarudzbenice.html')    
    else:
        return render(request, 'stavkanarudzbenice.html')

def updateStaN(request):
    if request.method == 'POST':
        rednibroj = request.POST.get('rednibroj')
        brojnarudzbenice = request.POST.get('brojnarudzbenice')
        sifraartikla = request.POST.get('sifraartikla')
        kolicina = request.POST.get('kolicina')
        pdv = request.POST.get('pdv')
        cena = request.POST.get('cena')
        napomena = request.POST.get('napomena')
        nazivartikla = request.POST.get('nazivartikla')
        try:
            if rednibroj and brojnarudzbenice:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.brojnarudzbenice = int(brojotpremnice)

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET BROJOTPREMNICE ={} WHERE REDNIBROJ = {}".format(SNarudzbenice.brojnarudzbenice,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif rednibroj and sifraartikla:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET SIFRAARTIKLA ={} WHERE REDNIBROJ = {}".format(SNarudzbenice.sifraartikla,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif rednibroj and kolicina:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.kolicina = int(kolicina)

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET KOLICINA ={} WHERE REDNIBROJ = {}".format(SNarudzbenice.kolicina,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif rednibroj and pdv:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.pdv = int(pdv)

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET PDV ={} WHERE REDNIBROJ = {}".format(SNarudzbenice.pdv,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif rednibroj and cena:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.cena = int(cena)

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET CENA ={} WHERE REDNIBROJ = {}".format(SNarudzbenice.cena,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif rednibroj and napomena:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.napomena = napomena

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET NAPOMENA ='{}' WHERE REDNIBROJ = {}".format(SNarudzbenice.napomena,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')
            
            elif rednibroj and nazivartikla:
                SNarudzbenice.rednibroj = int(rednibroj)
                SNarudzbenice.nazivartikla = nazivartikla

                cursor = connection.cursor()
                query = "UPDATE STAVKANARUDZBENICE SET NAZIVARTIKLA ='{}' WHERE REDNIBROJ = {}".format(SNarudzbenice.nazivartikla,SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            else:
                return render(request, 'stavkanarudzbenice.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'stavkanarudzbenice.html')

def deleteStaN(request):
    try:
        if(request.method == 'POST'):
            rednibroj = request.POST.get('rednibroj')
            brojnarudzbenice = request.POST.get('brojotpremnice')
            sifraartikla = request.POST.get('sifraartikla')

            if rednibroj:
                SNarudzbenice.rednibroj = int(rednibroj)

                cursor = connection.cursor()
                query = "DELETE FROM STAVKANARUDZBENICE WHERE REDNIBROJ = {}".format(SNarudzbenice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif brojotpremnice:
                SNarudzbenice.brojnarudzbenice = int(brojnarudzbenice) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKANARUDZBENICE WHERE BROJNARUDZBENICE = {}".format(SNarudzbenice.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')

            elif brojotpremnice:
                SNarudzbenice.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "DELETE FROM STAVKANARUDZBENICE WHERE SIFRAARTIKLA = {}".format(SNarudzbenice.sifraartikla)
                cursor.execute(query)
                return render(request, 'stavkanarudzbenice.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'stavkanarudzbenice.html')

def insertCA(request):
    if request.method == 'POST':
        try:
            idcene = request.POST.get('idcene')
            sifraartikla = request.POST.get('sifraartikla')
            datumod = request.POST.get('datumod')
            iznos = request.POST.get('iznos')
                     

            CenaArtikla.idcene = int(idcene)
            CenaArtikla.sifraartikla = int(sifraartikla)
            CenaArtikla.datumod = parse_date(datumod)
            CenaArtikla.iznos = int(iznos)
            

            cursor = connection.cursor()
            query = "INSERT INTO CENAARTIKLA(IDCENE, SIFRAARTIKLA, DATUMOD, IZNOS) VALUES({}, {} ,'{}' , {})".format(
                CenaArtikla.idcene, CenaArtikla.sifraartikla, CenaArtikla.datumod, CenaArtikla.iznos)
            cursor.execute(query)
            return render(request, 'cenaartikla.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'cenaartikla.html')    
    else:
        return render(request, 'cenaartikla.html')


def updateCA(request):
    if request.method == 'POST':
        idcene = request.POST.get('idcene')
        sifraartikla = request.POST.get('sifraartikla')
        datumod = request.POST.get('datumod')
        iznos = request.POST.get('iznos')
        try:
            if idcene and sifraartikla:
                CenaArtikla.idcene = int(idcene)
                CenaArtikla.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE CENAARTIKLA SET SIFRAARTIKLA ={} WHERE IDCENE = {}".format(CenaArtikla.sifraartikla,CenaArtikla.idcene)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            elif idcene and datumod:
                CenaArtikla.idcene = int(idcene)
                CenaArtikla.datumod = parse_date(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE CENAARTIKLA SET DATUMOD ='{}' WHERE IDCENE = {}".format(CenaArtikla.datumod,CenaArtikla.idcene)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            elif idcene and iznos:
                CenaArtikla.idcene = int(idcene)
                CenaArtikla.iznos = int(iznos)

                cursor = connection.cursor()
                query = "UPDATE CENAARTIKLA SET IZNOS ={} WHERE IDCENE = {}".format(CenaArtikla.iznos,CenaArtikla.idcene)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            else:
                return render(request, 'cenaartikla.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'cenaartikla.html')



def deleteCA(request):
    try:
        if(request.method == 'POST'):
            idcene = request.POST.get('idcene')
            sifraartikla = request.POST.get('sifraartikla')
            datumod = request.POST.get('datumod')
            iznos = request.POST.get('iznos')

            if idcene:
                CenaArtikla.idcene = int(idcene)

                cursor = connection.cursor()
                query = "DELETE FROM CENAARTIKLA WHERE IDCENE = {}".format(CenaArtikla.idcene)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            elif sifraartikla:
                CenaArtikla.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "DELETE FROM CENAARTIKLA WHERE SIFRAARTIKLA = {}".format(CenaArtikla.sifraartikla)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            elif datumod:
                CenaArtikla.datumod = parse_date(datumod)

                cursor = connection.cursor()
                query = "DELETE FROM CENAARTIKLA WHERE DATUMOD = '{}'".format(CenaArtikla.datumod)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')

            elif iznos:
                CenaArtikla.iznos = int(iznos)

                cursor = connection.cursor()
                query = "DELETE FROM CENAARTIKLA WHERE IZNOS = {}".format(CenaArtikla.iznos)
                cursor.execute(query)
                return render(request, 'cenaartikla.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'cenaartikla.html')


def insertStaF(request):
    if request.method == 'POST':
        try:
            rednibroj = request.POST.get('rednibroj')
            brojfakture = request.POST.get('brojfakture')
            kolicina = request.POST.get('kolicina')
            cena = request.POST.get('cena')
            pdv = request.POST.get('pdv')
            napomena = request.POST.get('napomena')
            sifraartikla = request.POST.get('sifraartikla')
            

            SFaktura.rednibroj = int(rednibroj)
            SFaktura.brojfakture = int(brojfakture)
            SFaktura.kolicina = int(kolicina)
            SFaktura.cena = int(cena)
            SFaktura.pdv = int(pdv)
            SFaktura.napomena = napomena
            SFaktura.sifraartikla = int(sifraartikla)
            

            cursor = connection.cursor()
            query = "INSERT INTO STAVKAFAKTURE(REDNIBROJ, BROJFAKTURE, KOLICINA, CENA, PDV, NAPOMENA, SIFRAARTIKLA) VALUES({}, {} ,KOLICINA({}) , {}  ,{} ,'{}',{})".format(
                SFaktura.rednibroj, SFaktura.brojfakture, SFaktura.kolicina, SFaktura.cena, SFaktura.pdv, SFaktura.napomena, SFaktura.sifraartikla)
            cursor.execute(query)
            return render(request, 'stavkafakture.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'stavkafakture.html')    
    else:
        return render(request, 'stavkafakture.html')



def updateStaF(request):
    if request.method == 'POST':
        rednibroj = request.POST.get('rednibroj')
        brojfakture = request.POST.get('brojfakture')
        kolicina = request.POST.get('kolicina')
        cena = request.POST.get('cena')
        pdv = request.POST.get('pdv')
        napomena = request.POST.get('napomena')
        sifraartikla = request.POST.get('sifraartikla')
        try:
            if rednibroj and brojfakture:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.brojfakture = int(brojfakture)

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET BROJFAKTURE ={} WHERE REDNIBROJ = {}".format(SFaktura.brojfakture,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif rednibroj and kolicina:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.kolicina = int(kolicina)

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET KOLICINA = KOLICINA({}) WHERE REDNIBROJ = {}".format(SFaktura.kolicina,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif rednibroj and cena:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.cena = int(cena)

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET BROJFAKTURE ={} WHERE CENA = {}".format(SFaktura.cena,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif rednibroj and dpd:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.pdv = int(pdv)

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET PDV = {} WHERE REDNIBROJ = {}".format(SFaktura.pdv,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif rednibroj and napomena:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.napomena = napomena

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET NAPOMENA ='{}' WHERE BROJFAKTURE = {}".format(SFaktura.napomena,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif rednibroj and sifraartikla:
                SFaktura.rednibroj = int(rednibroj)
                SFaktura.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE STAVKAFAKTURE SET SIFRAARTIKLA = {} WHERE BROJFAKTURE = {}".format(SFaktura.sifraartikla,SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            else:
                return render(request, 'stavkafakture.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'stavkafakture.html')


def deleteStaF(request):
    try:
        if(request.method == 'POST'):
            rednibroj = request.POST.get('rednibroj')
            brojfakture = request.POST.get('brojfakture')
            kolicina = request.POST.get('kolicina')
            sifraartikla = request.POST.get('sifraartikla')

            if rednibroj:
                SFaktura.rednibroj= int(rednibroj) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAFAKTURE WHERE REDNIBROJ = {}".format(SFaktura.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif brojfakture:
                SFaktura.brojfakture = int(brojfakture) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAFAKTURE WHERE BROJFAKTURE = {}".format(SFaktura.brojfakture)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')

            elif kolicina:
                SFaktura.kolicina = int(kolicina) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAFAKTURE WHERE KOLICINA = KOLICINA({})".format(SFaktura.kolicina)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')
            elif sifraartikla:
                SFaktura.sifraartikla = int(sifraartikla) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAFAKTURE WHERE SIFRAARTIKLA = {}".format(SFaktura.sifraartikla)
                cursor.execute(query)
                return render(request, 'stavkafakture.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'stavkafakture.html')



def insertF(request):
    if request.method == 'POST':
        try:
            brojfakture = request.POST.get('brojfakture')
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            brojotpremnice = request.POST.get('brojotpremnice')
            pib = request.POST.get('pib')
            dpd = request.POST.get('dpd')
            datumdospeca = request.POST.get('datumdospeca')
            napomena = request.POST.get('napomena')
            nazivkupca = request.POST.get('nazivkupca')
            

            Faktura.brojfakture = int(brojfakture)
            Faktura.sifrazaposlenog = int(sifrazaposlenog)
            Faktura.brojotpremnice = int(brojotpremnice)
            Faktura.pib = int(pib)
            Faktura.dpd = parse_date(dpd)
            Faktura.datumdospeca = parse_date(datumdospeca)
            Faktura.napomena = napomena
            Faktura.nazivkupca = nazivkupca
            

            cursor = connection.cursor()
            query = "INSERT INTO FAKTURA(BROJFAKTURE, SIFRAZAPOSLENOG, BROJOTPREMNICE, PIB, DPD, DATUMDOSPECA, NAPOMENA, NAZIVKUPCA) VALUES({}, {} ,{} , {}  ,'{}', '{}' ,'{}','{}')".format(
                Faktura.brojfakture, Faktura.sifrazaposlenog, Faktura.brojotpremnice, Faktura.pib, Faktura.dpd, Faktura.datumdospeca, Faktura.napomena, Faktura.nazivkupca)
            cursor.execute(query)
            return render(request, 'faktura.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'faktura.html')    
    else:
        return render(request, 'faktura.html')





def updateF(request):
    if request.method == 'POST':
        brojfakture = request.POST.get('brojfakture')
        sifrazaposlenog = request.POST.get('sifrazaposlenog')
        brojotpremnice = request.POST.get('brojotpremnice')
        pib = request.POST.get('pib')
        dpd = request.POST.get('dpd')
        datumdospeca = request.POST.get('datumdospeca')
        napomena = request.POST.get('napomena')
        nazivkupca = request.POST.get('nazivkupca')
        try:
            if brojfakture and sifrazaposlenog:
                Faktura.brojfakture = int(brojfakture)
                Faktura.sifrazaposlenog = int(sifrazaposlenog)

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET SIFRAZAPOSLENOG ={} WHERE BROJFAKTURE = {}".format(Faktura.sifrazaposlenog,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojfakture and brojotpremnice:
                Faktura.brojfakture = int(brojfakture)
                Faktura.brojotpremnice = int(brojotpremnice)

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET BROJOTPREMNICE ={} WHERE BROJFAKTURE = {}".format(Faktura.brojotpremnice,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojfakture and pib:
                Faktura.brojfakture = int(brojfakture)
                Faktura.pib = int(pib)

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET PIB ={} WHERE BROJFAKTURE = {}".format(Faktura.pib,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojfakture and dpd:
                Faktura.brojfakture = int(brojfakture)
                Faktura.dpd = parse_date(dpd)

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET DPD ='{}' WHERE BROJFAKTURE = {}".format(Faktura.dpd,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojfakture and datumdospeca:
                Faktura.brojfakture = int(brojfakture)
                Faktura.datumdospeca = parse_date(datumdospeca)

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET DATUMDOSPECA ='{}' WHERE BROJFAKTURE = {}".format(Faktura.datumdospeca,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojfakture and napomena:
                Faktura.brojfakture = int(brojfakture)
                Faktura.napomena = napomena

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET NAPOMENA ='{}' WHERE BROJFAKTURE = {}".format(Faktura.napomena,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')
            
            elif brojfakture and nazivkupca:
                Faktura.brojfakture = int(brojfakture)
                Faktura.nazivkupca = nazivkupca

                cursor = connection.cursor()
                query = "UPDATE FAKTURA SET NAZIVKUPCA ='{}' WHERE BROJFAKTURE = {}".format(Faktura.nazivkupca,Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            else:
                return render(request, 'faktura.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'faktura.html')


def deleteF(request):
    try:
        if(request.method == 'POST'):
            brojfakture = request.POST.get('brojfakture')
            brojotpremnice = request.POST.get('brojotpremnice')
            pib = request.POST.get('pib')

            if brojfakture:
                Faktura.brojfakture = int(brojfakture) 

                cursor = connection.cursor()
                query = "DELETE FROM FAKTURA WHERE BROJFAKTURE = {}".format(Faktura.brojfakture)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojotpremnice:
                Faktura.brojotpremnice = int(brojotpremnice) 

                cursor = connection.cursor()
                query = "DELETE FROM FAKTURA WHERE BROJOTPREMNICE = {}".format(Faktura.brojotpremnice)
                cursor.execute(query)
                return render(request, 'faktura.html')

            elif brojotpremnice:
                Faktura.pib = int(pib) 

                cursor = connection.cursor()
                query = "DELETE FROM FAKTURA WHERE PIB = {}".format(Faktura.pib)
                cursor.execute(query)
                return render(request, 'faktura.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'faktura.html')



def insertStaO(request):
    if request.method == 'POST':
        try:
            rednibroj = request.POST.get('rednibroj')
            brojotpremnice = request.POST.get('brojotpremnice')
            sifraartikla = request.POST.get('sifraartikla')
            kolicina = request.POST.get('kolicina')
            pdv = request.POST.get('pdv')
            cena = request.POST.get('cena')
            napomena = request.POST.get('napomena')
            nazivartikla = request.POST.get('nazivartikla')
            ukupnacena = request.POST.get('ukupnacena')

            SOtpremnice.rednibroj = int(rednibroj)
            SOtpremnice.brojotpremnice = int(brojotpremnice)
            SOtpremnice.sifraartikla = int(sifraartikla)
            SOtpremnice.kolicina = int(kolicina)
            SOtpremnice.pdv = int(pdv)
            SOtpremnice.cena = int(cena)
            SOtpremnice.napomena = napomena
            SOtpremnice.nazivartikla = nazivartikla
            SOtpremnice.ukupnacena = int(ukupnacena)

            cursor = connection.cursor()
            query = "INSERT INTO STAVKAOTPREMNICE(REDNIBROJ, BROJOTPREMNICE, SIFRAARTIKLA, KOLICINA, PDV, CENA, NAPOMENA, NAZIVARTIKLA, UKUPNACENA) VALUES({}, {} ,{} , {}  ,{}, {} ,'{}','{}', {})".format(
                SOtpremnice.rednibroj, SOtpremnice.brojotpremnice, SOtpremnice.sifraartikla, SOtpremnice.kolicina, SOtpremnice.pdv, SOtpremnice.cena, SOtpremnice.napomena, SOtpremnice.nazivartikla, SOtpremnice.ukupnacena)
            cursor.execute(query)
            return render(request, 'stavkaotpremnice.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'stavkaotpremnice.html')    
    else:
        return render(request, 'stavkaotpremnice.html')


def updateStaO(request):
    if request.method == 'POST':
        rednibroj = request.POST.get('rednibroj')
        brojotpremnice = request.POST.get('brojotpremnice')
        sifraartikla = request.POST.get('sifraartikla')
        kolicina = request.POST.get('kolicina')
        pdv = request.POST.get('pdv')
        cena = request.POST.get('cena')
        napomena = request.POST.get('napomena')
        nazivartikla = request.POST.get('nazivartikla')
        ukupnacena = request.POST.get('ukupnacena')
        try:
            if rednibroj and brojotpremnice:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.brojotpremnice = int(brojotpremnice)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET BROJOTPREMNICE ={} WHERE REDNIBROJ = {}".format(SOtpremnice.brojotpremnice,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and sifraartikla:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET SIFRAARTIKLA ={} WHERE REDNIBROJ = {}".format(SOtpremnice.sifraartikla,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and kolicina:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.kolicina = int(kolicina)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET KOLICINA ={} WHERE REDNIBROJ = {}".format(SOtpremnice.kolicina,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and pdv:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.pdv = int(pdv)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET PDV ={} WHERE REDNIBROJ = {}".format(SOtpremnice.pdv,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and cena:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.cena = int(cena)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET CENA ={} WHERE REDNIBROJ = {}".format(SOtpremnice.cena,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and napomena:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.napomena = napomena

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET NAPOMENA ='{}' WHERE REDNIBROJ = {}".format(SOtpremnice.napomena,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')
            
            elif rednibroj and nazivartikla:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.nazivartikla = nazivartikla

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET NAZIVARTIKLA ='{}' WHERE REDNIBROJ = {}".format(SOtpremnice.nazivartikla,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif rednibroj and ukupnacena:
                SOtpremnice.rednibroj = int(rednibroj)
                SOtpremnice.ukupnacena = int(ukupnacena)

                cursor = connection.cursor()
                query = "UPDATE STAVKAOTPREMNICE SET UKUPNACENA ={} WHERE REDNIBROJ = {}".format(SOtpremnice.ukupnacena,SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')
            else:
                return render(request, 'stavkaotpremnice.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'stavkaotpremnice.html')

def deleteStaO(request):
    try:
        if(request.method == 'POST'):
            rednibroj = request.POST.get('rednibroj')
            brojotpremnice = request.POST.get('brojotpremnice')
            sifraartikla = request.POST.get('sifraartikla')

            if rednibroj:
                SOtpremnice.rednibroj = int(rednibroj) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAOTPREMNICE WHERE REDNIBROJ = {}".format(SOtpremnice.rednibroj)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif brojotpremnice:
                SOtpremnice.brojotpremnice = int(brojotpremnice) 

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAOTPREMNICE WHERE BROJOTPREMNICE = {}".format(SOtpremnice.brojotpremnice)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')

            elif brojotpremnice:
                SOtpremnice.sifraartikla = int(sifraartikla)

                cursor = connection.cursor()
                query = "DELETE FROM STAVKAOTPREMNICE WHERE SIFRAARTIKLA = {}".format(SOtpremnice.sifraartikla)
                cursor.execute(query)
                return render(request, 'stavkaotpremnice.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'stavkaotpremnice.html')


def insertO(request):
    if request.method == 'POST':
        try:
            brojotpremnice = request.POST.get('brojotpremnice')
            napomena = request.POST.get('napomena')
            ukupno = request.POST.get('ukupno')
            pib = request.POST.get('pib')
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            date = request.POST.get('date')
            brojracuna = request.POST.get('brojracuna')

            Otpremnica.brojotpremnice = int(brojotpremnice)
            Otpremnica.napomena = napomena
            Otpremnica.ukupno = int(ukupno)
            Otpremnica.pib = int(pib)
            Otpremnica.sifrazaposlenog = int(sifrazaposlenog)
            Otpremnica.brojnarudzbenice = int(brojnarudzbenice)
            Otpremnica.date = parse_date(date)
            Otpremnica.brojracuna = int(brojracuna)

            print(type(Otpremnica.brojotpremnice))
            print(type(Otpremnica.napomena))
            print(type(Otpremnica.ukupno))
            print(type(Otpremnica.pib))
            print(type(Otpremnica.sifrazaposlenog))
            print(type(Otpremnica.brojnarudzbenice))
            cursor = connection.cursor()
            query = "INSERT INTO OTPREMNICA_VIEW(BROJOTPREMNICE, NAPOMENA, UKUPNO, PIB, SIFRAZAPOSLENOG, BROJNARUDZBENICE, DATUM, BROJRACUNA) VALUES({}, '{}' ,{} , {}  ,{}, {}, '{}', {})".format(
                Otpremnica.brojotpremnice, Otpremnica.napomena, Otpremnica.ukupno, Otpremnica.pib, Otpremnica.sifrazaposlenog, Otpremnica.brojnarudzbenice, Otpremnica.date, Otpremnica.brojracuna)
            cursor.execute(query)
            return render(request, 'otpremnica.html')
        except Exception as ex:            
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'otpremnica.html')
    else:
        return render(request, 'otpremnica.html')
        

def insertN(request):

    if request.method == 'POST':
        try:
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            brojkataloga = request.POST.get('brojkataloga')
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            pib = request.POST.get('pib')
            brojracuna = request.POST.get('brojracuna')
            date = request.POST.get('date')
            napomena = request.POST.get('napomena')

            Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
            Narudzbenica.brojkataloga = int(brojkataloga)
            Narudzbenica.sifrazaposlenog = int(sifrazaposlenog)
            Narudzbenica.pib = int(pib)
            Narudzbenica.brojracuna = int(brojracuna)
            Narudzbenica.date = parse_date(date)
            Narudzbenica.napomena = napomena

            cursor = connection.cursor()
            query = "INSERT INTO NARUDZBENICA(BROJNARUDZBENICE, BROJKATALOGA, SIFRAZAPOSLENOG, PIB, BROJRACUNA, DATUM, NAPOMENA) VALUES({}, {} ,{} , {}  , {}, '{}', '{}')".format(
                Narudzbenica.brojnarudzbenice, Narudzbenica.brojkataloga, Narudzbenica.sifrazaposlenog, Narudzbenica.pib, Narudzbenica.brojracuna, Narudzbenica.date, Narudzbenica.napomena)
            cursor.execute(query)
            return render(request, 'narudzbenica.html')
        except Exception as ex:           
            print(ex)
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'narudzbenica.html')
    else:
        return render(request, 'narudzbenica.html')


def deleteN(request):
    try:
        if(request.method == 'POST'):
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            brojkataloga = request.POST.get('brojkataloga')
            napomena = request.POST.get('napomena')

            if brojnarudzbenice:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)              
                cursor = connection.cursor()
                query = "DELETE FROM NARUDZBENICA WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')

            elif brojkataloga:
                Narudzbenica.brojkataloga = int(brojkataloga)
                cursor = connection.cursor()
                query = "DELETE FROM NARUDZBENICA WHERE BROJKATALOGA = {}".format(Narudzbenica.brojkataloga)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')

            elif napomena:
                Narudzbenica.napomena = napomena
                cursor = connection.cursor()
                query = "DELETE FROM ARTIKAL WHERE NAPOMENA= '{}'".format(Narudzbenica.napomena)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'narudzbenica.html')


def updateN(request):
    if request.method == 'POST':
        brojnarudzbenice = request.POST.get('brojnarudzbenice')
        brojkataloga = request.POST.get('brojkataloga')
        sifrazaposlenog = request.POST.get('sifrazaposlenog')
        pib = request.POST.get('pib')
        brojracuna = request.POST.get('brojracuna')
        date = request.POST.get('date')
        napomena = request.POST.get('napomena')
        try:
            if brojnarudzbenice and brojkataloga:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.brojkataloga = int(brojkataloga)

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET BROJKATALOGA ={} WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.brojkataloga, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
            elif brojnarudzbenice and sifrazaposlenog:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.sifrazaposlenog = int(sifrazaposlenog)

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET SIFRAZAPOSLENOG ={} WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.sifrazaposlenog, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
            elif brojnarudzbenice and pib:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.pib = int(pib)

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET PIB ={} WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.pib, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
            elif brojnarudzbenice and brojracuna:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.brojracuna = int(brojracuna)

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET BROJRACUNA ={} WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.brojracuna, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
            elif brojnarudzbenice and date:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.date = parse_date(date)

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET DATUM ='{}' WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.date, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
            elif brojnarudzbenice and napomena:
                Narudzbenica.brojnarudzbenice = int(brojnarudzbenice)
                Narudzbenica.napomena = napomena

                cursor = connection.cursor()
                query = "UPDATE NARUDZBENICA SET NAPOMENA ='{}' WHERE BROJNARUDZBENICE = {}".format(Narudzbenica.napomena, Narudzbenica.brojnarudzbenice)
                cursor.execute(query)
                return render(request, 'narudzbenica.html')
        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            print(ex)
            return render(request, 'narudzbenica.html')


def home_view(request):
    return render(request, 'home.html')

def search_view(request):
    return render(request, 'search.html')

def kupac(request):
    return render(request, 'kupac.html')

def stavkafakture(request):
    return render(request, 'stavkafakture.html')

def narudzbenica(request):
    return render(request, 'narudzbenica.html')

def stavkanarudzbenice(request):
    return render(request, 'stavkanarudzbenice.html')

def faktura(request):
    return render(request, 'faktura.html')

def katalog(request):
    return render(request, 'katalog.html')

def otpremnica_view(request):
    return render(request, 'otpremnica.html')

def stavkaotpremnice_view(request):
    return render(request, 'stavkaotpremnice.html')

def stavkakataloga_view(request):
    return render(request, 'stavkakataloga.html')

def cenaartikla(request):
    return render(request, 'cenaartikla.html')

def artikal(request):
    return render(request, 'artikal.html')

def stavkanaru_list(request):
    try:
        cursor = connection.cursor()
        cursor.execute("select * from stavkanarudzbenice")
        r = dictfetchall(cursor)
        print(r)
    except Exception as ex:
        print(ex)
    return render(request, 'stavkanarudzbenice.html', {'stav': r})

def stavkaO_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from stavkaotpremnice")
    r = dictfetchall(cursor)  

    return render(request, 'stavkaotpremnice.html', {'data': r})


def kupac_list(request):

    cursor = connection.cursor()
    cursor.execute("select pib, nazivkupca, adresa, tekuciracun from kupac")
    r = dictfetchall(cursor)


    return render(request, 'kupac.html', {'data': r})

def cenaartikla_list(request):
    cursor = connection.cursor()
    cursor.execute("select * from cenaartikla")
    r = dictfetchall(cursor)  

    return render(request, 'cenaartikla.html', {'data': r})
    
def stavkaK_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from stavkakataloga")
    r = dictfetchall(cursor)  

    return render(request, 'stavkakataloga.html', {'data': r})

def narudzbenica_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from narudzbenica")
    r = dictfetchall(cursor)  

    return render(request, 'narudzbenica.html', {'data': r})

def zaposleni_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from zaposleni")
    r = dictfetchall(cursor)  

    return render(request, 'zaposleni.html', {'data': r})


def faktura_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from faktura")
    r = dictfetchall(cursor)

    if 'partition' in request.POST:
        if 'partition1' == request.POST.get('partition'):
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM faktura PARTITION(old_fak)")
            r = dictfetchall(cursor)
            return render(request, 'faktura.html', {'data': r})

        elif'partition2' == request.POST.get('partition'):
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM faktura PARTITION(new_fak)")
            r = dictfetchall(cursor)
            return render(request, 'faktura.html', {'data': r})

        elif'all' == request.POST.get('partition'):
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM faktura")
            r = dictfetchall(cursor)
            return render(request, 'faktura.html', {'data': r})

    return render(request, 'faktura.html', {'data': r})


def katalog_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from katalog")
    r = dictfetchall(cursor)

    return render(request, 'katalog.html', {'data': r})


def artikal_list(request):

    cursor = connection.cursor()
    cursor.execute("select * from artikal")
    r = dictfetchall(cursor)
    return render(request, 'artikal.html', {'data': r})


def zaposleni(request):
    return render(request, 'zaposleni.html')


def artikal_update(request):
    if request.method == 'POST':
        try:
            sifra_artikla = request.POST.get('sifraartikla')
            naziv_artikla = request.POST.get('nazivartikla')
            aktuelna_cena = request.POST.get('aktuelnacena')
            if sifra_artikla and naziv_artikla and aktuelna_cena:
                Artikal.sifraartikla = int(sifra_artikla)
                Artikal.nazivartikla = naziv_artikla 
                Artikal.aktuelnacena = int(aktuelna_cena)
                
                cursor = connection.cursor()
                query = "UPDATE artikal SET NAZIVARTIKLA = '{}', AKTUELNACENA = {} WHERE SIFRAARTIKLA = {}".format(Artikal.nazivartikla, Artikal.aktuelnacena, Artikal.sifraartikla)
                cursor.execute(query)
                
                return render(request, 'artikal.html')
            elif sifra_artikla and naziv_artikla:
                Artikal.sifraartikla = int(sifra_artikla)
                Artikal.nazivartikla = naziv_artikla 
                cursor = connection.cursor()
                query = "UPDATE artikal SET NAZIVARTIKLA = '{}' WHERE SIFRAARTIKLA = {}".format(Artikal.nazivartikla, Artikal.sifraartikla)
                cursor.execute(query)
                return render(request, 'artikal.html')
            elif sifra_artikla and aktuelna_cena:
                Artikal.sifraartikla = int(sifra_artikla)
                Artikal.aktuelnacena = int(aktuelna_cena)
                cursor = connection.cursor()
                query = "UPDATE artikal SET AKTUELNACENA = {} WHERE SIFRAARTIKLA = {}".format(Artikal.aktuelnacena, Artikal.sifraartikla)
                cursor.execute(query)
                return render(request, 'artikal.html')
        except Exception as ex:
            messages.error(request, ex, extra_tags='update')
            return render(request, 'artikal.html')

def new(request):
    if request.method == 'POST':
        try:
            sifra_artikla = request.POST.get('sifraartikla')
            naziv_artikla = request.POST.get('nazivartikla')
            aktuelna_cena = request.POST.get('aktuelnacena')
            Artikal.sifraartikla = int(sifra_artikla)
            Artikal.nazivartikla = naziv_artikla
            Artikal.aktuelnacena = int(aktuelna_cena)

            cursor = connection.cursor()
            query = "INSERT INTO ARTIKAL VALUES({}, '{}', {})".format(Artikal.sifraartikla, Artikal.nazivartikla, Artikal.aktuelnacena)
            cursor.execute(query)
            return render(request, 'artikal.html')
        except Exception as ex:
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'artikal.html')
        
    
def dele(request):
    if(request.method == 'POST'):
        try:
            sifra_artikla = request.POST.get('sifraartikla')
            naziv_artikla = request.POST.get('nazivartikla')
            aktuelnca_cena = request.POST.get('aktuelnacena')

            if sifra_artikla and naziv_artikla:
                Artikal.sifraartikla = int(sifra_artikla)
                Artikal.nazivartikla = naziv_artikla

                cursor = connection.cursor()
                query = "DELETE FROM ARTIKAL WHERE SIFRAARTIKLA = {} AND NAZIVARTIKLA= '{}'".format(Artikal.sifraartikla, Artikal.nazivartikla)
                cursor.execute(query)
                return render(request, 'artikal.html')
            elif sifra_artikla:
                Artikal.sifraartikla = int(sifra_artikla)

                cursor = connection.cursor()
                query = "DELETE FROM ARTIKAL WHERE SIFRAARTIKLA = {}".format(Artikal.sifraartikla)
                cursor.execute(query)
                return render(request, 'artikal.html')
            elif naziv_artikla:
                Artikal.nazivartikla = naziv_artikla

                cursor = connection.cursor()
                query = "DELETE FROM ARTIKAL WHERE NAZIVARTIKLA= '{}'".format(Artikal.nazivartikla)
                cursor.execute(query)
                return render(request, 'artikal.html')

            elif naziv_artikla and aktuelnca_cena:
                Artikal.sifraartikla = int(sifra_artikla)
                Artikal.aktuelnacena = int(aktuelnca_cena)

                cursor = connection.cursor()
                query = "DELETE FROM ARTIKAL WHERE SIFRAARTIKLA = {} AND AKTUELNACENA= {}".format(Artikal.sifraartikla, Artikal.aktuelnacena)
                cursor.execute(query)
                return render(request, 'artikal.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            return render(request, 'artikal.html')


def deleteO(request):
    try:
        if(request.method == 'POST'):

            brojotpremnice = request.POST.get('brojotpremnice')
            napomena = request.POST.get('napomena')
            ukupno = request.POST.get('ukupno')
            pib = request.POST.get('pib')
            sifrazaposlenog = request.POST.get('sifrazaposlenog')
            brojnarudzbenice = request.POST.get('brojnarudzbenice')
            date = request.POST.get('date')
            brojracuna = request.POST.get('brojracuna')

            if brojotpremnice:
                    Otpremnica.brojotpremnice = int(brojotpremnice)
                    cursor = connection.cursor()
                    query = "DELETE FROM OTPREMNICA_VIEW WHERE BROJOTPREMNICE = {}".format(Otpremnica.brojotpremnice)
                    cursor.execute(query)
                    return render(request, 'otpremnica.html')

            elif napomena:

                    cursor = connection.cursor()
                    query = "DELETE FROM OTPREMOTPREMNICA_VIEWNICA WHERE NAPOMENA = '{}'".format(Otpremnica.napomena)
                    cursor.execute(query)
                    return render(request, 'otpremnica.html')

            elif ukupno:
                    cursor = connection.cursor()
                    query = "DELETE FROM OTPREMNICA_VIEW WHERE UKUPNO= {}".format(Otpremnica.ukupno)
                    cursor.execute(query)
                    return render(request, 'otpremnica.html')

            elif pib:
                    cursor = connection.cursor()
                    query = "DELETE FROM OTPREMNICA_VIEW WHERE PIB= {}".format(Otpremnica.pib)
                    cursor.execute(query)
                    return render(request, 'otpremnica.html')

            elif brojnarudzbenice:
                    cursor = connection.cursor()
                    query = "DELETE FROM OTPREMNICA_VIEW WHERE BROJNARUDZBENICE= {}".format(Otpremnica.brojnarudzbenice)
                    cursor.execute(query)
                    return render(request, 'otpremnica.html')

    except Exception as ex:
        print(ex)
        messages.error(request, ex, extra_tags='delete')
        return render(request, 'otpremnica.html')


def insertK(request):
    if request.method == 'POST':
        try:
            brojkataloga = request.POST.get('brojkataloga')
            naziv = request.POST.get('naziv')
            
            
            Katalog.brojkataloga = int(brojkataloga)
            Katalog.naziv = naziv
            

            cursor = connection.cursor()
            query = "INSERT INTO KATALOG(BROJKATALOGA, NAZIV) VALUES({},'{}')".format(
                Katalog.brojkataloga, Katalog.naziv)
            cursor.execute(query)
            return render(request, 'katalog.html')
        except Exception as ex: 
            messages.error(request, ex, extra_tags='insert')          
            print(ex)
            return render(request, 'katalog.html')    

def updateK(request):
    if request.method == 'POST':
        try:
            brojkataloga = request.POST.get('brojkataloga')
            naziv = request.POST.get('naziv')
            if brojkataloga and naziv:
                Katalog.brojkataloga = int(brojkataloga)
                Katalog.naziv = naziv 
                
                
                cursor = connection.cursor()
                query = "UPDATE KATALOG SET NAZIV = '{}' WHERE BROJKATALOGA = {}".format(Katalog.naziv, Katalog.brojkataloga)
                cursor.execute(query)                
                return render(request, 'katalog.html')

        except Exception as ex:
            messages.error(request, ex, extra_tags='insert')
            return render(request, 'katalog.html')

def deleteK(request):
    try:
        if(request.method == 'POST'):
            brojkataloga = request.POST.get('brojkataloga')
            naziv = request.POST.get('naziv')

            if brojkataloga:
                Katalog.brojkataloga = int(brojkataloga)

                cursor = connection.cursor()
                query = "DELETE FROM KATALOG WHERE BROJKATALOGA = {}".format(Katalog.brojkataloga)
                cursor.execute(query)
                return render(request, 'katalog.html')

            elif naziv:
                Katalog.naziv = naziv  

                cursor = connection.cursor()
                query = "DELETE FROM KATALOG WHERE NAZIV = '{}'".format(Katalog.naziv)
                cursor.execute(query)
                return render(request, 'katalog.html')

    except Exception as ex:
            messages.error(request, ex, extra_tags='delete')
            print(ex)
            return render(request, 'katalog.html')



