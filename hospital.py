import sqlite3,time
from tabulate import tabulate
con=sqlite3.connect('hospitall.db')#database name

class hospital:



    def disp(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                  WELCOME TO HOSPITAL ADMIN DESK                          *")
        print("*                                                                          *")
        print("*                        CODE BY VISHWA                                    *")
        print("*                                                                          *")
        print("****************************************************************************")
        print("")
        #time.sleep(1)
    def menu(self):
        print("\t\t\t|-------MENU--------|")
        print("\t\t\t|1.Appoinment       |")
        print("\t\t\t|                   |")
        print("\t\t\t|2.Patient details  |")
        print("\t\t\t|                   |")
        print("\t\t\t|3.Doctor details   |")
        print("\t\t\t|                   |")
        print("\t\t\t|4.Staff details    |")
        print("\t\t\t|                   |")
        print("\t\t\t|5.Hospital details |")
        print("\t\t\t|                   |")
        print("\t\t\t|6.About us         |")
        print("\t\t\t|                   |")
        print("\t\t\t|7.Exit             |")
        print("\t\t\t|                   |")
        print("\t\t\t|-------------------|")
        opt=int(input("Enter any options:"))
        if opt==1:
            obj.apt()
        elif opt==2:
            obj.patient()
        elif opt==3:
            obj.doctor()
        elif opt==4:
            obj.staff()
        elif opt==5:
            obj.hosp()
        elif opt==6:
            obj.abt()
        elif opt==7:
            print("*********************THANK YOU**********COME AGAIN******************************")
            exit()
        else:
            print("invalid option")

    def apt(self):
    
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        gender=input("Enter your gender:")
        contact=int(input("Enter your contact:"))
        address=input("Enter your adress:")
        cause=input("what disease:")
        qry="insert into pat (NAME,AGE,GENDER,CONTACT,ADDRESS,DISEASE) values (?,?,?,?,?,?);"
        con.execute(qry,(name,age,gender,contact,address,cause))
        con.commit()
        time.sleep(1)
        print("your appointment was booked")
        print("you may come tommorrow")
    def patient(self):
        result=con.cursor()
        qry="select * from pat;"
        result.execute(qry)
        result2=result.fetchall()
        print(tabulate(result2,headers=["ID","NAME","AGE","GENDER","CONTACT","ADDRESS","DISEASE"]))
    def doctor(self):
        result=con.cursor()
        qry="select * from doct;"
        result.execute(qry)
        result2=result.fetchall()
        print(tabulate(result2,headers=["id","name","age","gender","specialization","contact","address"]))
    def staff(self):
        result=con.cursor()
        qry="select * from staff;"
        result.execute(qry)
        result2=result.fetchall()
        print(tabulate(result2,headers=["id","name","age","gender","job","contact","address"]))
    def hosp(self):
        print("")
        print(">>>>>>>>>>>>>>>>>>HOSPITAL DETAILS<<<<<<<<<<<<<<<<<<<<<")
        print("")
        print("(Equipments)--------------------------------(Available pieces)")
        print("")
        print("  Hospital Stretchers--------------------------100 ")
        print("  Defribrillators------------------------------50")
        print("  Anesthesia Machines--------------------------35")
        print("  Patient Monitors-----------------------------90")
        print("  Sterilizers----------------------------------70")
        print("  EKG/ECG Machines-----------------------------20")
        print("  Surgical Tables------------------------------60")
        print("  Fluid Warmers--------------------------------10")
        print("  Electrosurgical Units------------------------40")
        print("  Surgical lights------------------------------120")
        print("")

    def abt(self):
        print("->this hospital was founded in 2003 ")
        print("->This hospital is the multi speciality health care provider with 16 health care facilities 8 cities across 6 states")
        print("->we have latest eqipments and experienced doctors")
        print("->largest private sector hospital in india")
        print("->150 renowed super specialities")
        print("->350 medical experts")
        print("->contact:04366-234567")
    
                  
obj=hospital()
obj.disp()
obj.menu()
check=0
while check==0:
    print("--------------------------------------------------------------------------------")
    print("1.back")
    print("2.quit")
    dumm=int(input("enter your choice:"))
    if dumm==1:
        obj.menu()
    else:
        print("*********************THANK YOU**********COME AGAIN******************************")
        check=1
