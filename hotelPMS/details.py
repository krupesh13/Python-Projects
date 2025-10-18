from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class details_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomtype=StringVar()

        lbl_title=Label(self.root,text="Room Booking",font=("times new romen",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        
        # label frame

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Add New Room',font=('times new roman',12,'bold'),fg="black")
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # floor
        lbl_floor=Label(labelframeleft,text="Floor :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)
        
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("times new roman",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        # Roomno
        lbl_roomno=Label(labelframeleft,text="Room No. :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W,padx=20)
        
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("times new roman",13,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)
        
        # Roomtype
        lbl_roomtypee=Label(labelframeleft,text="Room Type :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtypee.grid(row=2,column=0,sticky=W,padx=20)
        
        entry_roomtypee=ttk.Entry(labelframeleft,width=20,textvariable=self.var_roomtype,font=("times new roman",13,"bold"))
        entry_roomtypee.grid(row=2,column=1,sticky=W)

# buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)
        
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        
        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

# table frame and search frame
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text='Show Room Details',font=('times new roman',12,'bold'),fg="black")
        tableframe.place(x=600,y=55,width=600,height=350)
        
        scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
        
        self.Room_table=ttk.Treeview(tableframe,columns=("Floor","Roomno","Roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_table.xview)
        scroll_y.config(command=self.Room_table.yview)
        
        self.Room_table.heading("Floor",text='Floor')
        self.Room_table.heading("Roomno",text='Room No')
        self.Room_table.heading("Roomtype",text='Room Type')
        
        # self.Room_table.heading("Nationality",text='Nationality')
        # self.Cust_details_table.heading("ID-Proof",text='ID-proof')
        # self.Cust_details_table.heading("ID-Number",text='ID-number')
        
 
        self.Room_table["show"]="headings"
        self.Room_table.pack(fill=BOTH,expand=1)
        self.Room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

# add data
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",  (


                                          self.var_floor.get(),
                                          self.var_roomno.get(),
                                          self.var_roomtype.get(),
                                          
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

# fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
                self.Room_table.delete(*self.Room_table.get_children())
                for i in rows:
                        self.Room_table.insert("",END,values=i)
                conn.commit()
        conn.close()


    def get_cursor(self,event=""):
         cursor_row=self.Room_table.focus()
         content=self.Room_table.item(cursor_row)
         row=content["values"]

         self.var_floor.set(row[0]),
         self.var_roomno.set(row[1]),
         self.var_roomtype.set(row[2]),
         
         
# updat btn
    def update(self):
         if self.var_roomno=="":
              messagebox.showerror("Error","Please Room No",parent=self.root)
         else:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
              my_cursor.execute("update details set Floor=%s,Roomtype=%s where RoomNo=%s",(
                   
                   self.var_floor.get(),
                   self.var_roomtype.get(),
                   self.var_roomno.get(),
                   


              ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("updated","details Updated",parent=self.root)

# delete data

    def delete(self):
         delete=messagebox.askyesno("PMS","Do you want to delete this room",parent=self.root)
         if delete>0:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
        #       my_cursor.execute("")
              query="delete from details where RoomNo=%s"
              value=(self.var_roomno.get(),)
              my_cursor.execute(query,value)
         else:
              if not delete:
                   return     
         conn.commit()
         self.fetch_data()
         conn.close()
# reset data
    def reset(self):
         self.var_roomno.set(""),
         self.var_floor.set(""),
         self.var_roomtype.set(""),
        

        

if __name__=="__main__":
    root=Tk()
    obj=details_window(root)
    root.mainloop()
