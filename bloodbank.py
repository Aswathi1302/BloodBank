import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bloodbank1')
mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print("--------------------------------")
    print("1. add details")
    print("2.view details")
    print("3.search details")
    print("4.upadte details")
    print("5. delete details")
    print("6.exit")
    print("--------------------------------")

    
    choice=int(input("enter your choice:-"))
    if(choice==1):
        print("*----ADD ITEM----*")
    
        
        donername=input("enter  name:::---")
        place=input("enter the place:::---")
        bloodgroup=input("blood group:::---")
        age =input("enter the age:::---")
        phone =input("enter the phone number:::---")
        sql="INSERT INTO `bloodbank` (`donername`, `place`, `bloodgroup`, `age`, `phone`) VALUES (%s,%s,%s,%s,%s)"
        data=(donername,place,bloodgroup,age,phone)
        mycursor.execute(sql,data)
        mydb.commit()
        print("successfully added...........!")
    elif(choice==2):
        print("VIEW DETAILS")  
        sql="SELECT * FROM `bloodbank`"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)  
    elif(choice==3):
        print("SEARCH DETAILS")
    elif(choice==4):
        print("UPDATE DETAILS") 
    elif(choice==5) :
        print("DELETE DETAILS")
    elif(choice==6):
        break      