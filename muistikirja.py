import pickle
import time


# EI TARVITSE AINA TALLENTAA TIETOJA
# VAIN LOPETTAESSA OHJELMA


# Avattavan tiedoston oletusnimi
nimi = "muistio.dat"

# Yritetään lukea aikaisemmin luotua tiedostoa
# Jollei sitä ole, asetetaan ohjelman muistissa oleva muistiinpano-taulukko tyhjäksi
try:
    with open(nimi, "rb") as tiedosto:
        sisalto = pickle.load(tiedosto)
except IOError:
    print("Virhe tiedostossa, luodaan uusi:", nimi + ".")
    with open(nimi,"wb") as tiedosto:
            sisalto = []
except EOFError:
    #Luotetussa tiedostossa ei ole sisältöä lisättäväksi taulukkoon
    sisalto = []


ohjelmaKaynnissa = True

while ohjelmaKaynnissa:

    print("""
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta""")


    #Kysytään käyttäjältä int-tyyppistä lukua väliltä 1-5
    #Muut syötteet eivät kelpaa
    
    try:
        valinta = int(input("Valitse (kokonaisluku väliltä 1-5): "))
        if valinta > 5 or valinta < 1:
            raise ValueError("Valinta ei ole väliltä 1-5.")
    except ValueError:
        print("Virheellinen syöte.")
    except Exception:
        print("Tapahtui virhe.")


    if valinta == 1: #Lue muistikirjaa
        
        #with open(nimi, "rb") as tiedosto:
            #sisalto = pickle.load(tiedosto)

        print()
        for i in sisalto:
            print(i)
            

    elif valinta == 2: #Lisää merkintä
        
        with open(nimi, "wb") as tiedosto:
            
            lisays = input("Kirjoita uusi merkintä: ")
            lisays = lisays + " (" + time.strftime("%x %X") + ")"

            #Lisätään listaan uusi merkintä
            sisalto.append(lisays)

            #"Dumpataan" muokattu lista käsittelyssä olevaan tiedostoon
            #pickle.dump(sisalto, tiedosto)
            

    elif valinta == 3: #Muokkaa merkintää
        
        with open(nimi, "rb") as tiedosto:
            sisalto = pickle.load(tiedosto)
        
        maara = len(sisalto)
        print("Listalla on", maara, "merkintää.")
        muokattavan_indeksi = int(input("Valitse merkintä, jota haluat muokata (väliltä 1-"+ str(maara) + ").")) - 1

        if muokattavan_indeksi < 0 or muokattavan_indeksi > maara - 1:
                print("Virheellinen indeksi. Valitse indeksi väliltä 1-"+ str(maara) + ".")
        else:
            print(sisalto[muokattavan_indeksi])
            muokattu_teksti = input("Anna uusi teksti: ")
            sisalto[muokattavan_indeksi] = muokattu_teksti + " (" + time.strftime("%x %X") + ")"
        
            #with open(nimi, "wb") as tiedosto:
                #pickle.dump(sisalto, tiedosto)

    
    elif valinta == 4: #Poista merkintä

        with open (nimi, "rb") as tiedosto:
            sisalto = pickle.load(tiedosto)
        
        maara = len(sisalto)
        print("Listalla on", maara, "merkintää.")
        poistettavan_indeksi = int(input("Valitse merkintä, jonka haluat poistaa (väliltä 1-"+ str(maara) + ").")) - 1

        if poistettavan_indeksi < 0 or poistettavan_indeksi > maara - 1:
                print("Virheellinen indeksi. Valitse indeksi väliltä 1-"+ str(maara) + ".")
        else:
            poistettu = sisalto.pop(poistettavan_indeksi)
            print("Poistettiin merkintä:\n" + poistettu)

            #with open (nimi, "wb") as tiedosto:
                #pickle.dump(sisalto, tiedosto)        

    
    elif valinta == 5: #Tallenna ja lopeta
        
        print("Lopetetaan.")
        
        with open(nimi, "wb") as tiedosto:
            pickle.dump(sisalto, tiedosto)
        
        ohjelmaKaynnissa = False

    else:
        print("Miten sä tänne päädyit?")
