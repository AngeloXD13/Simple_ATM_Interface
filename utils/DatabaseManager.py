import sqlite3

from utils.AccountDATA import Account

del Account
class DatabaseManagerClass():
    def __init__(self):
        super(DatabaseManagerClass, self).__init__()
        print("INIT DATABASE")
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        global globalself
        globalself = self
        print("Opened database successfully")


    def insertData(self, fname, mname, lname, birthday, address, typeofid, idnumber, email, phonenumber, accountstatus, availbalance, onholdbalance, pinnumber):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()
        sql = ("INSERT INTO ACCOUNT(FNAME, MNAME, LNAME, BIRTHDAY, ADDRESS, TYPEOFID, IDNUMBER, EMAIL, PHONENUMBER, ACCOUNTSTATUS, AVAILBALANCE, ONHOLDBALANCE, PINNUMBER) VALUES( '" + fname + "', '" + mname + "',  '" + lname + "', '" + str(
                birthday) + "', '" + address + "', '" + typeofid + "','" + idnumber + "', '" + email + "', '" + phonenumber + "', '" + accountstatus + "', '" + str(
                availbalance) + "', '" + str(onholdbalance) + "', '" + pinnumber + "');")
        # try:
        print(sql)

        self.conn.execute(sql)
        print("Records created successfully!")
        self.conn.commit()
        self.conn.close()

def selectData(phoneNumber, action):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = "SELECT * FROM ACCOUNT WHERE PHONENUMBER = '" + phoneNumber + "';"
    print(sql)
    c.execute(sql)

    if action == 1:
        # action 1: only password will be returned
        account = None
        account = getPassword(c)
        return account
    elif action == 2:
        # action 2: all data will returned
        account = None
        account = getAllData(c)
        print("selectData: ", account.fname)
        return account
    elif action == 3:
        # action 3: check if phonenumber is Existing
        result = getOtherData(c)
        return result

def createTable(self):

    sql = ("CREATE TABLE IF NOT EXISTS 'ACCOUNT'("
    "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
    "FNAME TEXT NOT NULL, "
    "MNAME TEXT NOT NULL, "
    "LNAME TEXT NOT NULL, "
    "BIRTHDAY TEXT NOT NULL, "
    "ADDRESS TEXT NOT NULL, "    #full address {lothouse,barangay,citymuni,provice,zipcode}
    "TYPEOFID TEXT NOT NULL, "
    "IDNUMBER TEXT NOT NULL, "
    "EMAIL TEXT NOT NULL, "
    "PHONENUMBER TEXT NOT NULL UNIQUE, "
    "ACCOUNTSTATUS TEXT NOT NULL, "
    "AVAILBALANCE INTEGER DEFAULT 0, "
    "ONHOLDBALANCE INTEGER DEFAULT 0, "
    "PINNUMBER TEXT NOT NULL );")

    print(sql)

    try:
        self.conn.execute(sql)
        self.conn.commit()
        print("Table created successfully")
    except:
        print("Table creation error")

    self.conn.close()

def getPassword(c):
    from utils.AccountDATA import Account
#    Account = None
    print("GETPASS")
    pass_account = None
    pass_account = Account
    #del pass_account
    items = None
    items = c.fetchall()
    if items == []:
        print("no ITEMS DETECTED")
    else:
        print("intems",items)
        for item in items:
            pass_account.pin = None
            pass_account.pin = item[13]
            print(" pass_account.pin: ",pass_account.pin)
        return pass_account

def getAllData(c):
    from utils.AccountDATA import Account
    alldata_account = None
    alldata_account = Account
    items = None
    items = c.fetchall()
    if items == []:
        print("no ITEMS DETECTED")
    else:
        for item in items:
            alldata_account.fname = item[1]
            alldata_account.lname = item[3]
            alldata_account.phonenumber = item[9]
            alldata_account.status = item[10]
            alldata_account.availablebalance = item[11]
            alldata_account.onholdbalance = item[12]
            alldata_account.pin = item[13]

        print("getalldata: ", alldata_account.fname)
        return alldata_account

def getOtherData(c):
    items = None
    items = c.fetchone()
    print(items)
    if items == None:
        print("no ITEMS DETECTED")
        return False
    else:
        print("Items DEtected")
        return True

def updateAvailBalance(phoneNumber, newAvailBalance):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = ("UPDATE ACCOUNT SET AVAILBALANCE = '" + str(newAvailBalance) + "' WHERE PHONENUMBER = '" + phoneNumber + "'")
    print(sql)
    try:
        c.execute(sql)
        print("Update Avail BALANCE sucess")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        print("Update Avail BALANCE fail")
        conn.close()
        return False

def updateonHoldBalance(phoneNumber, newonHoldBalance):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = ("UPDATE ACCOUNT SET ONHOLDBALANCE = '" + str(newonHoldBalance) + "' WHERE PHONENUMBER = '" + phoneNumber + "'")
    print(sql)
    try:
        c.execute(sql)
        print("Update hold BALANCE sucess")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        print("Update hold BALANCE fail", error)
        conn.close()
        return False

def updatePinPassword(phoneNumber, newPinPass):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = ("UPDATE ACCOUNT SET PINNUMBER = '" + str(newPinPass) + "' WHERE PHONENUMBER = '" + phoneNumber + "'")
    print(sql)
    try:
        c.execute(sql)
        print("Update Avail PINNUMBER sucess")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        print("Update Avail PINNUMBER fail")
        conn.close()
        return False

def setAccountStatus(phoneNumber, status):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = ("UPDATE ACCOUNT SET ACCOUNTSTATUS = '" + str(status) + "' WHERE PHONENUMBER = '" + phoneNumber + "'")
    print(sql)
    try:
        c.execute(sql)
        print("Update Avail ACCOUNTSTATUS sucess")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        print("Update Avail ACCOUNTSTATUS fail")
        conn.close()
        return False

def updateAvailHoldBalance(phoneNumber, newHoldbalance, newAvailable):
    conn = None
    conn = sqlite3.connect('test.db')
    c = None
    c = conn.cursor()
    sql = ("UPDATE ACCOUNT SET ONHOLDBALANCE = '" + str(newHoldbalance) + "', AVAILBALANCE = '" + str(newAvailable) + "' WHERE PHONENUMBER = '" + phoneNumber + "'")
    print(sql)
    try:
        c.execute(sql)
        print("Update Avail PINNUMBER sucess")
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as error:
        print("Update Avail PINNUMBER fail")
        conn.close()
        return False
