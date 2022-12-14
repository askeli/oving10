# (                                       (    (        )   (                   )             )   (    (                                  
# )\ )    (       *   )    )     )    )   )\ ) )\ )  ( /(   )\ )             ( /(   *   )  ( /(   )\ ) )\ )  (        (                   
#(()/(    )\    ` )  /( ( /(  ( /( ( /(  (()/((()/(  )\()) (()/(   (   (     )\())` )  /(  )\()) (()/((()/(  )\ )     )\     (   (   (    
# /(_))((((_)(   ( )(_)))\()) )(_)))\())  /(_))/(_))((_)\   /(_))  )\  )\  |((_)\  ( )(_))((_)\   /(_))/(_))(()/(  ((((_)(   )\  )\  )\   
#(_))_  )\ _ )\ (_(_())((_)\ ((_) ((_)\  (_)) (_))    ((_) (_))   ((_)((_) |_ ((_)(_(_())   ((_) (_)) (_))   /(_))_ )\ _ )\ ((_)((_)((_)  
# |   \ (_)_\(_)|_   _| / (_)|_  )/  (_) | _ \| _ \  / _ \ / __| _ | || __|| |/ / |_   _|  / _ \ | _ \| _ \ (_)) __|(_)_\(_)\ \ / / | __| 
# | |) | / _ \    | |   | |   / /| () |  |  _/|   / | (_) |\__ \| || || _|   ' <    | |   | (_) ||  _/|  _/   | (_ | / _ \   \ V /  | _|  
# |___/ /_/ \_\   |_|   |_|  /___|\__/   |_|  |_|_\  \___/ |___/ \__/ |___| _|\_\   |_|    \___/ |_|  |_|      \___|/_/ \_\   \_/   |___| 
#
# 
#                                                                                                                                          
#
from datetime import datetime
import pandas as pd
import csv
import tkinter
from tkinter import filedialog
import os
import webbrowser
import time

dict_liste = dict()  
liste=[]

avtale_liste=[]
sted_liste=[]
kategori_liste=[]



#Klasse for ny avtale 
class Avtale():
    def __init__(self, init_tittel = "", init_sted = "", init_starttidspunkt = datetime.now(), init_varighet = 0, init_kategori ="" ):
        self.tittel = init_tittel
        self.sted = init_sted
        self.starttidspunkt = init_starttidspunkt
        self.varighet = init_varighet
        self.kategori = init_kategori

#Avtale streng __str__
    def __str__(self):
        return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori}"

#Klasse for kategori 
class Kategori():
    def __init__(self, start_id = "", start_navn = "", start_prioritet = 1):
        self.id = start_id
        self.navn = start_navn
        self.prioritet = start_prioritet
        

#Kategori streng __str__
    def __str__(self):
        return f"{self.id}, {self.navn}, {self.prioritet}"
  


#Stedsklasse
class Sted():
    def __init__(self,init_id = "" ,init_navn = "",init_gateadresse = None,init_poststed = None,init_postnummer = None):
        self.id = init_id
        self.navn = init_navn
        self.gateadresse = init_gateadresse
        self.poststed = init_poststed
        self.postnummer = init_postnummer
    def __str__(self):
        liste = [self.id,self.navn,self.gateadresse,self.poststed,self.postnummer]
        ny_liste = []
    
        for i in liste:
             if i != None:
                ny_liste.append(i)
        return f"{ny_liste}"

#Christoffer
#Unntaksh??ndtering
class GatenavnError(Exception):
    pass
class StedsnavnError(Exception):
    pass     



