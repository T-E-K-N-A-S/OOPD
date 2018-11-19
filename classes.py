import sqlite3
import os
import time
import random

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
            print('\n1 add doctor\n2 rem doctor\n3 add hospital\n4 rem hospital\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.add_doctor()
            elif c == 2:
                self.rem_doctor()
            elif c == 3:
                self.add_hospital()
            elif c == 4:
                self.rem_hospital()
            else:
                print("*invalid input*")

    def add_doctor(self):
        pass
    def rem_doctor(self):
        pass
    def add_hospital(self):
        pass
    def rem_hospital(self):
        pass
    





class Doctor:
    def __init__(self):
        pass
    def get_input(self):
        self.doctorID = random.randint(10000,99999) # 5 digit uniq id
        fname = input('First name: ')
        lname = input('Last name: ')
        self.name = fname + ' ' + lname
        self.email = input('Email: ')
        self.age = input('age: ')
        self.department = input('department: ')
        self.category = input('category : ')
        self.hospital_id = input('hospital id: ')
        self.password = input('Set Password: ')

    def create(self):
        print('inside patient create')
        self.get_input()
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
        insert_tup = (self.doctorID,self.name,self.email,self.age,self.department,self.category,self.hospital_id,self.password)
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
            print('\n1 view patient\n2 view history\n3 view schedule\n4 create report\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.view_patient()
            elif c == 2:
                self.view_history()
            elif c == 3:
                self.view_schedule()
            elif c == 4:
                self.create_report()
            else:
                print("*invalid input*")
        
    def view_patient(self):
        pass
    def view_history(self):
        pass
    def view_schedule(self):
        pass
    def create_report(self):
        pass

    

class Admin:
    def __init__(self):
        pass
    def get_input(self):
        self.doctorID = random.randint(10000,99999) # 5 digit uniq id
        fname = input('First name: ')
        lname = input('Last name: ')
        self.name = fname + ' ' + lname
        self.email = input('Email: ')
        self.phone = input('phone: ')
        self.password = input('Set Password: ')

    def create(self):
        print('inside patient create')
        self.get_input()
        conn = sqlite3.connect('test.db')
        conn.execute('''create table if not exists ADMIN
         (ADMIN_ID    INT     PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         EMAIL          TEXT    NOT NULL,
         PHONE        TEXT,
         PASSWORD       TEXT);''')
        
        insert_q = '''insert into ADMIN values (?,?,?,?,?)'''
        insert_tup = (self.adminID,self.name,self.email,self.phone,self.password)
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
        
        print('inside user menu')
        while 1:
            print('\n1 view patient\n2 view history\n3 view schedule\n4 create report\n0 logout')
            c = int(input('>'))
            if c == 0:
                return
                #break
            elif c == 1:
                self.view_patient()
            elif c == 2:
                self.view_history()
            elif c == 3:
                self.view_schedule()
            elif c == 4:
                self.create_report()
            else:
                print("*invalid input*")
        
    def view_patient(self):
        pass
    def view_history(self):
        pass
    def view_schedule(self):
        pass
    def create_report(self):
        pass




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
                time.sleep(2)
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
                time.sleep(2)
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
                time.sleep(2)
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
        time.sleep(5)
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