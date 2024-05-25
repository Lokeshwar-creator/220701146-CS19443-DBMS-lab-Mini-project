Hospital management system source code in PYTHON IDE
PROGRAM:

import random
import mysql.connector as a
con = a.connect(host="localhost",user="root",passwd="Lokeshwar2004",database="hos")
c = con.cursor()
doc_id=["9854","4356","8709","9865","9855","4214","2854","7721","3211","3290"]
staff_id=["1311","3490","5263","1119","0678"]

def mainmenu():
    print("Main menu----\n 1.Patient\n 2.Doctor\n 3.Staff\n 4.Know more\n")
    ans = input("Choose an Option Number: ")
    if ans == "1":
        patient()
    elif ans == "2":
        doctor()
    elif ans == "3":
        staff()
    elif ans == "4":
        print("GRC Hospital(since 2001) marks the beginning of a new genre of hospitals focused \nat bringing premium quality health care within the reach of people \nat an affordable costs We believe in delivering international standard \nas well as value for money.\n\n\033[1mWe are the care you can trust!")
    else:
        print("Enter a valid choice")
      
def patient():
    print("Patient----\n 1.Book an appointment\n 2.Book a bed\n 3.Find your best doctor\n 4.24 hrs ambulance\n 5.Cancel an appointment\n 6.Return to Main menu")
    ans = input("Choose an Option Number: ")
    if ans == "1":

       a1=  input("Enter Name: ")
       a2 = input("Enter Age: ")
       a3 = input("Enter Gender: ")
       print("The hospital's doctor list ---- ")
       print("--cardiology(CD)--\n9854|Dr.MOHITH\n4356|Dr.MANIKANDAN")
       print("--Neurology(NU)--\n8709|Dr.MERVIN\n9865|Dr.LOGESH")
       print("--Dermatology(DM)--\n9855|Dr.LITHAN\n4214|Dr.LALIT")
       print("--Surgery(SG)--\n2854|Dr.PRASHANTH\n7721|Dr.LOGESHWARAN")
       print("--Gastroentrology(GS)--\n3211|Dr.MUKESH \n3290|Dr.HARIVARSAN")
       a4 = input("Enter Doctor's ID you wanna appoint: ")
       z=0
       for i in range(len(doc_id)):
           if a4==doc_id[i]:
               z=1
               a5=  input("Enter your suitable date in YYYY-MM-DD format: ")
               a6=  input("Enter your contact no: ")
               a7 = uid()
               print("Your unique generated ID :", a7)
               print("\n\nCongratulations Your appointment has been booked!")
               data1=(a7,a1,a2,a3,a5,a6,a4)
               sql1="insert into patient values(%s,%s,%s,%s,%s,%s,%s)"
               c.execute(sql1,data1)
               con.commit()
               data2 =(a7,a1,a2,a4,a5,0,0)
               sql2 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
               c.execute(sql2, data2)
               con.commit()
       if z==0:
        print("Enter a valid doctor ID")
    elif ans == "2":
        print("Enter the general details----")
        a1 = input("Enter Name: ")
        a2 = input("Enter Age: ")
        a3 = input("Enter Gender: ")
        a4 = input("Enter Doctor's ID under which you want to take admission: ")
        z = 0
        for i in range(len(doc_id)):
            if a4 == doc_id[i]:
                z = 1

                a5 = input("Enter your suitable date you want to take admission in YYYY-MM-DD format: ")
                a7 = uid()
                print("Your unique generated ID :", a7)
                print("Book a bed----\n 1.General bed\n 2.ICU bed \n 3.Return to Main menu")
                ans = input("Choose an Option Number: ")
                if ans == "1":
                    a6="GEN"
                    data3 = (a7,a1, a2, a3, a4,a6, a5, 0)
                    sql3 = "insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    c.execute(sql3, data3)
                    con.commit()
                    data6=(a7,a1, a2, a4,a5,0,0)
                    sql6 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
                    c.execute(sql6,data6)
                    con.commit()
                    print("\n\nCongratulations Your General Bed has been booked!")

                elif ans == "2":
                    a6 = "ICU"
                    data3 = (a7,a1, a2, a3, a4,a6, a5, 0)
                    sql3 = "insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    c.execute(sql3, data3)
                    con.commit()
                    data6 = (a7, a1, a2, a4, a5, 0, 0)
                    sql6 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
                    c.execute(sql6, data6)
                    con.commit()
                    print("\n\nCongratulations Your ICU Bed has been booked!")
        if z==0:
            print("Enter a valid doctor ID")
        elif ans=="3":
            mainmenu()
    elif ans == "3":
            print("Find Your best doctor----\n 1.Cardiology(CD)\n 2.Neurology(NU)\n 3.Dermatology(DM)\n 4.Surgery(SG)\n 5.Gastroentrology(GS)")
            ans = input("Choose an department code: ")

            c.execute(f"select name from doc where dept='{ans}'")
            result = c.fetchall()
            for i in result:
                print("Dr. "+clean(i))
            con.commit()
    elif ans == "4":
        a1 = input("Enter Location: ")
        a2 = input("Enter contact number: ")
        data3 = (a1, a2)
        sql3 = "insert into emergency values(%s,%s)"
        c.execute(sql3, data3)
        con.commit()
        print("An ambulance will reach your location shortly")
    elif ans=='5':
        a1=input("Enter Your ID: ")
        a2=patient_check(a1)
        if a2==1:
            c.execute(f"DELETE FROM patient WHERE uid={a1}")
            con.commit()
            print("Your appointment is Cancelled! ")
        else:
            print("You do not have any appointments!")
    elif ans=='6':
        mainmenu()


    else:
         print("Enter a valid choice")
      
