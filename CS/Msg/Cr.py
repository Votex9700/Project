import mysql.connector
db = mysql.connector.connect(host = "localhost", user = "root", passwd = "Virtuoso", database = "Project")
curs = db.cursor()
def Cr():
        with open('Cr.txt', 'a+') as cr:
                Al = input('Enter Alias      :')
                Ak = int(input('Enter Access key :'))
                if Al not in cr.readlines():
                        curs.execute("insert into Cl (Alias, Access_key) values('{}',{})".format(Al,Ak))
                        syn = "create table "+Al+" (Sender varchar(20), Message varchar(200));"
                        curs.execute(syn)
                        db.commit()
                        st = Al+'.'+str(Ak)
                        cr.write('\n'+st)
                        cr.close()
                else:
                        print('Alias already exists')
                        Cr();
Cr();

