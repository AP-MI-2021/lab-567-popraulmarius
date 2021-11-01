from Domain.Rezervari import *
def ieftinire_checkin(lista_rezervari, procent_dat):
    '''
    ieftineste pretul biletului daca checkin-ul a fost facut
    :param lista_rezervari: lista cu rezervari
    :param procent_dat: procentul cu care se doreste ieftinirea biletului
    :return: lista dupa reducerile aferente
    '''
    if not (0< procent_dat < 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100.')
    lista_noua = []
    for rezervare in lista_rezervari:
        if get_checkin(rezervare) == "Nu":
            lista_noua.append(rezervare)
        else:
            lista_noua.append(
                [
                    ('id', get_id(rezervare)),
                    ('nume', get_nume(rezervare)),
                    ('clasa', get_clasa(rezervare)),
                    ('pret', get_pret(rezervare)-(get_pret(rezervare)*procent_dat/100)),
                    ('checkin', get_checkin(rezervare))
                ]
            )

    return lista_noua