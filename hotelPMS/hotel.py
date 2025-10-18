from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_window
from room import room_window
from details import details_window
from auto_details import auto_details_window



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title('Hotel Management System')
        self.root.geometry('1550x800+0+0')

#first image
        img1=Image.open(r"C:\Users\patel\OneDrive\Desktop\hotelPMS\images\outdoor.jpg")
        img1=img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
#logo
        img2=Image.open(r"C:\Users\patel\OneDrive\Desktop\hotelPMS\images\logo.jpg")
        img2=img2.resize((250,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)


        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=250,height=140)
#title"hotel mangement

        lbl_title=Label(self.root,text="HOTEL PMS",font=("times new romen",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

#MAIN FRAME
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

#menu  
        lbl_menu=Label(main_frame,text="MENU",font=("times new romen",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)  
# BUTTON FRAME
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=230)

        cust_button=Button(btn_frame,text='Customer',command=self.cust_details,width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        cust_button.grid(row=0,column=0,pady=1)   
        
        room_button=Button(btn_frame,command=self.room_booking,text='Rooms',width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        room_button.grid(row=1,column=0,pady=1)   
        
        details_button=Button(btn_frame,text='Details',command=self.detailss,width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        details_button.grid(row=2,column=0,pady=1) 

        report_button=Button(btn_frame,text='Report',width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        report_button.grid(row=3,column=0,pady=1) 

        autodetails_button=Button(btn_frame,text='Auto-details',command=self.autodetails,width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        autodetails_button.grid(row=4,column=0,pady=1)

        logout_button=Button(btn_frame,text='Logout',width=19,font=('time new roman',14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")        
        logout_button.grid(row=5,column=0,pady=1)

#right side image
        
        img3=Image.open(r"C:\Users\patel\OneDrive\Desktop\hotelPMS\images\inside.jpg")
        img3=img3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=590)
        
    def cust_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Cust_window(self.new_window)
    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=room_window(self.new_window)
    def detailss(self):
        self.new_window=Toplevel(self.root)
        self.app=details_window(self.new_window)
    def autodetails(self):
        self.new_window=Toplevel(self.root)
        self.app=auto_details_window(self.new_window)   
  

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()        


