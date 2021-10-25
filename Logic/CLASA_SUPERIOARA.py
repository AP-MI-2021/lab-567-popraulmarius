from Domain.Rezervari import *
def Upgrade(lista_rezervari,nume_dat):
    '''
    Trece la o clasa superioara rezervarea unui nume dat
    :param lista_rezervari: lista de rezervari actuala
    :param nume_dat: numele persoanei care trebuie sa i se faca upgrade de clasa
    :return: lista dupa upgrade
    '''
    lista_noua=[]
    for rezervare in lista_rezervari:
        if get_nume(rezervare) != nume_dat:
            lista_noua.append(rezervare)
        else:
            if get_clasa(rezervare)=='economy':
                clasa_noua='economy plus'
            else:
                clasa_noua='business'
            lista_noua.append(
                [
                    ('id', get_id(rezervare)),
                    ('nume',get_nume(rezervare)),
                    ('clasa',clasa_noua),
                    ('pret',get_pret(rezervare)),
                    ('checkin',get_checkin(rezervare))
                ]
            )
    return lista_noua