def creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin):
    '''
    
    :param id_rezervare: id-ul rezervarii
    :param nume: numele pasagerului caruia ii corespunde rezervare
    :param clasa: clasa la care zboara pasagerul
    :param pret: pretul biletului
    :param checkin: si-a facut sau nu checkin-ul pasagerul
    :return: un dictionar cu datele despre rezervare
    '''
    return {
        'id': id_rezervare,
        'nume': nume,
        'clasa': clasa,
        'pret':pret,
        'checkin':checkin,
    }
def get_id(rezervare):
    '''

    :param rezervare: rezervarea careia vrem sa ii aflam id-ul
    :return: returneaza id-ul rezervarii
    '''

    return rezervare['id']

def get_nume(rezervare):
    '''

    :param rezervare: rezervarea pentru care vrem sa aflam pasagerul
    :return: returneaza numele clientului care are rezervarea
    '''
    return rezervare['nume']

def get_clasa(rezervare):
    '''

    :param rezervare: rezervarea din care vrem sa aflam clasa
    :return: clasa specifica rezervarii
    '''
    return rezervare['clasa']

def get_pret(rezervare):
    '''

    :param rezervare: rezervarea careia vrem sa aflam pretul
    :return: pretul rezervarii
    '''
    return rezervare['pret']

def get_checkin(rezervare):
    '''

    :param rezervare: rezervarea pentru care vrem sa vedem daca a fost facut check-in-ul
    :return: returneaza daca a fost sau nu facut checkin-ul
    '''
    return rezervare['checkin']