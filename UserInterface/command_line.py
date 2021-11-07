from Logic.CRUD import *
from Logic.cerinte import *

def command_line(rezervari):
    m = input("Da lista de operatii pe care vrei sa le faca programul(operatii posibile : add, showall, delete, despartite prin ;, in cadrul comenzii itemele trebuie despartite doar prin virgula, fara spatii albe:")
    lst2 = (m.split(";"))
    map_object = map(str, lst2)
    lst = list(map_object)
    for i in lst:
        lst2 = (i.split(","))
        map_object = map(str, lst2)
        lst3 = list(map_object)
        if lst3[0]=='add':
            rezervari=adaugare2(rezervari,lst3)
        elif lst3[0]=='showall':
            for rezervare in rezervari:
                print(get_all(rezervare))
        elif lst3[0]=='delete':
            rezervari=stergere2(rezervari,lst3)
    return rezervari

def stergere2(rezervari,lst3):
                """
                sterge o rezervare dorita
                :param rezervari: rezervarile actuale
                :return: rezervarile dupa stergere
                """
                try:
                    id_sters = int(lst3[1])
                    rezervari = delete(rezervari, id_sters)
                    print("Stergerea a fost efectuata cu succes.")
                    return rezervari
                except ValueError as ve:
                    print('Eroare:', ve)
                return rezervari

def adaugare2(rezervari,lst3):
                """
                adauga in lista o rezervare noua
                :param rezervari: lista cu rezervarile actuale
                :return: lista cu rezervarea adaugata
                """
                try:
                    id_rezervare = int(lst3[1])
                    nume_rezervare = lst3[2]
                    clasa_rezervare = lst3[3]
                    pret_rezervare = int(lst3[4])
                    checkin_rezervare = lst3[5]
                    if clasa_rezervare not in ['economy', 'economy plus', 'business']:
                        raise ValueError(
                            f"Singurele varinate de clase acceptate sunt:economy, economy plus si business")
                    if checkin_rezervare not in ['Da', 'Nu']:
                        raise ValueError(f'Singurele varinate de checkin acceptate sunt : Da sau Nu')
                    print('Adaugarea a fost inregistrata.')
                    return create(rezervari, id_rezervare, nume_rezervare, clasa_rezervare, pret_rezervare,
                                  checkin_rezervare)
                except ValueError as ve:
                    print("Eroarea:", ve)
                return rezervari