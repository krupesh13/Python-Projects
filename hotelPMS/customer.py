from tkinter import*
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1295x550+230+220')

        # variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()


# title
        lbl_title=Label(self.root,text="Add customer details",font=("times new romen",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
# label frame

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text='Customer detials',font=('times new roman',12,'bold'),fg="black")
        labelframeleft.place(x=5,y=50,width=425,height=490)
# labels and entries
# custoref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,state="readonly",width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)

# custname
        
        cname=Label(labelframeleft,text="Customer Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1) 

#mothername

        mname=Label(labelframeleft,text="Mother Name :",font=("times new roman",12,"bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("times new roman",13,"bold"))
        txtmname.grid(row=2,column=1)

#gendername

        gender=Label(labelframeleft,text="Gender :",font=("times new roman",12,"bold"),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_gender['value']=("Male","Female","Other")
        # combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        
#postcode
        postcode=Label(labelframeleft,text="Postcode :",font=("times new roman",12,"bold"),padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)
        
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
        txtpostcode.grid(row=4,column=1) 

#mobilenumber

        mobilenum=Label(labelframeleft,text="Mobile Number :",font=("times new roman",12,"bold"),padx=2,pady=6)
        mobilenum.grid(row=5,column=0,sticky=W)
        
        txtmobilenum=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        txtmobilenum.grid(row=5,column=1)

        #email

        email=Label(labelframeleft,text="E-mail :",font=("times new roman",12,"bold"),padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)
        
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        txtemail.grid(row=6,column=1)  

        # nationality

        nationality=Label(labelframeleft,text="Nationality :",font=("times new roman",12,"bold"),padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)

        combo_nationlity=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_nationlity['value']=("India","American","Other")
        # combo_nationlity.current(0)
        combo_nationlity.grid(row=7,column=1)
        
        # idproof 

        lbl_idprrof=Label(labelframeleft,text="ID Proof :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_idprrof.grid(row=8,column=0,sticky=W)

        combo_proof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_proof['value']=("Card","License","Passport")
        # combo_proof.current(0)
        combo_proof.grid(row=8,column=1)
        
        # id number

        lbl_idnumber=Label(labelframeleft,text="ID Number :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_idnumber.grid(row=9,column=0,sticky=W)
        
        txtidnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("times new roman",13,"bold"))
        txtidnumber.grid(row=9,column=1)

        # address

        lbladress=Label(labelframeleft,text="Address :",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbladress.grid(row=10,column=0,sticky=W)
        
        txtadress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
        txtadress.grid(row=10,column=1)


        # buttons

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)
        
        
        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        
        btndelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        
        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)
     
    #  table frame 
        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text='View detials and Search History',font=('times new roman',12,'bold'),fg="black")
        tableframe.place(x=435,y=50,width=860,height=490)

        lblsearchbar=Label(tableframe,text="Search :",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblsearchbar.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        self.txt_search=StringVar()


        combo_search=ttk.Combobox(tableframe,textvariable=self.txt_search,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_search['value']=("Mobile Number","Ref","ID")
        # combosearchf.current(0)
        combo_search.grid(row=0,column=1,padx=5)


        txtSEARCH=ttk.Entry(tableframe,width=29,font=("times new roman",13,"bold"))
        txtSEARCH.grid(row=0,column=2,padx=5)
        
        btnsearch=Button(tableframe,command=self.search,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=2)

        btnshowall=Button(tableframe,command=self.fetch_data,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=2)

# show data table
        
        details_frame=Frame(tableframe,bd=2,relief=RIDGE)
        details_frame.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.Cust_details_table=ttk.Treeview(details_frame,columns=("Ref","Name","Mother Name","Gender","Post","Mobile","E-mail","Nationality","ID-Proof","ID-Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("Ref",text='Refer No.')
        self.Cust_details_table.heading("Name",text='Name')
        self.Cust_details_table.heading("Mother Name",text='Mother Name')
        self.Cust_details_table.heading("Gender",text='Gender')
        self.Cust_details_table.heading("Post",text='Post')
        self.Cust_details_table.heading("Mobile",text='Mobile')
        self.Cust_details_table.heading("E-mail",text='Email')
        self.Cust_details_table.heading("Nationality",text='Nationality')
        self.Cust_details_table.heading("ID-Proof",text='ID-proof')
        self.Cust_details_table.heading("ID-Number",text='ID-number')
        self.Cust_details_table.heading("Address",text='Address')
 
        self.Cust_details_table["show"]="headings"
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                   self.var_ref.get(),
                   self.var_cust_name.get(),
                   self.var_mother.get(),
                   self.var_gender.get(),
                   self.var_post.get(),
                   self.var_mobile.get(),
                   self.var_email.get(),
                   self.var_nationality.get(),
                   self.var_id_proof.get(),
                   self.var_id_number.get(),
                   self.var_address.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!= 0:
                self.Cust_details_table.delete(*self.Cust_details_table.get_children())
                for i in rows:
                        self.Cust_details_table.insert("",END,values=i)
                conn.commit()
        conn.close()        

    def get_cursor(self,event=""):
         cursor_row=self.Cust_details_table.focus()
         content=self.Cust_details_table.item(cursor_row)
         row=content["values"]

         self.var_ref.set(row[0]),
         self.var_cust_name.set(row[1]),
         self.var_mother.set(row[2]),
         self.var_gender.set(row[3]), 
         self.var_post.set(row[4]),
         self.var_mobile.set(row[5]),
         self.var_email.set(row[6]),
         self.var_nationality.set(row[7]),
         self.var_id_proof.set(row[8]),
         self.var_id_number.set(row[9]),
         self.var_address.set(row[10]),

    def update(self):
         if self.var_mobile=="":
              messagebox.showerror("Error","Please enter mobile number",parent=self.root)
         else:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
              my_cursor.execute("update customer set Name=%s,`Mother Name`=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,`ID-Proof`=%s,`ID-Number`=%s,Address=%s where Ref=%s",(
                   
                   self.var_cust_name.get(),
                   self.var_mother.get(),
                   self.var_gender.get(),
                   self.var_post.get(),
                   self.var_mobile.get(),
                   self.var_email.get(),
                   self.var_nationality.get(),
                   self.var_id_proof.get(),
                   self.var_id_number.get(),
                   self.var_address.get(),
                   self.var_ref.get()


              ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("updated","details UPdated",parent=self.root)
        

    def delete(self):
         delete=messagebox.askyesno("PMS","Do you want to delete this customer",parent=self.root)
         if delete>0:
              conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
              my_cursor=conn.cursor()
        #       my_cursor.execute("")
              query="delete from customer where Ref=%s"
              value=(self.var_ref.get(),)
              my_cursor.execute(query,value)
         else:
              if not delete:
                   return     
         conn.commit()
         self.fetch_data()
         conn.close()


    def reset(self):
        #  self.var_ref.set(""),
         self.var_cust_name.set(""),
         self.var_mother.set(""),
        #  self.var_gender.set(""), 
         self.var_post.set(""),
         self.var_mobile.set(""),
         self.var_email.set(""),
        #  self.var_nationality.set(""),
        #  self.var_id_proof.set(""),
         self.var_id_number.set(""),
         self.var_address.set(""),
         self.var_ref=StringVar()

         x=random.randint(1000,9999)
         self.var_ref.set(str(x))


    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Satkaival@123",database="hotelmanagemnet")    
         my_cursor=conn.cursor()
         my_cursor.execute("select * from customer where "+str(self.search_var.get())+ "LIKE '%" +str(self.txt_search.get())+"%'")
         rows=my_cursor.fetchall()
         if len(rows)!=0:
              self.Cust_details_table.delete(*self.Cust_details_table.get_children)
              for i in rows:
                   self.Cust_details_table.insert("",END,values=i)
              conn.commit()
         conn.close()  



if __name__=='__main__':
    root=Tk()
    obj=Cust_window(root)
    root.mainloop()