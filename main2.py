def wypisz_samochod(samochod, pojemnosc_silnika):
    print ("{0} {1}" .format(samochod, pojemnosc_silnika))

def czy_samochod(pojemnosc_silnika):
    MAX = 2.5
    if pojemnosc_silnika < MAX:
        return False
    else:
        return True

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
