from Domain.Rezervari import creeaza_rezervare, get_id


def create(lista_rezervari,id_rezervare,nume, clasa, pret, checkin,undo_list,redo_list):
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
    if read(lista_rezervari, id_rezervare) is not None:
        raise ValueError(f"Exista deja o rezervare cu id-ul {id_rezervare}.")
    rezervare= creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin)
    undo_list.append(lista_rezervari)
    redo_list.clear()
    return lista_rezervari + [rezervare]

def read(lista_rezervari,id_rezervare):
    '''

    :param lista_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii pe care trebuie sa il cautam in lista
    :return:
    '''
    if not id_rezervare:
        return lista_rezervari
    rezervare_cu_id= None
    for rezervare in lista_rezervari:
        if get_id(rezervare)== id_rezervare:
            rezervare_cu_id=rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return None

def delete(lista_rezervari,id_rezervare,undo_list,redo_list):
    """
    elimina o rezervare dupa un id dat din lista de rezervari
    :param lista_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii pe care vrem sa o stergem
    :return: lista nou creata fara rezervarea care trebuia sa fie eliminata
    """
    if read(lista_rezervari,id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare}pe care sa o stergem.')
    lista_noua=[]
    for rezervare in lista_rezervari:
        if get_id(rezervare) != id_rezervare:
            lista_noua.append(rezervare)
    return lista_noua

def update(lista_rezervari, rezervare_noua,undo_list,redo_list):
    """
    updateaza o rezervare din lista
    :param lista_rezervari: lista cu rezervari
    :param rezervare_noua: rezervarea noua facuta care trebuie adaugata
    :return: returneaza o lista noua, updatata cu noua rezervare facuta
    """
    if read(lista_rezervari,get_id(rezervare_noua)) is None:
        raise ValueError(f"Nu exista o prajitura cu id-ul {get_id(rezervare_noua)}pe care sa o actualizam")
    lista_noua=[]
    for rezervare in lista_rezervari:
        if get_id(rezervare) != get_id(rezervare_noua):
            lista_noua.append(rezervare)
        else:
            lista_noua.append(rezervare_noua)
    undo_list.append(lista_rezervari)
    redo_list.clear()
    return lista_noua
