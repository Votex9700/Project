#Importing necessary modules
import os
from cryptography.fernet import Fernet
import random
import mysql.connector
import subprocess


#Connect sql to python
db = mysql.connector.connect(host = "localhost", user = "root", passwd = "Virtuoso", database = "Crypt")
curs = db.cursor()

def codes():
    print('')
    print('Enter command code')
    print('Create Crypt:   1')
    print('View Crypt:     2')
    print('Delete Crypt    3')
    code = input('>>>             ')
    if code == '1':
        create()
    elif code == '2':
        view()
    elif code == '3':
        delete()
    elif code == 'ad':
        admin()
    else:
        codes()

def delete():
    user = input('Enter Alias: ')
    p = input('Enter Vault key: ')
    curs.execute('Select * from Vault;')
    vt = curs.fetchall()
    y = 0
    al = []
    vk = []
    for i in vt:
        al.append(vt[y][0])
        vk.append(vt[y][1])
        y+=1
    if user in al and p in vk:
        conf = input('Do you want to delete your Vault\n Type CONFIRM: ')
        if conf == 'CONFIRM':
            curs.execute("Delete from Vault where Alias = '{}';".format(user))
            db.commit()
            os.remove('User/'+user+'.txt')
        else:
            print('Invalid Alias or Vault Key')
            codes()
    codes()

def admin():
    ad = input('Access key: ')
    curs.execute('Select * from Ad;')
    adk = curs.fetchone()[0]
    if ad == adk:
        curs.execute('Select * from Vault;')
        vt = curs.fetchall()
        y = 0
        al = []
        vk = []
        for i in vt:
            al.append(vt[y][0])
            vk.append(vt[y][1])
            y+=1
        print('Welcome Administrator')
        print('Alias\t\t','Vault_Key')
        for i in al:
            print(i,'\t\t',vk[al.index(i)])
        codes()
    else:
        print('Invalid access key')
        codes()
        
def view():
    user = input('Enter Alias: ')
    p = input('Enter Vault key: ')
    curs.execute('Select * from Vault;')
    vt = curs.fetchall()
    y = 0
    al = []
    vk = []
    for i in vt:
        al.append(vt[y][0])
        vk.append(vt[y][1])
        y+=1
    if user in al and p in vk and al.index(user) == vk.index(p):
        curs.execute("Select Fernet_Key from Vault where Alias = '{}';".format(user))
        key = curs.fetchone()[0]
        with open('User\\'+user + '.txt', 'r') as rr:
            key = key.encode()
            f = Fernet(key)
            decr = f.decrypt(rr.read().encode())
            print(user + ':')
            print(decr.decode('utf-8'))
    else:
        print('Invalid Username or Vault key')
        codes()
    codes()
       
def create():
    user = input('Enter Alias: ')
    syn = 'select * from Vault;'
    curs.execute(syn)
    vt = curs.fetchall()
    al = []
    y = 0
    for i in vt:
        al.append(vt[y][0])
        y+=1
    if user in al:
        print('Alias already in use')
        create()
    d = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890" 
    p = "".join(random.sample(d,6))
    print('Your Vault key is:', p)
    key = Fernet.generate_key()
    f = Fernet(key)
    curs.execute("Insert into Vault (Alias,Vault_Key,Fernet_Key) values('{}','{}','{}');".format(user,p,key.decode('utf-8')))
    db.commit()
    data = input('Input data: ')
    file = open('User\\'+user + '.txt', 'wb')
    token = f.encrypt(data.encode())
    file.write(token)
    file.close()
    codes()

print('Welcome to the Crypt')
codes()


