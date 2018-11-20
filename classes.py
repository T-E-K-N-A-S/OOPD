import sqlite3
import os
import time
import random
import calendar
import datetime 
class DB():
    def __init__(self):
        conn = sqlite3.connect('test.db')
        print(conn)
        #super DB, self).__init__(*args))    

class Patient:
    def __init__(self):
        pass
    def create(self):
        print('inside patient create')
        self.get_input()
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists PATIENT
         (PATIENT_ID    INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         ADDRESS        CHAR(50),
         PHONE1         TEXT,
         PHONE2         TEXT,
         DOB            TEXT,
         PASSWORD       TEXT);''')
        
        insert_q = '''insert into PATIENT values (?,?,?,?,?,?,?,?)'''
        insert_tup = (self.patientID,self.name,self.email,self.address,self.phone1,self.phone2,self.dob,self.password)
        conn.execute(insert_q,insert_tup)
        conn.commit()
        
        cursor = conn.execute('SELECT * from PATIENT')
        output =cursor.fetchall()
        for row in output:
            print(row)

    def login(self):
        name = input('name: ')
        emailid = input('emailid: ')
        passwd = input('password: ')
        
        insert_q = '''select * from PATIENT where NAME = ? AND EMAIL = ? AND PASSWORD = ?'''
        insert_tup = (name,emailid,passwd)
        conn = sqlite3.connect('test.db')
        cur = conn.execute(insert_q,insert_tup)
        output = cur.fetchall()
        if len(output) == 1:
            self.patientID,self.name,self.email,self.address,self.phone1,self.phone2,self.dob,self.password = output[0]
            return 1
        else:
            return 0

    def get_input(self):
        self.patientID = random.randint(10000,99999) # 5 digit uniq id
        fname = input('First name: ')
        lname = input('Last name: ')
        self.name = fname + ' ' +  lname
        self.email = input('Email: ')
        self.address = input('Address: ')
        self.phone1 = input('Phone 1: ')
        self.phone2 = input('Alternate phone: ')
        self.dob = input('DOB: ')
        self.password = input('Set Password: ')
    
    def menu(self):
        print('inside user menu')
        while 1:
            print('\n1 search doctor\n2 book appt\n3 show records\n4 show_local\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.search_doctor()
            elif c == 2:
                self.book_appt()
            elif c == 3:
                self.show_records()
            elif c == 4:
                self.show_local()
            else:
                print("*invalid input*")

    def search_doctor(self):
        dept_list = ['allergy','dental','dermitology','general','orthopedic','cardiology','neurology']
        department = dept_list[ int(input('select department\n 1:allergy 2:dental 3:dermitology 4:general 5:orthopedic 6:cardiology 7:neurology'))-1]
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT DOCTOR_ID, NAME,EMAIL,CATEGORY,DEPARTMENT from DOCTOR where DEPARTMENT is ?',(department,))
        output =cursor.fetchall()
        for row in output:
            print(row)

        

    def book_appt(self):
        self.search_doctor()
        docid = int(input('select doc id to book appt: '))

        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists APPT
         (APPT_ID    INT     PRIMARY KEY     NOT NULL,
         PAT_ID           INT    NOT NULL,
         DOC_ID          INT    NOT NULL,
         DATE        TEXT,
         TIME         TEXT);''')


        cal = calendar.month(2018,11)
        print(cal)
        today = datetime.date.today()
        apptdate = input('input date for appt (yyyy-mm-dd)')
        apptdate =apptdate.split('-')
        d = datetime.date(int(apptdate[0]),int(apptdate[1]),int(apptdate[2]))
        #apptdate = time.strptime(apptdate, "%Y-%m-%d")
        appt_list = [x for x in range(10,17)]
        #print(appt_list)
        
        #print(d,today)
        if (d <= today):
            print('invalid date')
            return
        else:
            cursor = conn.execute('SELECT TIME from APPT where  DOC_ID = ? AND DATE = ?',(docid,d.strftime('%Y,%m,%d')))
            output = cursor.fetchall()
            #for row in output:
            #    print(row)
            print(output)
            output = [i[0] for i in output]
            if len(output)> 0:
                for i in appt_list:
                    if str(i) not in output:
                        print(i,end=' - ')
            slot = int(input('select your slot: '))
            insert_q = '''insert into APPT values (?,?,?,?,?)'''
            insert_tup = (random.randint(10000,99999),self.patientID,docid,d.strftime('%Y,%m,%d'),slot)
            conn.execute(insert_q,insert_tup)
            conn.commit()


    def show_records(self):
        pass
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT DOCTOR_ID,DEPT,REPORT,DRUGS,DATE from RECORD where PATIENT_ID = ? ',(self.patientID,))
        output = cursor.fetchall()
        #print('date\t\ttime\tid\tname')
        for row in output:
            print ('\n--- RECORD ---')
            print('Doctor: ',end='\t')
            cur = conn.execute('SELECT NAME from DOCTOR where DOCTOR_ID = ? ',(row[0],))
            out = cur.fetchall()
            print(out[0][0])
            print('Doctor ID: ',row[0])
            print('Department: ',row[1])
            print('Report: ',row[2])
            print('Drugs: ',row[3])
            print('Date of report: ',row[4])
    

    def show_local(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT LOCAL_ID,DOCTOR_ID,ROOM,BED,ADMIT_DATE,DISCHARGE_DATE from LOCAL where PATIENT_ID = ? ',(self.patientID,))
        output = cursor.fetchall()
        print('localid\tdoctorid\troom\tbed\tadmit date\tdischarge date')
        for row in output:
            for r in row:
                print(r,end = '\t')
    

'''



D   O   C   T   O   R




'''

class Doctor:
    def __init__(self):
        pass
    def get_input(self):
        doctorID = random.randint(10000,99999) # 5 digit uniq id
        fname = input('First name: ')
        lname = input('Last name: ')
        name = fname + ' ' + lname
        email = input('Email: ')
        age = input('age: ')
        dept_list = ['allergy','dental','dermitology','general','orthopedic','cardiology','neurology']
        department = dept_list[ int(input('select department\n 1:allergy 2:dental 3:dermitology 4:general 5:orthopedic 6:cardiology 7:neurology'))-1]
        cat_list = ['junior-residents', 'senior-residents', 'specialists', 'senior-specialists']
        category = cat_list[ int(input('select category\n 1:junior residents, 2:senior residents, 3:specialists, 4:senior specialists '))-1]
        hospital_id = input('hospital id: ')
        password = input('Set Password: ')
        return doctorID,name,email,age,department,category,hospital_id,password

    def create(self):
        print('inside doctor create')
        
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists DOCTOR
         (DOCTOR_ID    INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         AGE        CHAR(10),
         DEPARTMENT     TEXT,
         CATEGORY       TEXT,
         HOSPITAL_ID     TEXT,
         PASSWORD       TEXT);''')
        
        insert_q = '''insert into DOCTOR values (?,?,?,?,?,?,?,?)'''
        insert_tup = tuple(self.get_input())
        conn.execute(insert_q,insert_tup)
        conn.commit()
        
        cursor = conn.execute('SELECT * from DOCTOR')
        output =cursor.fetchall()
        for row in output:
            print(row)

    def login(self):
        name = input('name: ')
        emailid = input('emailid: ')
        passwd = input('password: ')
        
        insert_q = '''select * from DOCTOR where NAME = ? AND EMAIL = ? AND PASSWORD = ?'''
        insert_tup = (name,emailid,passwd)
        conn = sqlite3.connect('test.db')
        cur = conn.execute(insert_q,insert_tup)
        output = cur.fetchall()
        if len(output) == 1:
            self.doctorID,self.name,self.email,self.age,self.department,self.category,self.hospital_id,self.password = output[0]
            return 1
        else:
            return 0

    def menu(self):
        
        print('inside user menu')
        while 1:
            print('\n1 view patient\n2 show records\n3 view schedule\n4 create report\n5 refer patient local\n6 shift patient to local\n7 show local\n8 refer patient opd\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.view_patient()
            elif c == 2:
                self.show_records()
            elif c == 3:
                self.view_schedule()
            elif c == 4:
                self.create_record()
            elif c == 5:
                self.refer_patient_local()   
            elif c == 6:
                self.shift_patient_to_local()
            elif c == 7:
                self.show_local()   
            elif c == 8:
                self.refer_patient_opd()  
            else:
                print("*invalid input*")
        
    def view_patient(self):
        pass
    def view_history(self):
        pass
    def view_schedule(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT PAT_ID,DATE,TIME from APPT where DOC_ID = ? ',(self.doctorID,))
        output = cursor.fetchall()
        print('date\t\ttime\tid\tname')
        for row in output:
            print (row[1],'\t',row[2],'\t',row[0],end='\t')
            cur = conn.execute('SELECT NAME from PATIENT where PATIENT_ID = ? ',(row[0],))
            out = cur.fetchall()
            print(out[0][0])
    #print(output)

    def create_report(self):
        rep = input('\nwrite patient report within 500 chrs: \t')
        return rep

    def pres_drugs(self):
        drugs = input('\nprescribe drugs: \t')
        return drugs

    def create_record(self):
        pass
        self.view_schedule()
        patid = int(input('select patient id: '))
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists RECORD
         (DOCTOR_ID    INT     PRIMARY KEY     NOT NULL,
         PATIENT_ID    INT    NOT NULL,
         DEPT          TEXT    NOT NULL,
         REPORT        CHAR(500),
         DRUGS      TEXT,
         DATE     TEXT,
         HIST_ID       TEXT);''')
        
        insert_q = '''insert into RECORD values (?,?,?,?,?,?,?)'''
        insert_tup = (self.doctorID,patid,self.department,self.create_report(),self.pres_drugs(),datetime.date.today().strftime('%Y,%m,%d'),random.randint(10000,99999))
        conn.execute(insert_q,insert_tup)
        conn.commit()

    def refer_patient_local(self):
        pass
        if self.category == 'senior-residents':
            print('you are senior doctor you cannot refer patients, do not run away from your responsibility')
        else:
            print('\nREFER to SENIOR DOCTOR\n')
            self.show_local()
            patid = int(input('select patient id to be refered: '))

            print('\nList of senior doctors\n')
            conn = sqlite3.connect('test.db')
            cursor = conn.execute('SELECT DOCTOR_ID,NAME,DEPT,CATEGORY  from DOCTOR where CATEGORY = ? AND DEPARTMENT = ? ',(self.category,self.department))
            output = cursor.fetchall()
            for o in output:
                print(o)

            docid = int(input('select senior doc: '))
            cursor = conn.execute('UPDATE LOCAL SET DOCTOR_ID = ? where PATIENT_ID = ? ',(docid,patid))
            conn.commit()
            print('patient transfered to doc id:',docid)

    def refer_patient_opd(self):
        pass
        if self.category == 'senior-residents':
            print('you are senior doctor you cannot refer patients, do not run away from your responsibility')
        else:
            print('\nREFER to SENIOR DOCTOR\n')
            self.view_schedule()
            patid = int(input('select patient id to be refered: '))
            date = input('date yyyy-mm-dd')
            print('\nList of senior doctors\n')
            conn = sqlite3.connect('test.db')
            cursor = conn.execute('SELECT DOCTOR_ID,NAME,DEPARTMENT,CATEGORY  from DOCTOR where CATEGORY = ? AND DEPARTMENT = ? ',('senior-residents',self.department))
            output = cursor.fetchall()
            for o in output:
                print(o)

            docid = int(input('select senior doc: '))
            cursor = conn.execute('UPDATE APPT SET DOC_ID = ? where PAT_ID = ? ',(docid,patid))
            conn.commit()
            print('patient transfered to doc id:',docid)


    def show_local(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT LOCAL_ID,PATIENT_ID,ROOM,BED,ADMIT_DATE,DISCHARGE_DATE from LOCAL where DOCTOR_ID = ? ',(self.doctorID,))
        output = cursor.fetchall()
        print('localid\patientId\troom\tbed\tadmit date\tdischarge date')
        for row in output:
            for r in row:
                print(r,end = '\t')
            print('\n')
            
        


    def show_records(self):
        pass
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT PATIENT_ID,DEPT,REPORT,DRUGS,DATE from RECORD where DOCTOR_ID = ? ',(self.doctorID,))
        output = cursor.fetchall()
        #print('date\t\ttime\tid\tname')
        for row in output:
            print ('\n--- RECORD ---')
            print('Patient name: ',end='\t')
            cur = conn.execute('SELECT NAME from PATIENT where PATIENT_ID = ? ',(row[0],))
            out = cur.fetchall()
            print(out[0][0])
            print('Patient ID: ',row[0])
            print('Department: ',row[1])
            print('Report: ',row[2])
            print('Drugs: ',row[3])
            print('Date of report: ',row[4])

    def shift_patient_to_local(self):
        pass
        self.show_records()
        patid = int(input('select patient to be moved to LOCAL'))
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists LOCAL
         (PATIENT_ID    INT     PRIMARY KEY     NOT NULL,
         DOCTOR_ID           INT        NOT NULL,
         LOCAL_ID          INT    NOT NULL,
         ROOM        INT,
         BED     INT,
         ADMIT_DATE     TEXT,
         DISCHARGE_DATE    TEXT);''')
        
        room = int(input('insert room'))
        bed = int(input('insert bed'))
        admit_date = input('admit date in yyyy-mm-dd')
        discharge_date = input('discharge date in yyyy-mm-dd')
        insert_q = '''insert into LOCAL values (?,?,?,?,?,?,?)'''
        insert_tup = (patid,self.doctorID,random.randint(10000,99999),room,bed,admit_date,discharge_date)
        conn.execute(insert_q,insert_tup)
        conn.commit()


'''





A   D   M   I   N








'''

class Admin(Doctor):
    def __init__(self):
        pass
    def get_input(self):
        adminID = random.randint(10000,99999) # 5 digit uniq id
        fname = input('First name: ')
        lname = input('Last name: ')
        name = fname + ' ' + lname
        email = input('Email: ')
        phone = input('phone: ')
        password = input('Set Password: ')
        return adminID,name,email,phone,password
    def create(self):
        print('inside admin create')
        
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists ADMIN
         (ADMIN_ID    INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         PHONE        TEXT,
         PASSWORD       TEXT);''')
        
        insert_q = '''insert into ADMIN values (?,?,?,?,?)'''
        insert_tup = tuple(self.get_input())
        conn.execute(insert_q,insert_tup)
        conn.commit()
        
        cursor = conn.execute('SELECT * from ADMIN')
        output =cursor.fetchall()
        for row in output:
            print(row)

    def login(self):
        name = input('name: ')
        emailid = input('emailid: ')
        passwd = input('password: ')
        
        insert_q = '''select * from ADMIN where NAME = ? AND EMAIL = ? AND PASSWORD = ?'''
        insert_tup = (name,emailid,passwd)
        conn = sqlite3.connect('test.db')
        cur = conn.execute(insert_q,insert_tup)
        output = cur.fetchall()
        if len(output) == 1:
            self.adminID,self.name,self.email,self.phone,self.password = output[0]
            return 1
        else:
            return 0

    def menu(self):
        
        print('inside admin console')
        while 1:
            print('\n1 add doctor\n2 rem doctor\n3 view patient\n4 rem patient\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.add_doctor()
            elif c == 2:
                self.rem_doctor()
            elif c == 3:
                self.view_patient()
            elif c == 4:
                self.rem_patient()
            else:
                print("*invalid input*")
        
    def add_doctor(self):
        print('inside doctor create')
        
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists DOCTOR
         (DOCTOR_ID    INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         AGE        CHAR(1),
         DEPARTMENT     TEXT,
         CATEGORY       TEXT,
         HOSPITAL_ID     TEXT,
         PASSWORD       TEXT);''')
        
        insert_q = '''insert into DOCTOR values (?,?,?,?,?,?,?,?)'''
        insert_tup = tuple(super().get_input())
        conn.execute(insert_q,insert_tup)
        conn.commit()
        print ('doctor added to SHS')
        '''
        cursor = conn.execute('SELECT * from DOCTOR')
        output =cursor.fetchall()
        for row in output:
            print(row)
        '''
    def rem_doctor(self):
        pass
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT * from DOCTOR')
        output =cursor.fetchall()

        for row in output:
            print(row)
        # var
        doc_id = input('input doctor id to be removed: ')
        # get all doc ids
        cursor = conn.execute('SELECT DOCTOR_ID from DOCTOR')
        doc_ids =cursor.fetchall()
        ids = []
        for di in doc_ids:
            ids.append(di[0])
        doc_ids = ids
        print(doc_ids)
        if doc_id.isdigit() is False:
            print('invalid doctor id ')
        elif int(doc_id) not in doc_ids:
            print('This doctor id does not exist.')
        else:
            cursor = conn.execute('DELETE from DOCTOR WHERE DOCTOR_ID = ?',(int(doc_id),))
            conn.commit()
            print('doctor removed from SHS')

        #output =cursor.fetchall()
    def view_patient(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT * from PATIENT')
        output =cursor.fetchall()
        for row in output: # formatiing needed
            for r in row:
                print(r,end = '\t')
            print('\n')

    def rem_patient(self):
        conn = sqlite3.connect('test.db')
        cursor = conn.execute('SELECT * from PATIENT')
        output =cursor.fetchall()

        for row in output:
            print(row)
        # var
        pat_id = input('input patient id to be removed: ')
        # get all doc ids
        cursor = conn.execute('SELECT PATIENT_ID from PATIENT')
        pat_ids =cursor.fetchall()
        ids = []
        for pi in pat_ids:
            ids.append(pi[0])
        pat_ids = ids
        print(pat_ids)
        if pat_id.isdigit() is False:
            print('invalid patient id ')
        elif int(pat_id) not in pat_ids:
            print('This patient id does not exist.')
        else:
            cursor = conn.execute('DELETE from PATIENT WHERE PATIENT_ID = ?',(int(pat_id),))
            conn.commit()
            print('patient removed from SHS')

'''






M   A   I   N






'''



class Main():


    def __init__(self):
        
        print('****** SHS ******')
        self.run_this_shit()

    def run_this_shit(self):
        while 1:
            print('Main menu\nselect option\n 1 user\n 2 doc\n 3 admin\n 0 exit')
            choice = int(input('> '))
            if choice == 0: 
                self.abort()
                break

            else:
                while 1:
                    print('\n1. Login\n2. Register\n0. back')
                    log_reg = int(input('> '))
                    if log_reg == 0: #back option
                        break
                    elif log_reg == 1: # login
                        self.login(choice)

                    elif log_reg == 2 : # register option
                        pass
                        self.register(choice)
                    else:
                        print('*invalid input*')

    def login(self,user):
        print('---  Login   ---')
        if user == 1:
            P = Patient()
                        
            if P.login():
                time.sleep(1)
                print('\nyou are logged in')
                os.system('cls')
                P.menu()
                self.logout()
                #self.open_menu(choice)
            else:
                print('\ninvalid username or password')

        elif user == 2:
            D = Doctor()
            if D.login():
                time.sleep(1)
                print('\nyou are logged in')
                os.system('cls')
                D.menu()
                self.logout()
                #self.open_menu(choice)
            else:
                print('\ninvalid username or password')
        elif user == 3:
            A = Admin()
            
            if A.login():
                time.sleep(1)
                print('\nyou are logged in')
                os.system('cls')
                A.menu()
                self.logout()
                #self.open_menu(choice)
            else:
                print('\ninvalid username or password')
            
        return True
        

    def check_login(self,username,password,user):
        pass

    def register(self,user):
        if user == 1:
            P = Patient()
            P.create()
        elif user == 2:
            D = Doctor()
            D.create()
        elif user == 3:
            A = Admin()
            A.create()

    def open_menu(self,user):
        
        if user == 1:
            self.user_menu()
        elif user == 2:
            self.doctor_menu()
        elif user == 3:
            self.admin_menu()
        
    def logout(self):
        print('you are logged out')
        #self.abort()
        time.sleep(1)
        os.system('cls')
        self.run_this_shit()
        

    def abort(self):
        print('\n\n****\tthank you for using our services\t****')
        
    def user_menu(self):
        print('inside user menu')
        while 1:
            print('\n1 search doctor\n2 select doctor\n3 book appointment\n4 edit profile\n5 view history\n0 logout')
            c = int(input('>'))
            if c == 0:
                self.logout()
                break
            
    def doctor_menu(self):
        print('inside doctor menu')
        
        while 1:
            print('\n1 view patient\n2 view history\n3 view schedule\n4 create report\n0 logout')
            c = int(input('>'))
            if c == 0:
                self.logout()
                break

    def admin_menu(self):
        print('inside admin menu')
        
        while 1:
            print('\n1 add doctor\n2 rem doctor\n3 add hospital\n4 rem hospital\n0 logout')
            c = int(input('>'))
            if c == 0:
                self.logout()
                break