from Domain.Rezervari import get_all
from Logic.CRUD import *
from Logic.CLASA_SUPERIOARA import Upgrade


def show_menu():
    print('1.Adauga,sterge sau modifica o rezervare. ')
    print('2.Trecerea unei rezervari la o clasa superioara.')
    print('3.Ieftinierea rezervarilor cu un anumit procent pentru rezervarile care au check-in-ul facut.')
    print('4.Determina pretul maxim pentru fiecare clasa.')
    print('5.Ordoneaza rezervarilor descrescator dupa pret.')
    print('6.Afiseaza suma preturilor pentru fiecare pasager in parte.')
    print('7.Undo')
    print('8.Exit')
def adaugare (rezervari):
    id_rezervare=int(input('Dati id-ul rezervarii:'))
    nume_rezervare = input('Dati numele celui care a facut rezervarea:')
    clasa_rezervare = input('Dati clasa rezervarii:')
    pret_rezervare = int(input('Dati pretul biletului:'))
    checkin_rezervare = input('A fost facut checkin-ul ?:')
    return create(rezervari, id_rezervare,nume_rezervare,clasa_rezervare,pret_rezervare,checkin_rezervare)
def afisare(rezervari):
    for rezervare in rezervari:
        print(get_all(rezervare))

def CRUD_MENU(rezervari):
    while True:
        print('1.Adauga o rezervare.')
        print('2.Modifica o rezervare.')
        print('3.Sterge o rezervare.')
        print('4.Revii la lista anterioara de functionalitati.')
        print('a.Afiseaza lista de rezervari.')
        optiune = input('Alege optiunea:')
        if optiune== '1':
            rezervari=adaugare(rezervari)
        elif optiune=='a':
            afisare(rezervari)
        elif optiune=='4':
            break
    return rezervari




def run_ui(rezervari):
    show_menu()
    optiune = input('Alege optiunea: ')
    if optiune=='1':
        rezervari= CRUD_MENU(rezervari)
    if optiune=='2':


    if optiune=='8':
        break
    return rezervari