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

postnummer_register_df = pd.read_excel('ressursfiler\Postnummerregister-Excel.xlsx', sheet_name=0)

def nytt_sted():
    while True:
        try:
            #kommunenummer = input('Skriv inn steds-id: ')
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
            print(kommunenummer, etternavn, gatenavn, postnummer, poststed)
            break
    return 

 


nytt_sted()

