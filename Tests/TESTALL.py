from Logic.CLASA_SUPERIOARA import Upgrade
from Logic.CRUD import create,read,update,delete
from Logic.cerinte import *

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
    undo_list=[]
    redo_list=[]
    params= (12,'Radu','business',1000,'Da')
    rezervare_noua=creeaza_rezervare(*params)
    noi_rezervari= create(rezervari, *params,undo_list,redo_list)
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
    undo_list=[]
    redo_list=[]
    r_updated= creeaza_rezervare(5,'Radu','business',1000,'Da')
    updated= update(rezervari,r_updated,undo_list,redo_list)
    assert r_updated in updated
    assert r_updated not in rezervari
    assert len(updated) == len(rezervari)

def test_delete():
    '''
    testeaza daca functia delete functioneaza
    '''
    rezervari=get_data()
    to_delete=3
    undo_list=[]
    redo_list=[]
    r_deleted=read(rezervari,to_delete)
    deleted= delete(rezervari,to_delete,undo_list,redo_list)
    assert r_deleted not in deleted
    assert r_deleted in rezervari
    assert len(deleted)==len(rezervari)--1

def test_upgrade():
    '''
    testeaza daca functia upgrade functioneaza
    '''
    undo_list=[]
    redo_list=[]
    rezervari=get_data()
    rezervare=creeaza_rezervare(3, 'Ilie', 'economy plus', 100, 'Da')
    rezervari=Upgrade(rezervari,'Ilie',undo_list,redo_list)
    assert rezervare in rezervari

def test_ieftinire():
    '''
    testeaza daca functia ieftinire functioneaza
    '''
    undo_list=[]
    redo_list=[]
    rezervari = get_data()
    rezervare= creeaza_rezervare(3, 'Ilie', 'economy', 70, 'Da')
    rezervari= ieftinire_checkin(rezervari, 30,undo_list,redo_list)
    assert rezervare in rezervari

def test_pret_max():
    rezervari=get_data()
    assert pret_max(rezervari)=={'economy plus': 700, 'economy': 400, 'business': 1700}
def test_ord_desc():
    rezervari = get_data()
    undo_list=[]
    redo_list=[]
    assert ordonare_desc(rezervari,undo_list,redo_list)==[[('id', 5), ('nume', 'George'), ('clasa', 'business'), ('pret', 1700), ('checkin', 'Nu')], [('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 4), ('nume', 'Matei'), ('clasa', 'economy plus'), ('pret', 500), ('checkin', 'Da')], [('id', 6), ('nume', 'Mihaela'), ('clasa', 'economy'), ('pret', 400), ('checkin', 'Da')], [('id', 3), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

def test_suma_pret():
    rezervari = get_data()
    assert pret_pasager(rezervari)=={'Mihai': 700, 'Alexandra': 650, 'Ilie': 100, 'Matei': 500, 'George': 1700, 'Mihaela': 400}

def test_undo_redo():
    rezervari=[]
    undo_list=[]
    redo_list=[]
    rezervari= create(rezervari,1, 'Mihai', 'economy plus', 700, 'Da',undo_list,redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari=create(rezervari,2, 'Alexandra', 'economy plus', 650, 'Nu', undo_list,redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]

    rezervari=create(rezervari,3, 'Ilie', 'economy', 100, 'Da',undo_list,redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 3), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = ordonare_desc(rezervari, undo_list, redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 3), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = do_undo(rezervari, undo_list, redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 3), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]


    rezervari=do_undo(rezervari,undo_list,redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 2), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]

    rezervari=do_undo(rezervari,undo_list,redo_list)
    assert rezervari==[[('id', 1), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari=do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[]
    rezervari=do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[]

    rezervari = create(rezervari,4, 'Mihai', 'economy plus', 700, 'Da', undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = create(rezervari,5, 'Alexandra', 'economy plus', 650, 'Nu', undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]

    rezervari = create(rezervari,6, 'Ilie', 'economy', 100, 'Da', undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 6), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')], [('id', 6), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]

    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]

    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 5), ('nume', 'Alexandra'), ('clasa', 'economy plus'), ('pret', 650), ('checkin', 'Nu')]]
    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = create(rezervari,7, 'Ilie', 'economy', 100, 'Da', undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 7), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')], [('id', 7), ('nume', 'Ilie'), ('clasa', 'economy'), ('pret', 100), ('checkin', 'Da')]]

    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = do_undo(rezervari,undo_list, redo_list)
    assert rezervari==[]
    rezervari = do_redo(rezervari, undo_list, redo_list)
    assert rezervari==[]
    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]

    rezervari = do_redo(rezervari,undo_list, redo_list)
    assert rezervari==[[('id', 4), ('nume', 'Mihai'), ('clasa', 'economy plus'), ('pret', 700), ('checkin', 'Da')]]






def test_all():
    test_create()
    test_read()
    test_update()
    test_upgrade()
    test_ieftinire()
    test_pret_max()
    test_suma_pret()
    test_ord_desc()
    test_undo_redo()
