from Domain.Rezervari import creeaza_rezervare, get_id


def create(lista_rezervari,id_rezervare,nume, clasa, pret, checkin):
    '''
    Adauga o nonua rezervare in lista de rezervari
    :param lista_rezervari: lista cu rezervarile
    :param id_rezervare:id-ul noii rezervari care urmeaza sa fie adaugata in lista
    :param nume: numele pe care a fost facuta noua rezervare
    :param clasa: clasa specifica noii rezervari
    :param pret:pretul biletului pentru rezervarea specifica
    :param checkin: specifica daca a fost sau nu facut check-in-ul
    :return: lista actualizata cu noua rezervare
    '''
    rezervare= creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin)
    return lista_rezervari + [rezervare]

def read(lista_rezervari,id_rezervare):
    '''

    :param lista_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii pe care trebuie sa il cautam in lista
    :return:
    '''
    rezercare_cu_id= None
    for rezervare in lista_rezervari:
        if get_id(rezervare)== id_rezervare:
            rezervare_cu_id=rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return lista_rezervari

def delete(lista_rezervari,id_rezervare):
    """
    elimina o rezervare dupa un id dat din lista de rezervari
    :param lista_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii pe care vrem sa o stergem
    :return: lista nou creata fara rezervarea care trebuia sa fie eliminata
    """
    lista_noua=[]
    for rezervare in lista_rezervari:
        if get_id(rezervare) != id_rezervare:
            lista_noua.append(rezervare)
    return lista_noua

def update(lista_rezervari, rezervare_noua):
    """
    updateaza o rezervare din lista
    :param lista_rezervari: lista cu rezervari
    :param rezervare_noua: rezervarea noua facuta care trebuie adaugata
    :return: returneaza o lista noua, updatata cu noua rezervare facuta
    """
    lista_noua=[]
    for rezervare in lista_rezervari:
        if get_id(rezervare) != get_id(rezervare_noua):
            lista_noua.append(rezervare)
        else:
            lista_noua.append(rezervare_noua)
    return lista_noua