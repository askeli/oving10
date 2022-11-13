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




#p
#   Lag et menyvalg for å finne alle avtaler som foregår på et bestemt sted. Skriv ut lista over 
#   steder. Gå gjennom alle avtalene og sjekk stedet den foregår på. Skriv ut avtalen hvis den 
#   foregår på det angitte stedet.
