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

def fil_til_Sted():
    fil = open("steder.txt","r")
    steder_liste = []
    for i in fil:
        i = i.strip()
        i = i.split(";")
        steder.append(Sted(i[0],i[1],i[2],i[3],i[4]))
    fil.close()
    return steder
