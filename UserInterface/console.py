from Logic.cerinte import *
from UserInterface.command_line import command_line
from Tests.TESTCRUD import *

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
    print('7.Command_line_console.')
    print('a.Afiseaza lista')
    print('u.Undo')
    print ('r.Redo')
    print('e.Exit')

def adaugare(rezervari,undo_list,redo_list):
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
        rezultat= create(rezervari, id_rezervare, nume_rezervare, clasa_rezervare, pret_rezervare, checkin_rezervare,undo_list,redo_list)
        undo_list.append(rezervari)
        redo_list.clear()
        return rezultat
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


def stergere(rezervari,undo_list,redo_list):
    """
    sterge o rezervare dorita
    :param rezervari: rezervarile actuale
    :return: rezervarile dupa stergere
    """
    try:
        id_sters = int(input("Dati id-ul rezervarii pe care doriti sa o eliminati"))
        rezultat = delete(rezervari, id_sters,undo_list,redo_list)
        print("Stergerea a fost efectuata cu succes.")
        undo_list.append(rezervari)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print('Eroare:',ve)
    return rezervari


def modificare(rezervari,undo_list,redo_list):
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
    rezultat =update(rezervari,creeaza_rezervare(id_rezervare, nume_rezervare, clasa_rezervare, pret_rezervare, checkin_rezervare),undo_list,redo_list)
    undo_list.append(rezervari)
    redo_list.clear()
    return rezultat

def CRUD_MENU(rezervari,undo_list,redo_list):
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
            rezervari = adaugare(rezervari,undo_list,redo_list)
        elif optiune == '2':
            rezervari = modificare(rezervari,undo_list,redo_list)
        elif optiune == '3':
            rezervari = stergere(rezervari,undo_list,redo_list)
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
    undo_list=[]
    redo_list=[]
    while True:
        show_menu()
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            rezervari = CRUD_MENU(rezervari,undo_list,redo_list)
        elif optiune == '2':
            try:
                nume_upgrade = input('Dati numele persoanei careia vreti sa ii upgradati clasa:')
                rezervari = Upgrade(rezervari, nume_upgrade,undo_list,redo_list)
                print("Upgrade-ul s-a realizat.")
            except ValueError as ve:
                print ('Eroare',ve)
        elif optiune == '3':
            try:
                procent_ieftinire=float(input('Dati procentul cu care vreti sa se ieftineasca pretul biletelor(intre 0 si 100'))
                rezervari= ieftinire_checkin(rezervari, procent_ieftinire,undo_list,redo_list)
                print('preturile au fost reduse.')
            except ValueError as ve:
                print('Eroare',ve)
        elif optiune == '4':
            print(pret_max(rezervari))
        elif optiune == '5':
            rezervari=ordonare_desc(rezervari,undo_list,redo_list)
        elif optiune =='6':
            print(pret_pasager(rezervari))
        elif optiune == 'e':
            break
        elif optiune == 'a':
            afisare(rezervari)
        elif optiune == '7':
            rezervari=command_line(rezervari)
        elif optiune == 'u':
            if len(undo_list) > 0:
                print('S-a efectuat undo.')
                redo_list.append(rezervari)
                rezervari = undo_list.pop()
            else:
                print('Nu se poate face Undo.')
        elif optiune =='r':
            if len(redo_list)>0:
                rezervari=redo_list.pop()
                print('S-a efectuat redo.')
            else:
                print('Nu se poate face redo.')
        else:
            print("ati introdus o optiune gresita")
    return rezervari
