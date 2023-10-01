import os
from cryptography.fernet import Fernet
import random

def codes():
    print('')
    print('Enter command code')
    print('Create Crypt:   1')
    print('View Crypt:     2')
    print('Admin:          3')
    print('Delete Crypt    4')
    code = input('>>>             ')
    if code == '1':
        create()
    if code == '2':
        view()
    if code == '3':
        admin()
    if code == '4':
        delete()
        

def delete():
    user = input('Enter Username: ')
    p = input('Enter Password: ')
    st = user+'_'+p
    with open('Crypt.txt', 'r+') as cr:
        if st in cr.read():
            conf = input('Do you want to delete your Crypt \n Type CONFIRM: ')
            if conf == 'CONFIRM':
                with open("Crypt.txt",'r') as cr:
                    lines = cr.readlines()
                with open("Crypt.txt",'w') as cr:
                    for line in lines:
                        if line.find(st) != -1:
                            pass
                        else:
                            cr.write(line)
                os.remove('User/'+user+'.txt') 
            cr.close()
        else:
            print('Invalid Username or Password')
            cr.close()
            codes()
    codes()

def admin():
    di = {}
    user = 'Administrator'
    p = input('Enter Password: ')
    st = user+'_'+p
    with open('Admin.txt', 'r+') as ad:
        if st in ad.read():
            with open('Crypt.txt', 'r+') as cr:
                for li in cr.readlines():
                    k, val = li.split()
                    di[k] = val
                print('Welcome Administrator')
                print('User_Password\t\t', 'Key')
                print('')
                for i in di:
                    print(i, '\t\t',di[i])
    print('')
    codes()

def view():
    di = {}
    user = input('Enter Username: ')
    p = input('Enter Password: ')
    st = user+'_'+p
    key = input('Enter Key: ')
    with open('Crypt.txt', 'r+') as cr:
        if st in cr.read():
            with open('User\\'+user + '.txt', 'r') as rr:
                key = key.encode()
                f = Fernet(key)
                decr = f.decrypt(rr.read().encode())
                print(user + ':')
                print(decr.decode('utf-8'))
        else:
            print('Invalid Username or Password or Key')
            codes()
    codes()

def remove(st):
    return st.replace(" ", "")
       
def create():
    user = input('Enter username: ')
    with open('Crypt.txt', 'r+') as cr:
        if user in cr.read():
            print('Username already in use')
            create()
    d = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890" 
    p = "".join(random.sample(d,6))
    print('Your crypt password is:', p)
    key = Fernet.generate_key()
    f = Fernet(key)
    print('Your assigned key is:', key.decode('utf-8'))
    file = open('Crypt.txt', 'a+')
    st = remove(user+'_'+p)
    file.write('\n' + st + ' '+ key.decode('utf-8'))
    file.close()
    data = input('Input data:')
    file = open('User\\'+user + '.txt', 'wb')
    token = f.encrypt(data.encode())
    file.write(token)
    file.close()
    codes()

print('Welcome to the Crypt')
codes()


