
import mysql.connector

def setup():
    db = mysql.connector.connect(host = "localhost", user = "root", passwd = "Virtuoso")
    curs = db.cursor()
    curs.execute("drop database if exists Crypt;")
    curs.execute("create database Crypt;")
    curs.execute("use Crypt;")
    curs.execute("create table Vault (Alias varchar(20) primary key, Vault_Key varchar(6), Fernet_Key varchar(45));")
    curs.execute("create table Ad (adk varchar(20));")
    adk = input('Administrator Key: ')
    curs.execute("insert into Ad value('{}')".format(adk))
    db.commit()
    print('Setup complete')

def edadk():
    db = mysql.connector.connect(host = "localhost", user = "root", passwd = "Virtuoso", database = "Crypt")
    curs = db.cursor()
    adk = input('New Administrator Key: ')
    curs.execute('delete from Ad;')
    curs.execute("insert into Ad value('{}')".format(adk))
    db.commit()
    print('Administrator Key changed')
    
def prog():
    i = input(': ')
    if i in ['Setup','setup']:
        setup()
    elif i in ['Edit','edit']:
        edadk()
    else:
        prog()


prog()
    