def uid():
    d=""
    for i in range(0, 4):
            n = random.randint(0,9)
            c = str(n)
            d += c
    return d

def staff():
    print("Staff----\n 1.Login with ID \n 2.Return to Main menu")
    ans = input("Choose an Option Number: ")
    if ans == "1":
        id=input("Enter your ID Number: ")
        r=0
        c.execute(f"select name from staff where ID={id}")
        result = c.fetchall()
        for i in result:
            print("Hi! ",clean(i))
        for i in range(len(staff_id)):
            if id==staff_id[i]:
                r = 1
                print("Login with ID ----\n 1.Show the bill of a patient \n 2.Show the emergency list \n 3.Book a bed for patient\n 4.Return to Main menu")
                ans=input("Choose an Option Number: ")
                if ans == "1":
                    pid=input("Enter the patient's ID Number: ")
                    c.execute(f"select bill from final where ID={pid}")
                    result = c.fetchall()
                    for i in result:
                        print(f"Net bill of patient with ID {pid}: ₹", clean(i))
                elif ans == "2":
                    c.execute("select * from emergency ")
                    result = c.fetchall()
                    print("('Location', 'Contact Number')")
                    for i in result:
                        print(i)
                elif ans=='3':
                    print("Enter the Patient's general details----")
                    a1 = input("Enter Patient's Name: ")
                    a2 = input("Enter Patient's Age: ")
                    a3 = input("Enter Patient's Gender: ")
                    a4 = input("Enter Doctor's ID under which the Patient want to take admission: ")
                    z = 0
                    for i in range(len(doc_id)):
                        if a4 == doc_id[i]:
                            z = 1
                            a5 = input("Enter your suitable date the Patient want to take admission in YYYY-MM-DD format: ")
                            a7 = uid()
                            print("Patient's unique generated ID :", a7)
                            print("Book a bed for patient----\n 1.General bed\n 2.ICU bed \n 3.Return to Main menu")
                            ans = input("Choose an Option Number: ")
                            if ans == "1":
                                a6 = "GEN"
                                data3 = (a7, a1, a2, a3, a4, a6, a5, 0)
                                sql3 = "insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                c.execute(sql3, data3)
                                con.commit()
                                data6 = (a7, a1, a2, a4, a5, 0, 0)
                                sql6 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
                                c.execute(sql6, data6)
                                con.commit()
                                print("\n\nCongratulations Patient's General Bed has been booked!")

                            elif ans == "2":
                                a6 = "ICU"
                                data3 = (a7, a1, a2, a3, a4, a6, a5, 0)
                                sql3 = "insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                c.execute(sql3, data3)
                                con.commit()
                                data6 = (a7, a1, a2, a4, a5, 0, 0)
                                sql6 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
                                c.execute(sql6, data6)
                                con.commit()
                                print("\n\nCongratulations Patient's ICU Bed has been booked!")
                    if z==0:
                        print("Enter a valid Doctor ID")

                elif ans=='4':
                    mainmenu()
                else:
                    print("Enter a valid choice")
        if r==0:
            print("Enter a valid ID")
    elif ans=='2':
        mainmenu()
    else:
        print("Enter a valid choice")


