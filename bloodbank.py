import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='bloodbank')
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
    
        
        name=input("enter  name:::---")
        place=input("enter the place:::---")
        phone =input("enter the phone number:::---")
        bloodgroup=input("blood group:::---")
        sql="INSERT INTO `bloodbank`(`name`, `place`, `phone`, `bloodgroup`) VALUES (%s,%s,%s,%s)"
        data=(name,place,phone,bloodgroup)
        mycursor.execute(sql,data)
        mydb.commit()
        print("successfully added...........!")
    elif(choice==2):
        print("VIEW DETAILS")    
    elif(choice==3):
        print("SEARCH DETAILS")
    elif(choice==4):
        print("UPDATE DETAILS") 
    elif(choice==5) :
        print("DELETE DETAILS")
    elif(choice==6):
        break      