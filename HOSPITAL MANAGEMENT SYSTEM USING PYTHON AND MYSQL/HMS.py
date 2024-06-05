HOSPITAL MANAGEMENT SYSTEM USING PYTHON AND MYSQL
PYTHON IDLE CODE
PROGRAM:

import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="Lokeshwar2004", database="hos")
c = con.cursor()

doc_id = ["9854", "4356", "8709", "9865", "9855", "4214", "2854", "7721", "3211", "3290"]
staff_id = ["1311", "3490", "5263", "1119", "0678"]

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GRC Hospital")
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        tk.Label(self.root, text="------------WELCOME TO GRC HOSPITAL------------").pack()
        tk.Label(self.root, text="Main menu----").pack()
        tk.Button(self.root, text="1. Patient", command=self.patient_menu).pack()
        tk.Button(self.root, text="2. Doctor", command=self.doctor_menu).pack()
        tk.Button(self.root, text="3. Staff", command=self.staff_menu).pack()
        tk.Button(self.root, text="4. Know more", command=self.know_more).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def know_more(self):
        message = (
    "GRC Hospital, established in 2001, is committed to delivering premium quality healthcare within reach of everyone at affordable costs. "
    "Our mission is to provide international standard care combined with exceptional value for money. "
    "With a team of highly qualified doctors, state-of-the-art facilities, and compassionate staff, we ensure the best possible treatment and comfort for our patients.\n\n"
    "At GRC Hospital, we believe in the care you can trust. We offer a wide range of medical services, including cardiology, neurology, dermatology, surgery, and gastroenterology, supported by advanced diagnostic and therapeutic technologies. "
    "Our 24-hour emergency services and ambulance facilities ensure that help is always available when you need it the most.\n\n"
    "GRC Hospital is not just about treatment; it’s about creating a nurturing environment where patients and their families feel supported and confident in their care journey. "
    "Our patient-centric approach ensures personalized treatment plans tailored to individual needs.\n\n"
    "Explore our specialized departments and find the best healthcare professionals dedicated to improving your health and well-being. With GRC Hospital, you are in safe hands.")
        messagebox.showinfo("ABOUT GRC ",message)

    def patient_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Patient----").pack()
        tk.Button(self.root, text="1. Book an appointment", command=self.book_appointment).pack()
        tk.Button(self.root, text="2. Book a bed", command=self.book_bed).pack()
        tk.Button(self.root, text="3. Find your best doctor", command=self.find_best_doctor).pack()
        tk.Button(self.root, text="4. 24 hrs ambulance", command=self.book_ambulance).pack()
        tk.Button(self.root, text="5. Cancel an appointment", command=self.cancel_appointment).pack()
        tk.Button(self.root, text="6. Return to Main menu", command=self.main_menu).pack()

    def book_appointment(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        age = simpledialog.askstring("Input", "Enter Age:")
        gender = simpledialog.askstring("Input", "Enter Gender:")
        doctor_id = simpledialog.askstring("Input", "Enter Doctor's ID you wanna appoint:")
        
        if doctor_id not in doc_id:
            messagebox.showerror("Error", "Enter a valid doctor ID")
            return

        date = simpledialog.askstring("Input", "Enter your suitable date in YYYY-MM-DD format:")
        contact = simpledialog.askstring("Input", "Enter your contact no:")
        unique_id = self.uid()
        messagebox.showinfo("Success", f"Your unique generated ID: {unique_id}\n\nCongratulations Your appointment has been booked!")
        
        data1 = (unique_id, name, age, gender, date, contact, doctor_id)
        sql1 = "insert into patient values(%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql1, data1)
        con.commit()

        data2 = (unique_id, name, age, doctor_id, date, 0, 0)
        sql2 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql2, data2)
        con.commit()

    def book_bed(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        age = simpledialog.askstring("Input", "Enter Age:")
        gender = simpledialog.askstring("Input", "Enter Gender:")
        doctor_id = simpledialog.askstring("Input", "Enter Doctor's ID under which you want to take admission:")

        if doctor_id not in doc_id:
            messagebox.showerror("Error", "Enter a valid doctor ID")
            return

        date = simpledialog.askstring("Input", "Enter your suitable date you want to take admission in YYYY-MM-DD format:")
        unique_id = self.uid()
        messagebox.showinfo("Success", f"Your unique generated ID: {unique_id}")

        bed_type = simpledialog.askstring("Input", "Book a bed----\n1. General bed\n2. ICU bed\nEnter your choice:")
        if bed_type == "1":
            bed_type = "GEN"
        elif bed_type == "2":
            bed_type = "ICU"
        else:
            messagebox.showerror("Error", "Enter a valid choice")
            return

        data3 = (unique_id, name, age, gender, doctor_id, bed_type, date, 0)
        sql3 = "insert into admission values(%s,%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql3, data3)
        con.commit()

        data6 = (unique_id, name, age, doctor_id, date, 0, 0)
        sql6 = "insert into final values(%s,%s,%s,%s,%s,%s,%s)"
        c.execute(sql6, data6)
        con.commit()

        messagebox.showinfo("Success", f"Congratulations Your {bed_type} Bed has been booked!")

    def find_best_doctor(self):
        dept_code = simpledialog.askstring("Input", "Find Your best doctor----\n1. Cardiology (CD)\n2. Neurology (NU)\n3. Dermatology (DM)\n4. Surgery (SG)\n5. Gastroentrology (GS)\nEnter department code:")
        c.execute(f"select name from doc where dept='{dept_code}'")
        result = c.fetchall()
        doctors = "\n".join([f"Dr. {self.clean(i)}" for i in result])
        messagebox.showinfo("Doctors", doctors)

    def book_ambulance(self):
        room_no = simpledialog.askstring("Input", "Enter room no:")
        patient_name = simpledialog.askstring("Input", "Enter patient name:")
        contact_no = simpledialog.askstring("Input", "Enter contact number:")
        location = simpledialog.askstring("Input", "Enter location:")

        data3 = (room_no, patient_name, contact_no, location)
        sql3 = "insert into emergency2 values(%s,%s,%s,%s)"
        c.execute(sql3, data3)
        con.commit()
        
        messagebox.showinfo("Success", "Congrats!!! Your ambulance has been booked and will reach your location shortly")

    def cancel_appointment(self):
        unique_id = simpledialog.askstring("Input", "Enter Your ID:")
        if self.patient_check(unique_id):
            c.execute(f"DELETE FROM patient WHERE uid={unique_id}")
            con.commit()
            messagebox.showinfo("Success", "Your appointment is Cancelled!")
        else:
            messagebox.showerror("Error", "You do not have any appointments!")

    def staff_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Staff----").pack()
        tk.Button(self.root, text="1. Login with ID", command=self.staff_login).pack()
        tk.Button(self.root, text="2. Return to Main menu", command=self.main_menu).pack()

    def staff_login(self):
        staff_id = simpledialog.askstring("Input", "Enter your ID Number:")
        if staff_id not in staff_id:
            messagebox.showerror("Error", "Enter a valid ID")
            return

        c.execute(f"select name from staff where ID={staff_id}")
        result = c.fetchall()
        staff_name = self.clean(result[0])
        messagebox.showinfo("Welcome", f"Hi! {staff_name}")

        self.clear_window()
        tk.Label(self.root, text="Login with ID ----").pack()
        tk.Button(self.root, text="1. Show the bill of a patient", command=self.show_patient_bill).pack()
        tk.Button(self.root, text="2. Show the emergency list", command=self.show_emergency_list).pack()
        tk.Button(self.root, text="3. Book a bed for patient", command=self.book_bed).pack()
        tk.Button(self.root, text="4. Return to Main menu", command=self.main_menu).pack()

    def show_patient_bill(self):
        patient_id = simpledialog.askstring("Input", "Enter the patient's ID Number:")
        c.execute(f"select bill from final where ID={patient_id}")
        result = c.fetchall()
        bill = self.clean(result[0])
        messagebox.showinfo("Bill", f"Net bill of patient with ID {patient_id}: ₹{bill}")

    def show_emergency_list(self):
        c.execute("select * from emergency")
        result = c.fetchall()
        emergencies = "\n".join([str(i) for i in result])
        messagebox.showinfo("Emergency List", f"('Location', 'Contact Number')\n{emergencies}")

    def doctor_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Doctor----").pack()
        tk.Button(self.root, text="1. Login with ID", command=self.doctor_login).pack()
        tk.Button(self.root, text="2. Return to Main menu", command=self.main_menu).pack()

    def doctor_login(self):
        doctor_id = simpledialog.askstring("Input", "Enter your ID Number:")
        if doctor_id not in doc_id:
            messagebox.showerror("Error", "Enter valid ID")
            return

        c.execute(f"select name from doc where ID={doctor_id}")
        result = c.fetchall()
        doctor_name = self.clean(result[0])
        messagebox.showinfo("Welcome", f"Hi! Dr. {doctor_name}")

        self.clear_window()
        tk.Label(self.root, text="Login with ID ----").pack()
        tk.Button(self.root, text="1. Show my appointments", command=self.show_appointments).pack()
        tk.Button(self.root, text="2. Discharge a patient", command=self.discharge_patient).pack()
        tk.Button(self.root, text="3. Update my opd list", command=self.update_opd_list).pack()
        tk.Button(self.root, text="4. Return to Main menu", command=self.main_menu).pack()

    def show_appointments(self):
        doctor_id = simpledialog.askstring("Input", "Enter your ID Number:")
        messagebox.showinfo("Appointments", "Hello doctor, your today's OPD appointments are----")
        c.execute(f"select name,uid from patient where dr={doctor_id}")
        result = c.fetchall()
        appointments = "\n".join([self.clean(i) for i in result])
        messagebox.showinfo("Appointments", appointments)

        messagebox.showinfo("Hospital Patients", "And, your today's patients in hospitals are----")
        c.execute(f"select name,ID from admission where dr={doctor_id}")
        result = c.fetchall()
        hospital_patients = "\n".join([self.clean(i) for i in result])
        messagebox.showinfo("Hospital Patients", hospital_patients)

    def discharge_patient(self):
        doctor_id = simpledialog.askstring("Input", "Enter your ID Number:")
        messagebox.showinfo("Patients", "Your all inhospital patients along with their ID----")
        c.execute(f"select name,ID from admission where dr={doctor_id}")
        result = c.fetchall()
        patients = "\n".join([self.clean(i) for i in result])
        messagebox.showinfo("Patients", patients)

        patient_id = simpledialog.askstring("Input", "Enter the id of the patient you want to discharge:")
        c.execute(f"select incoming_date from final where ID={patient_id}")
        result = c.fetchall()
        incoming_date = self.clean(result[0])
        messagebox.showinfo("Admission Date", f"Your patient was admitted on {incoming_date}")

        days_in_hospital = simpledialog.askstring("Input", "Enter the no of days the patient was in the hospital under you:")
        c.execute(f"select bed_type from admission where ID={patient_id}")
        result = c.fetchall()
        bed_type = self.clean(result[0])

        if bed_type == 'GEN':
            bill = (4500 + 2000 + 1000) * int(days_in_hospital)
        elif bed_type == 'ICU':
            bill = (7500 + 3000 + 1500) * int(days_in_hospital)

        c.execute(f"update final set bill={bill} where ID={patient_id}")
        c.execute(f"DELETE FROM admission WHERE ID={patient_id}")
        c.execute(f"update final set days={days_in_hospital} where ID={patient_id}")
        con.commit()

        messagebox.showinfo("Discharge", "Discharged Successfully")

    def update_opd_list(self):
        patient_id = simpledialog.askstring("Input", "Enter the id of the patient you have checked:")
        c.execute(f"DELETE FROM patient WHERE uid={patient_id}")
        con.commit()
        messagebox.showinfo("Update", "Your patient list Updated!")

    def uid(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(4)])

    def clean(self, str1):
        return str1[0] if str1 else ""

    def patient_check(self, str1):
        c.execute("select uid FROM patient")
        result = c.fetchall()
        result1 = [self.clean(i) for i in result]
        return str1 in result1

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
