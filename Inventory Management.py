import os    #to create folder and access files
import random
import mysql.connector
import datetime
now = datetime.datetime.now()




def product_mgmt():    #Menu for product mngmt
    while True:
        print()
        print('\t'*3," ▓▓▓▓▓ PRODUCT MANAGEMENT ▓▓▓▓▓")
        print()
        print()
        print("\t\t\t 1. Add New Product")
        print("\t\t\t 2. Search Product")
        print("\t\t\t 3. Update Product")
        print("\t\t\t 4. Delete Product")
        print("\t\t\t 5. Back (Main Menu)")
        print()
        ch=int(input("\t\t Enter Your Choice : "))

        if ch==1:
            add_product()
        if ch==2:
            search_product()
        if ch==3:
            update_product()
        if ch==4:
            delete_product()
        if ch==5:
            break

def add_product():     #to add new product
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql = ("INSERT INTO product(pcode,pname,price,pqty,pcat) values(%s,%s,%s,%s,%s)")
    code = int(input("\t\t Enter product code : "))
    search = ("SELECT count(*) FROM product WHERE pcode=%s;")
    val = (code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt = x[0]
        if cnt == 0:
            name = input("\t\t Enter product name : ")
            qty = int(input("\t\t Enter product quantity : "))
            price = float(input("\t\t Enter product unit price : "))
            cat = input("\t\t Enter Product category : ")
            val = (code,name,price,qty,cat)
            mycursor.execute(sql,val)
            mydb.commit()
        else:
            print("\t\t Product already exist")

def search_product():   #to search for a product
    while True:
        print()
        print()
        print("\t\t\t 1. List all product")
        print("\t\t\t 2. List product code wise")
        print("\t\t\t 3. List product category wise")
        print("\t\t\t 4. Back (Main Menu)")
        s = int(input("\t\t Enter Your Choice :"))
        if s == 1:
            list_product()
        if s == 2:
            code=int(input(" Enter product code : "))
            list_prcode(code)
        if s == 3:
            list_prcat()
        if s == 4:
            break


def list_product():  #list of all products
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql = ("SELECT * from product")
    mycursor.execute(sql)
    print("\t\t\t\t\t\tPRODUCT DETAILS")
    print("\t\t", "_" * 85)
    print("\t\t Code\t Name \t\t\t\tPrice \t\tQuantity  \tCategory")
    print("\t\t", "_" *85)
    print()
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t\t", i[2], "\t", i[3], "\t\t", i[4])
        print("\t\t", "-" * 85)

def list_prcode(code):   #list of products based on code
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql=("SELECT * from product WHERE pcode=%s")
    val= (code,)
    mycursor.execute(sql, val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t", "-" * 80)
    print("\t\t Code\t Name\t\t\t Price\t\t Quantity \tCategory")
    print("\t\t", "-" * 80)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
        print("\t\t", "-" * 80)

def list_prcat():   #list of all products based on category
    print("List of all categories : ")
    print("1. CLOTHING")
    print("2. FOOTWEAR")
    print('3. JEWELLERY')
    print('4. STATIONERY')
    print('5. ELECTRONICS')
    print('4. COSMETICS')
    print('5. BOOKS')
    print('6. SPORTS')
    print("7. HEALTHCARE")
    print("8. GROCERY")
    print("9. KITCHEN")
    
    cat=input("Enter Category to be searched : ")
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    print(cat)
    sql=("SELECT * from product WHERE pcat =%s")
    val = (cat,)       
    mycursor.execute(sql, val)
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t", "-" * 80)
    print("\t\t Code  \tName \t\t\tPrice \t\tQuantity \tCategory")
    print("\t\t", "-" * 80)
    for i in mycursor:
        print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
        print("\t\t", "-" * 80)




def update_product():   #to update record of a product
    while True:
        mydb=mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
        mycursor = mydb.cursor()
        print("1.Update product price.")
        print("2.Update product quantity.")
        print("3.Back")
        ch=int(input("enter choice : "))
        print()
        if ch==1:
            update_price()
        if ch==2:
            update_qty()
        if ch==3:
            break

def update_price():  #update price of product
    mydb=mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    print()
    code = int(input("Enter the product code : "))
    p=int(input("Enter price : "))
    sql=("UPDATE product SET price=%s WHERE pcode=%s;")
    val=(p,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print()
    print("RECORD UPDATED.☺")
    print()
    print("-" * 85)


def update_qty():   #update quantity of product
    mydb=mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    print()
    code = int(input("Enter the product code : "))
    qty= int(input("Enter new quantity : "))
    sql=("UPDATE product SET pqty=%s WHERE pcode=%s;")
    val = (qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print()
    print("RECORD UPDATED.☺")
    print()
    print("-" * 85)



def delete_product():  #delete a product
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor=mydb.cursor()
    code=int(input("Enter the product code : "))
    sql=("DELETE FROM product WHERE pcode = %s;")
    val= (code,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount,"record(s) deleted");


def purchase_mgmt():  #menu of purchase mngmt
    print('\t'*3,"▓▓▓▓▓ PRURCHASE MANAGEMENT ▓▓▓▓▓")
    while True:
        print()
        print()
        print("\t\t\t 1. Add Order")
        print("\t\t\t 2. List Order")
        print("\t\t\t 3. Back (Main Menu)")
        ch=int(input("\t\t Enter Your Choice : "))
        if ch==1:
            add_order()
        if ch==2:
            list_order()
        if ch==3:
            break



def add_order():   #to add an order
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    code=int(input('enter code : '))
    list_prcode(code)
    now = datetime.datetime.now()   #main
    sql = ("INSERT INTO orders (orderid, orderdate, pcode,pprice, pqty, pcat) values(%s,%s,%s,%s,%s,%s)")
    code = int(input("Enter product code : "))
    oid = now.year+now.month+now.day+now.hour+now.minute+now.second   
    qty = int(input("Enter product quantity : "))
    price = float(input("Enter Product unit price: "))
    cat = input("Enter product category: ")
    val = (oid, now, code, price, qty, cat)
    mycursor.execute(sql, val)
    mydb.commit()

def list_order():   #list of all orders

    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql = ("SELECT * from orders")
    mycursor.execute(sql)
    print("\t\t\t\t\t ORDER DETAILS")
    print("-"*115)
    print("Orderid \t Date \t\tProductcode \tPrice \t\tQuantity \tCategory")
    print("-" * 115)
    for i in mycursor:
        print(i[0], "\t\t", i[1], "\t", i[2], "\t\t", i[3], "\t", i[4], "\t\t", i[5])
        print("-" * 115)




def sales_mgmt( ):   #menu for sales mngmt
    print('\t'*3,"▓▓▓▓▓ SALES MANAGEMENT ▓▓▓▓▓")
    while True:
        print()
        print()
        print("\t\t\t 1. Sale Items")
        print("\t\t\t 2. List Sales")
        print("\t\t\t 3. Back (Main Menu)")
        ch=int (input("\t\t Enter Your Choice : "))
        if ch== 1:
            sale_product()
        if ch== 2:
            list_sale()
        if ch== 3:
            break     #INVENTORY OPT 1 UNDER MAIN MENU

def sale_product():   #to add sales of product
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    pcode = input("Enter product code: ")
    sql= ("SELECT count(*) from product WHERE pcode=%s;") #counting no. of records of the code 
    val= (pcode,)                                       #inserting code
    mycursor.execute(sql,val)
    for x in mycursor:  #result set is count of products available (with the same pcode)
        cnt = x[0]   #no of records
        if cnt!= 0 :  #checks if records are 0 (rows)
            sql=("SELECT * from product WHERE pcode=%s;")
            val= (pcode,)  #tuple
            mycursor.execute(sql, val)
            print("\t\t", "_" * 85)
            print("\t\t Code\t Name \t\t\t\tPrice \t\tQuantity  \tCategory")
            print("\t\t", "_" *85)
            print()
            for i in mycursor:
                print("\t\t", i[0], "\t", i[1], "\t\t", i[2], "\t", i[3], "\t\t", i[4])
                print("\t\t", "-" * 85)
                price= int(i[2])
                pqty = int(i[3])
                qty = int(input("Enter quantity :"))
                if qty <= pqty:
                    total = qty * price
                    print("Collect Rs. ", total)
                    sql = ("INSERT into sales values(%s,%s,%s,%s,%s,%s)")   #inserting total qty sold in table sales
                    val = (int(pcode)+1,datetime.datetime.now(),pcode,price,qty,total)   #gives current date and time  #pcode+1 is generating a new sales id
                    mycursor.execute(sql,val)
                    sql =("UPDATE product SET pqty=pqty-%s WHERE pcode=%s")    #updating number of products in table product
                    val = (qty, pcode)
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    print("Quantity not available")
        else:
            print("Product is not available")


def list_sale():  #list of all sales
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql = ("SELECT * FROM sales")
    mycursor.execute(sql)
    print("\t\t\t\t SALES DETAILS")
    print("_" * 90)
    print("SalesID \t Date \t\tProductCode \t Price \t\t Quantity \tTotal")
    print("_" * 90)
    for x in mycursor:
        print(x[0], "\t\t", x[1], "\t", x[2], "\t\t", x[3], "\t", x[4], "\t\t", x[5])
        print("-" * 90)

    
    


def db_mgmt( ):  #creation of database
    while True:
        print()
        print()
        print("\t\t\t 1. Database creation")
        print("\t\t\t 2. List Database")
        print("\t\t\t 3. Back (Main Menu)")
        ch = int(input("\t\t Enter Your Choice : "))
        if ch== 1:
            create_tables()
        if ch== 2:
            list_tables()
        if ch== 3:
            break

def create_tables():  #creation of tables
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    print(" Creating PRODUCT table")   #creating table product
    sql=("CREATE TABLE if not exists product(pcode int(4) PRIMARY KEY,pname char(30) NOT NULL,price float(8,2),pqty int(4),pcat char(30))")
    mycursor.execute(sql)
    print("Creating ORDER table")

    sql=("CREATE TABLE if not exists orders(orderid int(4)PRIMARY KEY,orderdate DATE,pcode char(30) NOT NULL ,pprice float(8,2),pqty int(4),supplier char(50),pcat char(30))")
    mycursor.execute(sql)
    print("ORDER table created")

    print("Creating SALES table")
    sql=("CREATE TABLE if not exists sales(salesid int(4) PRIMARY KEY,salesdate DATE,pcode char(30) references product(pcode),pprice float(8,2),pqty int(4),Total double(8,2))")
    mycursor.execute(sql)
    print("SALES table created")

    attendence()
    print("ATTENDENCE table created")




def list_tables():  #list of all tables
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456",database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql = ("show tables")
    mycursor.execute(sql)
    for i in mycursor:
        print(i)



def ATTENDENCE_MAIN():#main 2
    while True:
        print()
        print()
        print("\t1. Mark attendence")
        print("\t2. Display attendence")
        print("\t3. Back")
        ch=int(input("\tEnter your choice : "))
        if ch==1:
            update_attendence()
        if ch==2:
            display_attendence()
        if ch==3:
            break

def attendence():  #creating attendence table
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    mycursor = mydb.cursor()
    sql=("CREATE TABLE if not exists EMP1_attendence(empcode int(4) PRIMARY KEY, empname char(40), status char(10), dt DATETIME)")
    mycursor.execute(sql)
    print("Creating ATTENDENCDE table....")
    print("Table successfully created")

def update_attendence():  #to update attendence table
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    cursor = mydb.cursor()
    ecode=int(input('Enter user id : '))
    ename=input("Enter name: ")
    status='present'
    now = datetime.datetime.now()
    sql=('insert into emp1_attendence(empcode,empname,status,dt) values(%s,%s,%s,%s)')
    val=(ecode,ename,status,now)
    cursor.execute(sql,val)
    print()
    print("Attendence marked")
    print()
    mydb.commit()

def display_attendence():  #display of all attendence
    mydb = mysql.connector.connect(host="localhost", user="root",password="123456", database="stock",auth_plugin='mysql_native_password',charset='utf8')
    cursor = mydb.cursor()
    cursor.execute("select empcode,empname, IFNULL(status,'NA'), IFNULL(dt,'NA') from EMP1_attendence")
    result=cursor.fetchall()
    print('_'*80)
    print("CODE\t NAME \t\t STATUS \t DATE AND TIME")
    print('_'*80)
    for X in result:
        print(X[0],'\t',X[1],'\t\t',X[2],'\t',X[3])   #display with columns, use date time
        print( "-" * 80)


def MNGT():    #main list of all management systems
    print("\n"*2)
    while True:
        print()
        print()
        print('*' * 85)
        print("\t\t\t\t STOCK MANAGEMENT")
        print('*' * 85,"\n")
        print("\t 1. PRODUCT MANAGEMENT")
        print("\t 2. PURCHASE MANAGEMENT")
        print("\t 3. SALES MANAGEMENT")
        print("\t 4. DATABASE SETUP")
        print("\t 5. BACK(MAIN MENU)")
        print("\t 6. EXIT\n")
        ch=int(input("Enter your choice : "))
        if ch==1:
            product_mgmt()
        if ch==2:
            os.system('cls')
            purchase_mgmt()
        if ch==3:
            sales_mgmt()
        if ch==4:
            db_mgmt()
        if ch==5:
            break
        if ch==6:
            exit()





    

def MAIN_MENU():
    while True:
        print()
        print()
        print("█"*88)
        print()
        print("\t\t\t\t\t\t\t MAIN MENU")
        print()
        print("█"*88)
        print()
        print("\t1. STOCK MANAGEMENT")
        print("\t2. ATTENDANCE")
        print("\t3. BACK")
        ch=int(input("\tEnter your choice : "))
        if ch==1:
            MNGT()
        if ch==2:
            ATTENDENCE_MAIN()
        if ch==3:
            LOGIN()


def enter_user():
    f=open('user1.txt','a')
    uid=random.randint(100,999)
    nm=input('Enter username : ')
    pswd=input('Enter password : ')
    f.write(str(uid))
    f.write('\t')
    f.write(nm)
    f.write('\t')
    f.write(pswd)
    f.write('\n')
    f.close()
    print("Your personal user id is : ", uid)
    print()
    print()
    print("****************************************************************************************")
    print("*                                                                                      *")
    print("*                           WELCOME  TO  THE  TEAM!!                                   *")
    print("*  We're delighted that you have joined K-MART. We look forward to working with you! ☺ *")
    print("*                                                                                      *")
    print("****************************************************************************************")
    LOGIN()
    


def check_pswd():
    f=open('user1.txt','r')
    ans='y'
    data=f.readlines()
    while ans=='y':
        uid=input('Enter your id : ')
        pswd=input('Enter your password : ')
        for i in data:
            lst=list(i.split())
            if uid==lst[0]:
                if pswd==lst[2]:
                    MAIN_MENU()
                    ans='n'
                else:
                    print()
                    print('Incorrect password, Try again.')
                    print()
                    ans='y'
                

def LOGIN():
    print()
    print()
    print()
    print()
    print("▓"*88)
    print()
    print("\t\t\t\t\t\tWELCOME TO K-MART INVENTORY MANAGEMENT")
    print()
    print("▓"*88)
    print()
    print()
    print("1. Login")
    print("2. Sign Up")
    print("3. Exit")
    print()
    ch=int(input('enter choice : '))
    if (ch==1):
        check_pswd()
    if (ch==2):
        enter_user()
    if (ch==3):
        exit()
LOGIN()
