import pickle
import time

#TODO
#Miksi merkinnät "tallentuu" ilman tallentamista? Päätyykö ihan tiedostoon saakka?
#Monissa valinnoissa paljon samankaltaisuutta, tee alifunktiota?


# Avattavan tiedoston oletusnimi
nimi = "muistio.dat"


def avaaTiedosto(nimi):
    
    # Yritetään lukea tiedostoa
    # Jollei sitä ole, asetetaan ohjelman muistissa oleva muistiinpano-taulukko tyhjäksi
    try:
        with open(nimi, "rb") as tiedosto:
            sisalto = pickle.load(tiedosto)
    except IOError:
        print("Virhe tiedostossa, luodaan uusi:", nimi + ".")
        with open(nimi,"wb") as tiedosto:
                sisalto = []
    except EOFError:
        #Luetussa tiedostossa ei ole sisältöä lisättäväksi taulukkoon
        sisalto = []


ohjelmaKaynnissa = True

avaaTiedosto(nimi)

print("_______ MUISTIKIRJASOVELLUS _______")

while ohjelmaKaynnissa:

    print(f"""
Käytössä muistikirjana {nimi}.

(1) Näytä merkinnät
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tyhjennä muistikirja
(6) Vaihda muistikirja
(7) Tallenna
(8) Lopeta
""")


    #Kysytään käyttäjältä int-tyyppistä lukua väliltä 1-8
    #Muut syötteet eivät kelpaa
    
    try:
        valinta = int(input("Valitse (kokonaisluku väliltä 1-8): "))
        print()
        if valinta > 8 or valinta < 1:
            raise ValueError("Valinta ei ole väliltä 1-8.")
    except ValueError:
        print("Virheellinen syöte.")
    except Exception:
        print("Tapahtui virhe.")

    

    if valinta == 1: #Lue muistikirjaa
        
        for i in sisalto:
            print(i)
            
    
    elif valinta == 2: #Lisää merkintä
        
        with open(nimi, "wb") as tiedosto:

            # Esimerkkimerkintä (03/27/24 14:34:20) 
            lisays = input("Kirjoita uusi merkintä: ")
            lisays = lisays + " (" + time.strftime("%x %X") + ")"

            #Lisätään listaan uusi merkintä
            sisalto.append(lisays)
    

    elif valinta == 3: #Muokkaa merkintää
        
        maara = len(sisalto)
        print("Listalla on", maara, "merkintää.")

        for i in range(maara):
            print(f"{i + 1}) " + sisalto[i])

        print()
        muokattavan_indeksi = int(input("Valitse merkintä, jota haluat muokata (väliltä 1-"+ str(maara) + ").")) - 1

        if muokattavan_indeksi < 0 or muokattavan_indeksi > maara - 1:
                print("Virheellinen indeksi. Valitse indeksi väliltä 1-"+ str(maara) + ".")
        else:
            print("Muokattava merkintä:", sisalto[muokattavan_indeksi])
            muokattu_teksti = input("Anna uusi teksti: ")
            sisalto[muokattavan_indeksi] = muokattu_teksti + " (" + time.strftime("%x %X") + ")"

    
    elif valinta == 4: #Poista merkintä
        
        maara = len(sisalto)
        print("Listalla on", maara, "merkintää.")
        
        for i in range(maara):
            print(f"{i + 1}) " + sisalto[i])

        print()
        poistettavan_indeksi = int(input("Valitse merkintä, jonka haluat poistaa (väliltä 1-"+ str(maara) + ").")) - 1

        if poistettavan_indeksi < 0 or poistettavan_indeksi > maara - 1:
                print("Virheellinen indeksi. Valitse indeksi väliltä 1-"+ str(maara) + ".")
        else:
            poistettu = sisalto.pop(poistettavan_indeksi)
            print("\nPoistettiin merkintä:\n" + poistettu)


    elif valinta == 5: #Tyhjennä muistikirja

        pass


    elif valinta == 6: #Vaihda muistikirja

        while True:

            print("Haluatko tallentaa viimeisimmät muutokset tiedostoon", nimi, "ennen muistikirjan vaihtamista?")
            print("1) Kyllä \n2) Ei")    
            tallennus = int(input("Valitse 1 tai 2."))
            print()
        
            if tallennus == 1:
                
                #Tee tähän tallennus, with open ja pickle dump, tee mahdollisesti tallennusfunktio?
                break
            elif tallennus == 2:
                print("Oletko varma, että haluat vaihtaa muistikirjan tallentamatta ensin?")
                print("1) Kyllä \n2) Ei")
                varmennus = int(input("Valitse 1 tai 2."))
                print()
                if varmennus == 1:
                    break
                elif varmennus == 2:
                    pass
                else:
                    print("Syötäthän luvun 1 tai 2.")
            else:
                print("Syötäthän luvun 1 tai 2.")
                
        print("Tämänhetkinen muistikirja on tiedostossa nimeltä", nimi +". Mihin tiedostoon haluat vaihtaa?")
        nimi = str(input("Syötä tiedoston nimi:"))

    
    
    elif valinta == 7: #Tallenna
        
        with open(nimi, "wb") as tiedosto:
            pickle.dump(sisalto, tiedosto)

        print("Muistikirja tallennettu.")


    elif valinta == 8: #Tallenna ja lopeta

        print("Ohjelma lopetetaan.")
        
        ohjelmaKaynnissa = False

    else:
        print("Miten sä tänne päädyit?")
    