def doctor():
    print("Doctor----\n 1.Login with ID \n 2.Return to Main menu")
    ans = input("Choose an Option Number: ")
    if ans == "1":
        id=input("Enter your ID Number: ")
        r=0
        for i in range(len(doc_id)):
            if id==doc_id[i]:
                r = 1
                c.execute(f"select name from doc where ID={id}")
                result = c.fetchall()
                for i in result:
                    print("Hi! Dr.", clean(i))
                print("Login with ID ----\n 1.Show my appointments \n 2.Discharge a patient \n 3.Update my opd list \n 4.Return to Main menu")
                ans = input("Choose an Option Number: ")
                if ans == "1":

                 print("Hello doctor, your today's OPD appointments are----")
                 c.execute(f"select name,uid from patient where dr={id}")
                 result=c.fetchall()
                 for i in result:
                    print(clean(i))

                 print("And, your today's patients in hospitals are----")
                 c.execute(f"select name,ID from admission where dr={id}")
                 result = c.fetchall()
                 for i in result:
                    print(clean(i))
                 con.commit()
                elif ans == "2":
                    print("Your all inhospital patients along with their ID----")
                    c.execute(f"select name,ID from admission where dr={id}")
                    result = c.fetchall()
                    for i in result:
                        print(clean(i))
                    a1=input("Enter the id of the patient you want to discharge : ")
                    c.execute(f"select incoming_date from final where ID={a1}")
                    result = c.fetchall()
                    for i in result:
                        print("your patient was admitted on",clean(i))
                    a22=input("Enter the no of days he was in the hospital under you: ")
                    c.execute(f"select bed_type from admission where ID={a1}")
                    result = c.fetchall()
                    for i in result:
                        bd=clean(i)

                    if (bd == 'GEN'):
                        bl = (4500+2000+1000)*int(a22)

                        c.execute(f"update final set bill={bl} where ID={a1}")
                        con.commit()
                    elif (bd == 'ICU'):
                        bl = (7500+3000 +1500)*int(a22)
                        c.execute(f"update final set bill={bl} where ID={a1}")
                        con.commit()

                    c.execute(f"DELETE FROM admission WHERE ID={a1}")
                    c.execute(f"update final set days={a22} where ID={a1}")
                    con.commit()


                    print("Discharged Successfully")
                elif ans == "3":
                    a1 = input("Enter the id of the patient you have checked : ")
                    c.execute(f"DELETE FROM patient WHERE uid={a1}")
                    con.commit()
                    print("Your patient list Updated!")
                elif ans=="4":
                    mainmenu()
                else:
                    print("Enter a valid choice")

        if(r==0):
            print("Enter valid ID")
    elif ans == "2":
        mainmenu()
    else:
        print("Enter a valid choice")
      
def clean(str1):
    str2=""
    for i in range (len(str1)):
        if str1[i]!="'" and str1[i]!="(" and str1[i]!=")" and str1[i]!=",":
            str2=str2+str1[i]
    return str2
  
def patient_check(str1):
    c.execute("select uid FROM patient")
    result=c.fetchall()
    result1=[]
    for i in result:

        result1.append(clean(i))
    z=0
    for i in range(len(result1)):
        if str1==result1[i]:
            z=1
    con.commit()
    return z

mainmenu()
