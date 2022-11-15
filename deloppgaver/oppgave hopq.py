#                                                       
#   (       )                 )      (     (                
#   )\   ( /(  (   (       ( /(      )\ )  )\ )    (   (    
# (((_)  )\()) )(  )\  (   )\()) (  (()/( (()/(   ))\  )(   
# )\___ ((_)\ (()\((_) )\ (_))/  )\  /(_)) /(_)) /((_)(()\  
#((/ __|| |(_) ((_)(_)((_)| |_  ((_)(_) _|(_) _|(_))   ((_) 
# | (__ | ' \ | '_|| |(_-<|  _|/ _ \ |  _| |  _|/ -_) | '_| 
#  \___||_||_||_|  |_|/__/ \__|\___/ |_|   |_|  \___| |_|   
                                                           
#   h
#   Lag en funksjon som leser inn et nytt sted til systemet.
#   Funksjonen skal bruke input-setninger til å spørre brukeren om id, 
#   navn og adresse. Funksjonen skal returnere et Sted-objekt for stedet.
import pandas as pd

class GatenavnError(Exception):
    pass
class EtternavnError(Exception):
    pass
"""
## START TORBJØRN ( KUN FOR TESTING )

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

## SLUTT TORBJØRN

#Christoffer
#Denne funksjonen tar inn *etternavn, *gatenavn og *postnummer. Poststed og kommunenummer (id) er hentet fra et xlsx ark lastet ned fra bring.no
postnummer_register_df = pd.read_excel('ressursfiler\Postnummerregister-Excel.xlsx', sheet_name=0)

def nytt_sted():
    print('\033[1m','\nLegge til nytt sted\n','\033[0m')
    while True:
        try:
            etternavn = input('Skriv inn etternavn:\n> ')
            gatenavn = input('Skriv inn gatenavn:\n> ')
            postnummer = int(input('Skriv inn postnummer:\n> '))
            poststed = postnummer_register_df[(postnummer_register_df['Postnummer'] == postnummer)]['Poststed'].item()
            kommunenummer = postnummer_register_df[(postnummer_register_df['Postnummer'] == postnummer)]['Kommunenummer'].item()
            if etternavn.isalpha() is not True:
                raise EtternavnError
            elif gatenavn.isalpha() is not True:
                raise GatenavnError
        except EtternavnError:
            print('Vennligst skriv inn et gyldig etternavn. ')
        except GatenavnError:
            print('Vennligst skriv inn et gyldig gatenavn. ')
        except ValueError:
            print('Vennligst skriv inn et gyldig postnummer. ')
        else:
            break
    return Sted(kommunenummer, etternavn, gatenavn, poststed, postnummer)

#o
#   Lag et nytt menyvalg i menysystemet for å legge en kategori til en avtale. Funksjonen skal 
#   skrive ut kategori-lista og la brukeren velge hvilken kategori ved å oppgi indeksen til 
#   kategorien i lista.
indexfortest = input('Skriv inn index til avtalen som skal endres: ')
indexfortest = (indexfortest-1)



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
        avtale_indeks = (int(input('Hvilken avtale ønsker du å endre?\n> ')))
        print(df_liste_kategori)
        kategori_indeks = (int(input('Hvilken kategori ønsker du å endre?\n> ')))
    except ValueError:
        print('Skriv inn en gyldig indeksverdi')
    else:
        ny_kategori = kategori_liste[kategori_indeks]
        avtale_liste[avtale_indeks].kategori = Avtale(kategori=ny_kategori)
  

#p
#   Lag et menyvalg for å finne alle avtaler som foregår på et bestemt sted. Skriv ut lista over 
#   steder. Gå gjennom alle avtalene og sjekk stedet den foregår på. Skriv ut avtalen hvis den 
#   foregår på det angitte stedet.


#q

#Klasse for kategori 
class Kategori():
    def __init__(self, start_id = "", start_navn = "", start_prioritet = 1):
        self.id = start_id
        self.navn = start_navn
        self.prioritet = start_prioritet

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
        return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori.id}, {self.kategori.navn}, {self.kategori.prioritet}"
"""
#Progressbar

def progress_bar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
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

import time

# Liste til progress_bar
items_progress_bar = list(range(0, 57))

# Progress bar
for item in progress_bar(items_progress_bar, prefix = 'Progress:', suffix = 'Complete', length = 50):
    # Do stuff...
    time.sleep(0.01)




else:
    try:
        valg = int(input('Ønsker du å\n1: Legge til\n2: Overskrive\n> '))
    except ValueError:
        print('Skriv inn en gyldig verdi')
    if valg == 1:
        #Gjør någe
    elif valg == 2:
        #Gjør någe aent
    elif valg > 0 and valg < 0:
        raise ValueError

     

    

#OPPGAVE OOOOO

for i in range(0, len(kategori_liste)):
    indeks = indeks + 1

def __str__(self):
    return f"{self.tittel}, {self.sted}, {self.starttidspunkt}, {self.varighet} min, {self.kategori[i].id}"
