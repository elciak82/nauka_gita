def wypisz_samochod(samochod, pojemnosc_silnika):
    print ("{0} {1}" .format(samochod, pojemnosc_silnika))

def czy_samochod(pojemnosc_silnika):
    MAX = 2.5
    if pojemnosc_silnika > MAX:
        return False
    else:
        return True

imie = 'Ewelina'
nazwisko = 'W'
#komentarz
pelne_imie = imie + ' ' + nazwisko
print (pelne_imie)

ilosc_zwierzat_domowych = 2
cena = 2 + 100
print (cena)

if __name__ == "__main_imie__":
    imie = "Ewelina"
    nazwisko = "Walczak"
    print ("{0} {1}" .format(imie, nazwisko))

if __name__ == "__main_wiek__":
    imie = "Ewelina"
    wiek = 28.5
    print ("{0} {1}" .format(imie, wiek))
    if wiek > 63:
        print ("Nie emeryt")
    else:
        print ("Do pracy rodacy")

if __name__ == "__main__":
    samochod = "Opel"
    pojemnosc_silnika = 1.5
    wypisz_samochod(samochod, pojemnosc_silnika)
    #print ("{0} {1}" .format(samochod, pojemnosc_silnika))
    if czy_samochod(pojemnosc_silnika):
    #<= 2.4:
        print ("ekonomiczny")
    else:
        print ("niekekonomiczny")
