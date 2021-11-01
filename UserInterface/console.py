from Domain.Rezervari import get_all
from Logic.CRUD import *
from Logic.CLASA_SUPERIOARA import Upgrade
from Logic.ieftinire import *


def show_menu():
    """
        Meniul afisat initial
    """
    print('1.Adauga,sterge sau modifica o rezervare. ')
    print('2.Trecerea unei rezervari la o clasa superioara.')
    print('3.Ieftinierea rezervarilor cu un anumit procent pentru rezervarile care au check-in-ul facut.')
    print('4.Determina pretul maxim pentru fiecare clasa.')
    print('5.Ordoneaza rezervarilor descrescator dupa pret.')
    print('6.Afiseaza suma preturilor pentru fiecare pasager in parte.')
    print('7.Undo')
    print('8.Exit')
    print('a.Afiseaza lista')


def adaugare(rezervari):
    """
    adauga in lista o rezervare noua
    :param rezervari: lista cu rezervarile actuale
    :return: lista cu rezervarea adaugata
    """
    try:
        id_rezervare = int(input('Dati id-ul rezervarii:'))
        nume_rezervare = input('Dati numele celui care a facut rezervarea:')
        clasa_rezervare = input('Dati clasa rezervarii:')
        pret_rezervare = int(input('Dati pretul biletului:'))
        checkin_rezervare = input('A fost facut checkin-ul ?:')
        if clasa_rezervare not in ['economy', 'economy plus', 'business']:
            raise ValueError(f"Singurele varinate de clase acceptate sunt:economy, economy plus si business")
        if checkin_rezervare not in ['Da', 'Nu']:
            raise ValueError(f'Singurele varinate de checkin acceptate sunt : Da sau Nu')
        print('Adaugarea a fost inregistrata.')
        return create(rezervari, id_rezervare, nume_rezervare, clasa_rezervare, pret_rezervare, checkin_rezervare)
    except ValueError as ve:
        print("Eroarea:",ve)
    return rezervari

def afisare(rezervari):
    """
    afiseaza toate rezervarile facute
    :param rezervari: rezervarile facute
    """
    for rezervare in rezervari:
        print(get_all(rezervare))


def stergere(rezervari):
    """
    sterge o rezervare dorita
    :param rezervari: rezervarile actuale
    :return: rezervarile dupa stergere
    """
    try:
        id_sters = int(input("Dati id-ul rezervarii pe care doriti sa o eliminati"))
        rezervari = delete(rezervari, id_sters)
        print("Stergerea a fost efectuata cu succes.")
        return rezervari
    except ValueError as ve:
        print('Eroare:',ve)
    return rezervari


def modificare(rezervari):
    """
    modifca o rezervare
    :param rezervari: rezervarile curente
    :return: rezervarile dupa modificarea facuta
    """
    id_rezervare = int(input('Dati id-ul rezervarii pe care vreti sa o modificati:'))
    nume_rezervare = input('Dati numele celui care a facut rezervarea:')
    clasa_rezervare = input('Dati clasa rezervarii:')
    pret_rezervare = int(input('Dati pretul biletului:'))
    checkin_rezervare = input('A fost facut checkin-ul ?:')
    print("Modificarea s-a efectuat cu succes.")
    return update(rezervari,
                  creeaza_rezervare(id_rezervare, nume_rezervare, clasa_rezervare, pret_rezervare, checkin_rezervare))


def CRUD_MENU(rezervari):
    """
    submeniul pentru optiunea 1
    :param rezervari: lista de rezervari
    :return: lista de rezervari dupa prelucrate
    """
    while True:
        print('1.Adauga o rezervare.')
        print('2.Modifica o rezervare.')
        print('3.Sterge o rezervare.')
        print('4.Revii la lista anterioara de functionalitati.')
        print('a.Afiseaza lista de rezervari.')
        optiune = input('Alege optiunea:')
        if optiune == '1':
            rezervari = adaugare(rezervari)
        elif optiune == '2':
            rezervari = modificare(rezervari)
        elif optiune == '3':
            rezervari = stergere(rezervari)
        elif optiune == 'a':
            afisare(rezervari)
        elif optiune == '4':
            return rezervari


def run_ui(rezervari):
    """
    meniul propriu-zis
    :param rezervari: lista cu rezervari
    :return: lista cu rezervari dupa modificarile aferente
    """
    while True:
        show_menu()
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            rezervari = CRUD_MENU(rezervari)
        elif optiune == '2':
            try:
                nume_upgrade = input('Dati numele persoanei careia vreti sa ii upgradati clasa:')
                rezervari = Upgrade(rezervari, nume_upgrade)
                print("Upgrade-ul s-a realizat.")
            except ValueError as ve:
                print ('Eroare',ve)
        elif optiune == '3':
            try:
                procent_ieftinire=float(input('Dati procentul cu care vreti sa se ieftineasca pretul biletelor(intre 0 si 100'))
                rezervari= ieftinire_checkin(rezervari, procent_ieftinire)
                print('preturile au fost reduse.')
            except ValueError as ve:
                print('Eroare',ve)
        elif optiune == '8':
            break
        elif optiune == 'a':
            afisare(rezervari)
    return rezervari
