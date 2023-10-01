import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", passwd = "Virtuoso", database = "Project")
curs = db.cursor()
def Exe():
    Al = input('Enter Alias     :')
    Ak = input('Enter Access Key:')
    with open('Temp.txt', 'w+') as te:
        te.write(Al)
    st = Al+'.'+Ak
    with open('Cr.txt', 'r+') as cr:
        if st in cr.read():
            Cmd();
        else:
            print('Invalid Alias or Key')
            Exe();
    cr.close()
def Cmd():
    print('Send:S \nInbox:I \nLogout:L')
    Cd = input('Enter Code:')
    if Cd == 'S':
        S();
    elif Cd == 'I':
        Inb();
    elif Cd == 'L':
        Lg();
    else:
        print('Invalid')
        Cmd();
def S():
    with open('Temp.txt', 'r+') as te:
        Al = te.read()
    Rs = input('Enter recipient alias:')
    with open('Cr.txt', 'r+') as cr:
        if Rs in cr.read():
            Msg = input('(limit 200 words)\n:')
            if len(Msg)<200:
                syn = "insert into "+Rs+"(Sender, Message) value('{}','{}')"
                curs.execute(syn.format(Al,Msg))
                db.commit()
                print('Sent')
            else:
                print('Limit exceeded')
                S();
        else:
            print('Invalid alias')
            S()
    cr.close()
    Cmd();
def Inb():
    with open('Temp.txt', 'r+') as te:
        Al = te.read()
    with open('Cr.txt', 'r+') as cr:
        if Al in cr.read():
            Ib = curs.execute("select * from "+Al)
            Re = curs.fetchall()
            for i in Re:
                print(i[0]+': '+i[1])
            Cmd();
        else:
            print('Invalid alias')
            Inb();
def Lg():
    conf = input('Confirm(y/n):')
    if conf == 'y':
        Exe();
    else:
        Cmd();
Exe()