#Christoffer
#filterfunksjon for liste
def liste_filter(avtale_liste):
    gyldige_kolonner = ["tittel", "sted", "starttidspunkt", "varighet", "kategori"]
    gyldige_kolonner_print = ["1. Tittel", "2. Sted", "3. Starttidspunkt", "4. Varighet", "5. Kategori"]
    print("Hvilken kolonne ??nsker du ?? lete i?")
    print('\n'.join(gyldige_kolonner_print))
    while True:
        try:
            kolonne = int(input('Skriv inn valg [1-6]: '))
            if kolonne < 1 or kolonne > 5:
                raise ValueError
        except ValueError:
            print('Velg en gyldig kategori')
        else:
            lete_streng = str(input('Hva leter du etter?: '))
            data_frame = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])
            for i in avtale_liste:
                df = pd.DataFrame([[i.tittel, i.sted, str(i.starttidspunkt), i.varighet, i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
                data_frame = data_frame.append([df], ignore_index=True)
            return print("S??keresultat som inneholder '%s': \n"%(lete_streng),data_frame[data_frame['%s'%(gyldige_kolonner[kolonne-1])].str.contains(lete_streng)])

#Christoffer
#Denne funksjonen tar inn *stedsnavn, *gatenavn og *postnummer. Poststed og kommunenummer (id) er hentet fra et xlsx ark lastet ned fra bring.no
postnummer_register_df = pd.read_excel('ressursfiler\Postnummerregister-Excel.xlsx', sheet_name=0)

def nytt_sted():
    global sted_liste
    print('\033[1m','\nLegge til nytt sted\n','\033[0m')
    while True:
        try:
            stedsnavn = input('Skriv inn stedsnavn:\n> ')
            gatenavn = input('Skriv inn gatenavn:\n> ')
            postnummer = int(input('Skriv inn postnummer:\n> '))
            poststed = postnummer_register_df[(postnummer_register_df['Postnummer'] == postnummer)]['Poststed'].item()
            kommunenummer = postnummer_register_df[(postnummer_register_df['Postnummer'] == postnummer)]['Kommunenummer'].item()
            if stedsnavn.isalpha() is not True:
                raise StedsnavnError
            elif gatenavn.isalpha() is not True:
                raise GatenavnError
        except StedsnavnError:
            print('Vennligst skriv inn et gyldig stedsnavn. ')
        except GatenavnError:
            print('Vennligst skriv inn et gyldig gatenavn. ')
        except ValueError:
            print('Vennligst skriv inn et gyldig postnummer. ')
        else:
            break
    sted_liste.append(Sted(kommunenummer, stedsnavn, gatenavn, poststed, postnummer))
    return Sted(kommunenummer, stedsnavn, gatenavn, poststed, postnummer)


#Christoffer
#Denne funksjonen gir et avtale-objekt ny kategori
#Listene er laget lokalt, siden skriv_ut_alle funksjonen ikke tillater utskrift fra individ. lister.
def ny_kategori_til_avtale():
    print('...\nLegge til ny kategori til avtale\n...\n')
    #Avtale liste kopi
    liste1 = avtale_liste
    df_liste_avtale = pd.DataFrame(columns = ['tittel','sted','starttidspunkt','varighet','kategori'])  
    for i in liste1:
        df1 = pd.DataFrame([[i.tittel,i.sted,str(i.starttidspunkt),i.varighet,i.kategori]], columns=('tittel','sted','starttidspunkt','varighet','kategori'))
        df_liste_avtale = df_liste_avtale.append([df1], ignore_index=True)

    #Kategori liste kopi
    liste2 = kategori_liste
    df_liste_kategori = pd.DataFrame(columns = ['ID','navn','prioritet'])  
    for i in liste2:
        df2 = pd.DataFrame([[i.id,i.navn,i.prioritet]], columns=(['ID','navn','prioritet']))
        df_liste_kategori = df_liste_kategori.append([df2], ignore_index=True) 

    try:
        print(df_liste_avtale)
        avtale_indeks = (int(input('Hvilken avtale ??nsker du ?? endre?\n> ')))
        print(df_liste_kategori)
        kategori_indeks = (int(input('Hvilken kategori ??nsker du ?? endre?\n> ')))
    except ValueError:
        print('Skriv inn en gyldig indeksverdi')
    else:
        ny_kategori = kategori_liste[kategori_indeks]
        avtale_liste[avtale_indeks].kategori = Avtale(kategori=ny_kategori)

#Progressbar
def progress_bar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '???', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()



        
def avtaler_fra_fil():
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    filnavn = filedialog.askopenfilename()
    global dict_liste
    #dict_liste.clear() # slett den eksisterende listen
    with open(filnavn, 'r') as csv_file:
        reader = csv.reader(csv_file,delimiter=';')
        dict_liste = dict(reader)
    print ("Lest f??lgende avtaler fra fil: ")
    for i in (dict_liste):
        print(i," - ",dict_liste[i])
    input("For ?? g?? tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)


def avtaler_til_fil():
    print("Du har valgt: 2: Skriv avtalene til fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil g?? tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        with open('avtaler.csv', 'a',newline='') as csv_file: # appender csv filen, endre til w hvis den skal overskrives
            writer = csv.writer(csv_file,delimiter =";")
            for key, value in dict_liste.items():
                writer.writerow([key,value])
            print ("Skrevet f??lgende avtaler til fil: ")
            for i in (dict_liste):
                print(i," - ",dict_liste[i])
    input("For ?? g?? tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)
    
## fil_til_Sted funksjon
def fil_til_sted():
    print("Du har valgt: xx: Skriv steder til fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil g?? tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        a_file = open("steder.csv", "r")
        lines = a_file.readlines()
        for line in lines:
            print(line)
    input("For ?? g?? tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)


def sted_til_fil():
    global sted_liste
    print("Du har valgt: xx: Skriv steder til fil")
    fortsette_tilbake = input("Hvis du vil fortsette, trykk ENTER, hvis du vil g?? tilbake, tast 0")
    if fortsette_tilbake == "0":
        hovedmeny(1)
    else:
        pass
        with open('steder.csv', 'a',newline='') as csv_file: # appender csv filen, endre til w hvis den skal overskrives
            writer = csv.writer(csv_file, delimiter='\n')
            writer.writerow(sted_liste)
    input("For ?? g?? tilbake til hovedmenyen, trykk ENTER")
    hovedmeny(1)



def ny_avtale_til_meny():       
    bekreftet = "" 
    while bekreftet != "Ja":
        tittel = input("Ny avtale\nOppgi tittel:")
        for (i, item) in enumerate(sted_liste, start=0):
            print(i, item)
        sted = sted_liste[int(input("Oppgi sted:"))]
        print("Oppgi tidpunkt(????????-MM-DD TT:MM:SS):")
        starttidspunkt = ""

        while starttidspunkt == "":
            try:
                starttidspunkt = datetime(int(input("????????:")),int(input("MM:")),int(input("DD:")),int(input("TT:")),int(input("MM:")))                
                if starttidspunkt < datetime.now():
                    print("Dato utg??tt! Vennligst oppgi p?? nytt.")
                    starttidspunkt = ""
            except ValueError:
                print("Ikke en gyldig dato!")

        varighet = input("Oppgi varighet:")
        while varighet != type(int):
            try:
                varighet = int(varighet)
                break
            except ValueError:
                print("Ikke et gyldig tall!")
                varighet = input("Oppgi varighet:")

        kategori = input("Oppgi kategori:")


        print("Bekreft ", Avtale(tittel,sted, starttidspunkt, varighet, kategori))
        bekreftet = input("Ja/Nei:").casefold()        
        if "ja" in bekreftet:

            dict_liste[tittel]=Avtale(tittel,sted, starttidspunkt, varighet, kategori)
            avtale_liste.append(Avtale(tittel,sted, starttidspunkt, varighet, kategori))

            return(Avtale(tittel,sted, starttidspunkt, varighet, kategori))
            break
        else:
            print("Skriv avtalen p?? nytt.")
            continue    
            
    input("For ?? g?? tilbake til hovedmenyen, trykk ENTER")#han som har lagd den my flytte denne p?? riktig plass, finner ikke ut av det
  
    
#Funksjon for ?? lage en ny kategori 
def legg_til_kategori():
    bruker_id = input("Skriv inn id: ") 
    navn = input("Skriv inn navn: ")
    prioritet = ""
    while prioritet == "":
        prioritet = input("Skriv inn prioritet(1-2-3): ")
        try:
            prioritet = int(prioritet)
            if prioritet < 1 or prioritet > 3:
                prioritet = ""
                raise ValueError                
        except ValueError:
            prioritet = ""
            print("Ikke et gyldig tall")

    print("Bekreft kategori: ", Kategori(bruker_id, navn, prioritet))
    bekreftet = input("Ja/Nei:").casefold()  
    if "ja" in bekreftet:
        print("Kategori lagret")
        kategori_liste.append(Kategori(bruker_id, navn, prioritet))            
        return (Kategori(bruker_id, navn, prioritet))
    else:
        print("Kategori ikke lagret")
        

#Funksjon for ?? lagre kategori liste til fil
def lagre_kategorifil():
    print("Du har valgt: 10: Lagre kategorifil")
    fortsette_tilbake = input("For ?? fortsette, tast 1, hvis du ??nsker ?? g?? tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == "0":
        hovedmeny()
    else:
        pass
        global kategori_liste
        filnavn = input("hva vil du kalle filen?")
        fil = open(filnavn+".txt", "w", encoding ="UTF8")
        df_liste = pd.DataFrame(columns = ['ID','navn','prioritet'])
        for i in kategori_liste:
            df = pd.DataFrame([[i.id,i.navn,i.prioritet]], columns=('ID','navn','prioritet'))
            df_liste = df_liste.append([df], ignore_index=True)
        fil.write(str(df_liste))
        fil.close()

    

#Funksjon for ?? ??pne kategori liste fra fil
def ??pne_kategori():
    print("Du har valgt: 11: ??pne kategorifil")
    fortsette_tilbake = input("For ?? fortsette, tast 1, hvis du ??nsker ?? g?? tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == "0":
        hovedmeny()
    else:
        pass    
        filnavn = input("Hvilken fil vil du ??pne?")
        try:
            fil = open(filnavn+".txt", "r", encoding ="UTF8")
            webbrowser.open(filnavn+".txt")
            for i in fil:
                print(i)
            fil.close()    
        except FileNotFoundError:
            print("filen finnes ikke")  
    

#Funksjon for ?? skrive ut lister
def skriv_ut_alle():
    pass
    global kategori_liste
    global avtale_liste
    global sted_liste

    print("Skriv ut liste:")
    print("1: Kategori")
    print("2: Avtale")
    print("3: Sted")
    valg = int(input("\n> "))
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
 
    
def slette_avtale():
    print("Du har valgt: 5: Slette en avtale")
    fortsette_tilbake = input("For ?? fortsette, trykk ENTER, hvis du ??nsker ?? g?? tilbake til hovedmenyen, tast 0 :")
    if fortsette_tilbake == 1:
        hovedmeny(1)
    else:
        pass
    global avtale_liste
    for i in range(len(avtale_liste)):
        print(i,avtale_liste[i].tittel," - ",avtale_liste[i].__str__())
    indeks = int(input("Hvilken avtale vil du slette: "))
    del avtale_liste[indeks]
    input("Avtale slettet, trykk ENTER for ?? g?? tilbake til hovedmenyen")

    hovedmeny(1)
def filoperasjoner():
    print("\nHva ??nsker du ?? endre?")
    valg = int(input('\n1: Skriv avtale til fil\n2: Les avtale fra fil\n3: Kategori til fil\n4: Kategori fra fil\n5: Sted til fil\n6: Sted fra fil\n0: Avslutt\n\n> '))
    if valg == 1:
        avtaler_til_fil()
    elif valg == 2:
        avtaler_fra_fil()
    elif valg == 3:
        lagre_kategorifil()
    elif valg == 4:
        ??pne_kategori()
    elif valg == 5:
        sted_til_fil()
    elif valg ==6:
        fil_til_sted()
    else:
        hovedmeny(1)
    
def redigere_avtale():

    while True:
        print("\nHva ??nsker du ?? endre?")
        try:
            valg = int(input('\n1: Endre avtale\n2: Legge kategori til avtale\n3: Legge sted til avtale\n0: Avslutt\n\n> '))
            if valg == 1:
                pass
            elif valg == 2:
                ny_kategori_til_avtale()
            elif valg == 3:
                print(nytt_sted())
            elif valg > 3 or valg < 0:
                raise ValueError
            elif valg == 0:
                hovedmeny(1)
        except ValueError:
            print('Skriv inn et gyldig valg')
        else:
            break

    global liste

    for i in range(len(liste)):
        print(i,liste[i].tittel," - ",liste[i].__str__())
    indeks = int(input("Hvilken avtale vil du redigere?"))
    ny = ny_avtale()
    #if hva == 1:
        #ny = input("Hva vil du redigere til: ")
        #liste[int(indeks)].tittel
    
    liste[indeks] = ny
    
    input("Avtale redigert, trykk ENTER for ?? g?? tilbake til hovedmenyen")
    hovedmeny(1)

def hovedmeny(start):
    #os.system('cls')                 
    while start == 1:
        print('\n',85*'-','\nDAT 120 ??ving 10 [November 2022]\nUiS\nForfattere: Henry Eikeland, Hermann Tveit, Torbj??rn Bekkevoll, Christoffer Enoksen\n',85*'-','\n')
        print('1: Skriv inn ny avtale')
        print('2: Skriv ut alle avtaler')
        print('3: S??ke i avtaler')
        print('4: Endre en avtale')
            #4.1 Rediger avtale redigere_avtale()
            #4.2 Legge kategori til avtale ny_kategori_til_avtale()
            #4.3 Legge sted til avtale (NY FUNKSJON, EKSISTERER IKKE)
        print('5: Slette en avtale')
        print('6: Filoperasjoner')
        print('7: Legg til kategori')
        print('8: Legg til sted')
        items_progress_bar = list(range(0, 57))#Liste til progress_bar

        try:
            valg=int(input("\nSkriv inn ??nsket handling [1-8]:\n> "))
            if valg == 1:
                ny_avtale_til_meny()
            elif valg == 2:
                for item in progress_bar(items_progress_bar, prefix = 'Laster:', suffix = 'Ferdig', length = 50):
                    time.sleep(0.01)
                skriv_ut_alle()
            elif valg == 3:
                liste_filter(avtale_liste)
            elif valg == 4:
                redigere_avtale()
            elif valg == 5:
                slette_avtale()
            elif valg == 6:
                filoperasjoner()
            elif valg == 7:
                legg_til_kategori()
            elif valg == 8:
                print(nytt_sted())
            else:
                print("Ugyldig svar, vennligst bruk 1-8")
                input("")
        except ValueError:
            print("Ugyldig svar, vennligst bruk 1-8")
            input("")            
hovedmeny(1)