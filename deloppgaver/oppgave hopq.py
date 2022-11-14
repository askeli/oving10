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

#Denne funksjonen tar inn *etternavn, *gatenavn og *postnummer. Poststed og kommunenummer (id) er hentet fra et xlsx ark lastet ned fra bring.no
postnummer_register_df = pd.read_excel('ressursfiler\Postnummerregister-Excel.xlsx', sheet_name=0)

def nytt_sted():
    while True:
        try:
            etternavn = input('Skriv inn etternavn: ')
            gatenavn = input('Skriv inn gatenavn: ')
            postnummer = int(input('Skriv inn postnummer: '))
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

print(nytt_sted())


#o
#   Lag et nytt menyvalg i menysystemet for å legge en kategori til en avtale. Funksjonen skal 
#   skrive ut kategori-lista og la brukeren velge hvilken kategori ved å oppgi indeksen til 
#   kategorien i lista.
indexfortest = input('Skriv inn index til avtalen som skal endres: ')
indexfortest = (indexfortest-1)



def ny_kategori_til_avtale():
    
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
        gammel_tittel = df_liste_avtale.iloc[avtale_indeks]['tittel']
        gammel_sted = df_liste_avtale.iloc[avtale_indeks]['sted']
        gammel_starttidspunkt = df_liste_avtale.iloc[avtale_indeks]['starttidspunkt']
        gammel_varighet = df_liste_avtale.iloc[avtale_indeks]['varighet']
        ny_kategori = kategori_liste[kategori_indeks]
        avtale_liste[avtale_indeks] = Avtale(gammel_tittel, gammel_sted, gammel_starttidspunkt, gammel_varighet, ny_kategori)
    

#p
#   Lag et menyvalg for å finne alle avtaler som foregår på et bestemt sted. Skriv ut lista over 
#   steder. Gå gjennom alle avtalene og sjekk stedet den foregår på. Skriv ut avtalen hvis den 
#   foregår på det angitte stedet.
