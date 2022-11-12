# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:24:50 2022

@author: Henry
"""



import pandas as pd
import webbrowser



#Klasse for kategori 
class Kategori():
    def __init__(self, start_id = "", start_navn = "", start_prioritet = 1):
        self.id = start_id
        self.navn = start_navn
        self.prioritet = start_prioritet
        

#Kategori streng __str__
    def __str__(self):
        return f"{self.id}, {self.navn}, {self.prioritet}"
        



avtale_liste=[]
sted_liste=[]
kategori_liste=[]



#Funksjon for å lage en ny kategori 
def ny_kategori():
    bruker_id = input("skriv inn id: ") 
    navn = input("skriv inn navn: ")
    prioritet = ""
    while prioritet == "":
        prioritet = input("skriv inn prioritet(1-2-3): ")
        try:
            prioritet = int(prioritet)
            if prioritet < 1 or prioritet > 3:
                prioritet = ""
                raise ValueError                
        except ValueError:
            prioritet = ""
            print("ikke et gyldig tall")
    
    print("Bekreft kategori: ", Kategori(bruker_id, navn, prioritet))
    bekreftet = input("Ja/Nei:").casefold()  
    if "ja" in bekreftet:
        print("kategori lagret")
        kategori_liste.append(Kategori(bruker_id, navn, prioritet))            
        return (Kategori(bruker_id, navn, prioritet))
    else:
        print("kategori ikke lagret")
        


#Funksjon for å lagre kategori liste til fil
def lagre_kategorifil(liste):
    filnavn = input("hva vil du kalle filen?")
    fil = open(filnavn+".txt", "w", encoding ="UTF8")
    df_liste = pd.DataFrame(columns = ['ID','navn','prioritet'])
    for i in liste:
        df = pd.DataFrame([[i.id,i.navn,i.prioritet]], columns=('ID','navn','prioritet'))
        df_liste = df_liste.append([df], ignore_index=True)
    fil.write(str(df_liste))
    fil.close()

    

#Funksjon for å åpne kategori liste fra fil
def åpne_kategori():
    filnavn = input("Hvilken fil vil du åpne?")
    try:
        fil = open(filnavn+".txt", "r", encoding ="UTF8")
        webbrowser.open(filnavn+".txt")
        for i in fil:
            print(i)
        fil.close()    
    except FileNotFoundError:
        print("filen finnes ikke")       
        


#Funksjon for å skrive ut lister
def skriv_ut_alle():
    global kategori_liste
    global avtale_liste
    global sted_liste
    
    print("print ut liste:")
    print("1: kategori")
    print("2: avtale")
    print("3: sted")
    valg = int(input("valg = "))
    #kategori liste
    if valg == 1:
        liste = kategori_liste
        df_liste = pd.DataFrame(columns = ['ID','navn','prioritet'])  
        for i in liste:
            df = pd.DataFrame([[i.id,i.navn,i.prioritet]], columns=(['ID','navn','prioritet']))
            df_liste = df_liste.append([df], ignore_index=True) 
        print("Utskrift kategori")
        print(df_liste) 
    
    #avtale liste
    elif valg == 2: 
        liste = avtale_liste
        df_liste = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])  
        for i in liste:
            df = pd.DataFrame([[i.tittel,i.sted,str(i.starttidspunkt),i.varighet,i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
            df_liste = df_liste.append([df], ignore_index=True)
        print("Utskrift Avtaler")
        print(df_liste)
        
    #sted liste    
    elif valg == 3:
        liste = sted_liste
        df_liste = pd.DataFrame(columns = ['id','navn','gateadresse','poststed','postnummer'])  
        for i in liste:
            df = pd.DataFrame([[i.id, i.navn, i.gateadresse,i.poststed,i.postnummer]], columns=('id','navn','gateadresse','poststed','postnummer'))
            df_liste = df_liste.append([df], ignore_index=True)
        print("Utskrift sted")
        print(df_liste)
    else:
        print("ikke et definert valg")










