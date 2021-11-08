from Domain.Rezervari import *
def ieftinire_checkin(lista_rezervari, procent_dat,undo_list,redo_list):
    '''
    ieftineste pretul biletului daca checkin-ul a fost facut
    :param lista_rezervari: lista cu rezervari
    :param procent_dat: procentul cu care se doreste ieftinirea biletului
    :return: lista dupa reducerile aferente
    '''
    if not (0< procent_dat < 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100.')
    lista_noua = []
    undo_list.append(lista_rezervari)
    redo_list.clear()
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

def pret_max (lista_rezervari):
    preturi={}
    for rezervare in lista_rezervari:
        clasa=get_clasa(rezervare)
        pret=get_pret(rezervare)
        if clasa in preturi:
            if pret > preturi[clasa]:
                preturi[clasa]=pret
        else:
            preturi[clasa]=pret
    return preturi

def pret_pasager(lista_rezervari):
    tarife_nume={}
    for rezervare in lista_rezervari:
        nume=get_nume(rezervare)
        pret=get_pret(rezervare)
        if nume in tarife_nume:
            tarife_nume[nume]+=pret
        else:
            tarife_nume[nume]=pret
    return tarife_nume
def ordonare_desc(lista_rezervari,undo_list,redo_list):
    undo_list.append(lista_rezervari)
    redo_list.clear()
    return sorted(lista_rezervari,key=lambda rezervare : get_pret(rezervare),reverse=1)

def do_undo(lista_rezervari,undo_list, redo_list):
        if undo_list:
            top_undo = undo_list.pop()
            redo_list.append(top_undo)
            return top_undo
        return lista_rezervari


def do_redo(lista_rezervari,undo_list, redo_list):
    if redo_list:
        top_redo = redo_list.pop()
        undo_list.append(top_redo)
        return top_redo
    return lista_rezervari