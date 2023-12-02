import mysql.connector
mydb=mysql.connector.connect(host='local host',user=root,database='bms')
def open_account():
    name=input("enter your name:")
    acc=input("enter your acc no:")
    dob=input("enter your dob:")
    add=input("enter your address:")
    con=input("enter your contact:")
    op_bal=int(input("enter your opening balance:"))
    data1=(name,acc,dob,add,con,op_bal)
    data2=(name,acc,op_bal)

    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values (%s,%s,%s,%s)')

    x=mydb.cursor()

    x.execute(sql1,data1)
    x.execute(sql2,data2)

    mydb.commit()
    print("data entered successfully")
    main()
def deposit():
    amount=input("enter the ampount to deposit:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc_no=%s"
    data1=(acc,)
    x=mydb.cursor()
    x.execute (a,data1)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance where acc_no=%s')
    d=(t,acc)
    x.executed (sql,d)
    mydb.commit()
    print("................")
    main()

def withdraw():
    amount=input("enter the amount to withdraw:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc_no=%s"
    data1=(acc,)
    x=mydb.cursor()
    x.execute (a,data1)
    result=x.fetchone()
    t=result[0]-amount
    sql=('update amount set balance where acc_no=%s')
    d=(t,acc)
    x.executed (sql,d)
    mydb.commit()
    print(".................")
    main()
def balance():
    ac=input("enter the account number:")
    a="select *from amount where acc_no=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    mydb.commit()
def main():
    print("""
1.open new account
2.deposit amount
3.withraw amount
4.balance enquiry
5.show customer details
6.close on acount
""")
    c=int(input("choose your option:"))
    if (c==1):
        print("open new account")
        main()
    elif(c==2):
        print("deposit amount")
        main()
    elif(c==3):
        print("withdraw amount")
        main()
    elif(c==4):
        print("balance enquiry")
        main()
    elif(c==5):
        print("show customer details")
        main()
    elif(c==6):
        print("close on account")
        main()
    else:
        print("enter the valid number")
        main()
main()          
