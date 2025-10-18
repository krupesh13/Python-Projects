from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class room_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        # variables
        self.va_contact=StringVar()
        self.va_checkin=StringVar()
        self.va_checkout=StringVar()
        self.va_roomtype=StringVar()
        self.va_roomavailable=StringVar()
        self.va_meal=StringVar()
        self.va_noofdays=StringVar()
        self.va_paidtax=StringVar()
        self.va_total=StringVar()
        self.va_totallll=StringVar()
    
        lbl_title=Label(self.root,text="Room Booking",font=("times new romen",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        # label frame

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Room Booking Details',font=('times new roman',12,'bold'),fg="black")
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # labels and entries
        # custoref
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.va_contact,width=20,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        btnfetchdata=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=7)
        btnfetchdata.place(x=340,y=4)
        
        # checkindate
        lbl_checkin=Label(labelframeleft,text="Check_in Date :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_checkin.grid(row=1,column=0,sticky=W)
        
        entry_checkin=ttk.Entry(labelframeleft,textvariable=self.va_checkin,width=29,font=("times new roman",13,"bold"))
        entry_checkin.grid(row=1,column=1)

        # checkoutdate
        lbl_checkout=Label(labelframeleft,text="Check_out Date :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_checkout.grid(row=2,column=0,sticky=W)
        
        entry_checkout=ttk.Entry(labelframeleft,textvariable=self.va_checkout,width=29,font=("times new roman",13,"bold"))
        entry_checkout.grid(row=2,column=1)

        # roomtype
        conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from details")
        types=my_cursor.fetchall()

        lbl_roomtype=Label(labelframeleft,text="Room Type:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)
        
        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.va_roomtype,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_roomtype["values"]=types
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)
        # available room
        lbl_availroom=Label(labelframeleft,text="Available Room:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_availroom.grid(row=4,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.va_roomavailable,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_roomno["values"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)

        # meal
        lbl_meal=Label(labelframeleft,text="Meal:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)
        
        entry_meal=ttk.Entry(labelframeleft,textvariable=self.va_meal,width=29,font=("times new roman",13,"bold"))
        entry_meal.grid(row=5,column=1)

        # no of days
        lbl_days=Label(labelframeleft,text="NO. of Days:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_days.grid(row=6,column=0,sticky=W)
        
        entry_dasy=ttk.Entry(labelframeleft,textvariable=self.va_noofdays,width=29,font=("times new roman",13,"bold"))
        entry_dasy.grid(row=6,column=1)

        # paid tax
        lbl_tax=Label(labelframeleft,text="Paid Tax:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_tax.grid(row=7,column=0,sticky=W)
        
        entry_tax=ttk.Entry(labelframeleft,width=29,textvariable=self.va_paidtax,font=("times new roman",13,"bold"))
        entry_tax.grid(row=7,column=1)

        # Sub total
        lbl_subtotal=Label(labelframeleft,text="Sub Total:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0,sticky=W)
        
        entry_subtotal=ttk.Entry(labelframeleft,textvariable=self.va_total,width=29,font=("times new roman",13,"bold"))
        entry_subtotal.grid(row=8,column=1)

        # total cost
        lbl_totalcost=Label(labelframeleft,text="Total Cost:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_totalcost.grid(row=9,column=0,sticky=W)
        
        entry_totalcost=ttk.Entry(labelframeleft,textvariable=self.va_totallll,width=29,font=("times new roman",13,"bold"))
        entry_totalcost.grid(row=9,column=1)
        
        # bill button

        btnbill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)

# buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)
        
        
        btnupdate=Button(btn_frame,command=self.update,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        
        btndelete=Button(btn_frame,command=self.delete,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        
        btnreset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

# table frame and search frame
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text='View detials and Search History',font=('times new roman',12,'bold'),fg="black")
        tableframe.place(x=435,y=280,width=860,height=260)

        lblsearchbar=Label(tableframe,text="Search :",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchbar.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        self.txt_search=StringVar()


        combo_search=ttk.Combobox(tableframe,textvariable=self.txt_search,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_search['value']=("Mobile Number","Rooms","ID")
        # combosearchf.current(0)
        combo_search.grid(row=0,column=1,padx=5)


        txtSEARCH=ttk.Entry(tableframe,width=29,font=("times new roman",13,"bold"))
        txtSEARCH.grid(row=0,column=2,padx=5)
        
        btnsearch=Button(tableframe,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(tableframe,command=self.fetch_data,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=2)

        details_frame=Frame(tableframe,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=180)
# data table 
        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.Room_table=ttk.Treeview(details_frame,columns=("Contact","Checkin","Checkout","Roomtype","Roomavailable","Meal","Days","Tax","Subtotal","Totalcost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_table.xview)
        scroll_y.config(command=self.Room_table.yview)

        self.Room_table.heading("Contact",text='Contact')
        self.Room_table.heading("Checkin",text='Check-in')
        self.Room_table.heading("Checkout",text='Check-out')
        self.Room_table.heading("Roomtype",text='Room Type')
        self.Room_table.heading("Roomavailable",text='Room No')
        self.Room_table.heading("Meal",text='Meal')
        self.Room_table.heading("Days",text='NoOfDays')
        # self.Room_table.heading("Nationality",text='Nationality')
        # self.Cust_details_table.heading("ID-Proof",text='ID-proof')
        # self.Cust_details_table.heading("ID-Number",text='ID-number')
        
 
        self.Room_table["show"]="headings"
        self.Room_table.pack(fill=BOTH,expand=1)
        self.Room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
# add data
    def add_data(self):
        if self.va_contact.get()=="" or self.va_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",  (


                                          self.va_contact.get(),
                                          self.va_checkin.get(),
                                          self.va_checkout.get(),
                                          self.va_roomtype.get(),
                                          self.va_roomavailable.get(),
                                          self.va_meal.get(),
                                          self.va_noofdays.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room alloted",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
    
    def get_cursor(self,event=""):
         cursor_row=self.Room_table.focus()
         content=self.Room_table.item(cursor_row)
         row=content["values"]

         self.va_contact.set(row[0]),
         self.va_checkin.set(row[1]),
         self.va_checkout.set(row[2]),
         self.va_roomtype.set(row[3]), 
         self.va_roomavailable.set(row[4]),
         self.va_meal.set(row[5]),
         self.va_noofdays.set(row[6]),
         
# updat btn
    def update(self):
         if self.va_contact=="":
              messagebox.showerror("Error","Please enter mobile number",parent=self.root)
         else:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
              my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfDays=%s where Contact=%s",(
                   
                   self.va_checkin.get(),
                   self.va_checkout.get(),
                   self.va_roomtype.get(),
                   self.va_roomavailable.get(),
                   self.va_meal.get(),
                   self.va_noofdays.get(),
                   self.va_contact.get(),
                   


              ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("updated","details UPdated",parent=self.root)

# delete data

    def delete(self):
         delete=messagebox.askyesno("PMS","Do you want to delete this customer",parent=self.root)
         if delete>0:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
        #       my_cursor.execute("")
              query="delete from room where Contact=%s"
              value=(self.va_contact.get(),)
              my_cursor.execute(query,value)
         else:
              if not delete:
                   return     
         conn.commit()
         self.fetch_data()
         conn.close()
# reset data
    def reset(self):
         self.va_contact.set(""),
         self.va_checkin.set(""),
         self.va_checkout.set(""),
        #  self.var_gender.set(""), 
         self.va_roomtype.set(""),
         self.va_roomavailable.set(""),
         self.va_meal.set(""),
        #  self.var_nationality.set(""),
        #  self.var_id_proof.set(""),
         self.va_noofdays.set(""),
        #  self.var_address.set(""),
        #  self.var_ref=StringVar()
         self.va_paidtax.set("")
         self.va_total.set("")
         self.va_totallll.set("")

        #  x=random.randint(1000,9999)
        #  self.var_ref.set(str(x))
    
# fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
                self.Room_table.delete(*self.Room_table.get_children())
                for i in rows:
                        self.Room_table.insert("",END,values=i)
                conn.commit()
        conn.close()


# all datd fetching
    def Fetch_contact(self):
        if self.va_contact.get()=="":
            messagebox.showerror("ERROR","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.va_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==NONE:
                messagebox.showerror("ERROR","invalid number",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=500,height=200)
                
                labelname=Label(showdataframe,text="Name:",font=("new times roman",12,"bold"))
                labelname.place(x=0,y=0)
                
                lbl=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl.place(x=90,y=0)
            
                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.va_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                labelgenmder=Label(showdataframe,text="Gender:",font=("new times roman",12,"bold"))
                labelgenmder.place(x=0,y=30)
                
                lbl2=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl2.place(x=90,y=30)

                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.va_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                labelemail=Label(showdataframe,text="Email:",font=("new times roman",12,"bold"))
                labelemail.place(x=0,y=60)
                

                lbl33=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl33.place(x=90,y=60)

                

                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.va_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                labelnationality=Label(showdataframe,text="Nationality:",font=("new times roman",12,"bold"))
                labelnationality.place(x=0,y=90)
                
                lbl3=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl3.place(x=90,y=90)




                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                query=("select `ID-Proof` from customer where Mobile=%s")
                value=(self.va_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                labelidproof=Label(showdataframe,text="ID-Proof:",font=("new times roman",12,"bold"))
                labelidproof.place(x=0,y=120)
                
                lbl4=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl4.place(x=90,y=120)




                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                query=("select `ID-Number` from customer where Mobile=%s")
                value=(self.va_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
            
                labelidnum=Label(showdataframe,text="ID-Number:",font=("new times roman",12,"bold"))
                labelidnum.place(x=0,y=150)
                
                lbl5=Label(showdataframe,text=row,font=("new times roman",12,"bold"))
                lbl5.place(x=90,y=150)
  


    def total(self):
         indates=self.va_checkin.get()
         outdate=self.va_checkout.get()
         indates=datetime.strptime(indates,"%d/%m/%Y")
         outdate=datetime.strptime(outdate,"%d/%m/%Y")
         self.va_noofdays.set(str(abs(outdate-indates).days))
         
         if (self.va_meal.get()=="yes" and self.va_roomtype.get()=="Smoking Rooms"):
              
              q1=float(50)
              q2=float(70)
              q3=float(self.va_noofdays.get())
              q4=float(q1+q2)
              q5=float(q3+q4)
              tax="$ "+str("%.2f"%((q5)*0.15))
              ST="$ "+str("%.2f"%(q5))
              TT="$ "+str("%.2f"%(q5+((q5)*0.15)))
              self.va_paidtax.set(tax)
              self.va_total.set(ST)
              self.va_totallll.set(TT)
              self.root.update_idletasks()
         
         elif (self.va_meal.get()=="no" and self.va_roomtype.get()=="Smoking Rooms"):
              
              q1=float(50)
            #   q2=float(70)
              q3=float(self.va_noofdays.get())
              q4=float(q1)
              q5=float(q3+q4)
              tax="$ "+str("%.2f"%((q5)*0.15))
              ST="$ "+str("%.2f"%(q5))
              TT="$ "+str("%.2f"%(q5+((q5)*0.15)))
              self.va_paidtax.set(tax)
              self.va_total.set(ST)
              self.va_totallll.set(TT)
              self.root.update_idletasks()
 
    # search sys
    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
         my_cursor=conn.cursor()
         my_cursor.execute("select * from room where "+str(self.search_var.get())+ "LIKE '%" +str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
              self.Room_table.delete(*self.Room_table.get_children)
              for i in rows:
                   self.Room_table.insert("",END,values=i)
              conn.commit()
         conn.close()  
    























if __name__=="__main__":
    root=Tk()
    obj=room_window(root)
    root.mainloop()