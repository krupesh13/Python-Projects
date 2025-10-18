from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
import json

class auto_details_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')
        

        self.load_btn = Button(self.root, text="Load Bookings",font=("arial",12,"bold"),bg="black",fg="gold",width=15,command=self.show_bookings)
        self.load_btn.grid(row=0,column=10,padx=500,pady=50)

    def load_bookings(self):
            with open("auto_details.json", "r") as file:
               return json.load(file)
        
    def insert_booking(self, auto_details):
            response = messagebox.askyesno(
                "Approval Needed", f"Do you approve booking for {auto_details['Name']}?"
            )
            if response:  # If user clicks 'Yes'
                try:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Satkaival@123", database="hotelmanagemnet"
                    )
                    cursor = conn.cursor()

                    # Check if customer exists
                    cursor.execute("SELECT * FROM customer WHERE Mobile = %s", (auto_details["Mobile"],))
                    customer_exists = cursor.fetchone()

                    if not customer_exists:
                        # Insert new customer
                        sql_customer = """INSERT INTO customer (Ref, Name, `Mother Name`, Gender , Post , Mobile , Email , Nationality , `ID-Proof` , `ID-Number` , Address) 
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        values_customer = (
                            auto_details["Ref"],
                            auto_details["Name"],
                            auto_details["Mother Name"],
                            auto_details["Gender"],
                            auto_details["Post"],
                            auto_details["Mobile"],
                            auto_details["Email"],
                            auto_details["Nationality"],
                            auto_details["ID-Proof"],
                            auto_details["ID-Number"],
                            auto_details["Address"],
                            

                        )
                        cursor.execute(sql_customer, values_customer)

                    # Insert room details linked to customer
                    sql_room = """INSERT INTO room (Contact, checkin, checkout, roomtype, roomavailable, meal , noOfDays)
                                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    values_room = (
                        auto_details["Mobile"],
                        auto_details["checkin"],
                        auto_details["checkout"],
                        auto_details["roomtype"],
                        auto_details["roomavailable"],
                        auto_details["meal"],
                        auto_details["noOfDays"],
                    )
                    cursor.execute(sql_room, values_room)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", f"Booking for {auto_details['Name']} added successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to insert: {e}")
            else:
                messagebox.showinfo("Rejected", f"Booking for {auto_details['Name']} was not approved.")

    
    def show_bookings(self):
        auto_details = self.load_bookings()
        for i, booking in enumerate(auto_details):
            label = ttk.Label(self.root, text=f"{booking['Name']} | {booking['roomtype']}")
            label.grid(row=i, column=0, padx=10, pady=5)

            approve_btn = Button(self.root, text="Approve", command=lambda b=booking: self.insert_booking(b))
            approve_btn.grid(row=i, column=1, padx=10, pady=5)



if __name__ == "__main__":
    root = Tk()
    app = auto_details_window(root)
    root.mainloop()
