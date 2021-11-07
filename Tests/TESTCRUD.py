from Domain.Rezervari import creeaza_rezervare, get_id
from Logic.CLASA_SUPERIOARA import Upgrade
from Logic.CRUD import create,read,update,delete
from Logic.cerinte import ieftinire_checkin
def get_data():
    '''
    :return: returneaza un set de date pentru care se fac testele
    '''
    return [
        creeaza_rezervare(1,'Mihai','economy plus',700,'Da'),
        creeaza_rezervare(2, 'Alexandra', 'economy plus', 650, 'Nu'),
        creeaza_rezervare(3, 'Ilie', 'economy', 100, 'Da'),
        creeaza_rezervare(4, 'Matei', 'economy plus', 500, 'Da'),
        creeaza_rezervare(5, 'George', 'business', 1700, 'Nu'),
        creeaza_rezervare(6, 'Mihaela', 'economy', 400, 'Da')
    ]

def test_create():
    '''
     testeaza functia create
    '''
    rezervari= get_data()
    params= (12,'Radu','business',1000,'Da')
    rezervare_noua=creeaza_rezervare(*params)
    noi_rezervari= create(rezervari, *params)
    assert rezervare_noua in noi_rezervari
def test_read():
    '''
    testeaza functia read
    '''
    rezervari=get_data()
    o_rezervare=rezervari[2]
    assert read(rezervari,get_id(o_rezervare))==o_rezervare

def test_update():
    '''
    testeaza daca functia update functioneaza
    '''
    rezervari=get_data()
    r_updated= creeaza_rezervare(5,'Radu','business',1000,'Da')
    updated= update(rezervari,r_updated)
    assert r_updated in updated
    assert r_updated not in rezervari
    assert len(updated) == len(rezervari)

def test_delete():
    '''
    testeaza daca functia delete functioneaza
    '''
    rezervari=get_data()
    to_delete=3
    r_deleted=read(rezervari,to_delete)
    deleted= delete(rezervari,to_delete)
    assert r_deleted not in deleted
    assert r_deleted in rezervari
    assert len(deleted)==len(rezervari)--1

def test_upgrade():
    '''
    testeaza daca functia upgrade functioneaza
    '''
    rezervari=get_data()
    rezervare=creeaza_rezervare(3, 'Ilie', 'economy plus', 100, 'Da')
    rezervari=Upgrade(rezervari,'Ilie')
    assert rezervare in rezervari

def test_ieftinire():
    '''
    testeaza daca functia ieftinire functioneaza
    '''
    rezervari = get_data()
    rezervare= creeaza_rezervare(3, 'Ilie', 'economy', 70, 'Da')
    rezervari= ieftinire_checkin(rezervari, 30)
    assert rezervare in rezervari

def test_all():
    test_create()
    test_read()
    test_update()
    test_upgrade()
    test_ieftinire()
