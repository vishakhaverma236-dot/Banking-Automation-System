from tkinter import Tk,Label,Frame,Entry,Button,messagebox
from tkinter.ttk import Combobox
import time
import generate
from PIL import Image,ImageTk
import random
# to update time after each 1 sec
# create root window
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(bg='#002147')
def update_time():
    dt=time.strftime("📅%A-%d-%m-%Y ⏰%r")
    lbl_tt.config(text=dt)
    root.after(1000,update_time)
list_logos=['bank.png','bank1.png','bank2.png','bank3.png','bank4.png','bank5.png']
def update_logo():
    logo=random.choice(list_logos)
    img=Image.open(logo).resize((250,150))
    img_pil=ImageTk.PhotoImage(img,master=root)
    lbl_img.configure(image=img_pil)
    lbl_img.image=img_pil
    root.after(1000,update_logo)

def fp_frame():
    frm=Frame(root,highlightbackground='black',highlightthickness=2) 
    frm.configure(bg='alice blue')
    frm.place(relx=.55,rely=.165,relwidth=.44,relheight=.71)

    
    # frm.place(relx=.55,rely=.165,relwidth=.44,relheight=.71)
    def call_main_frame():
        frm.destroy()
        main_frame()
    lbl_acn=Label(frm,text='  ACN 👤   ',font=('arial',20,'bold'),bg="powder blue")
    lbl_acn.place(relx=.15,rely=.2)
    lbl_email=Label(frm,text=' Email 📧  ',font=('arial',20,'bold'),bg="powder blue")
    lbl_email.place(relx=.15,rely=.3)
    lbl_adhar=Label(frm,text=' Adhaar 🪪 ',font=('arial',20,'bold'),bg="powder blue")
    lbl_adhar.place(relx=.15,rely=.4)



    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.2)
    e_acn.focus()
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)
    cb_adhar=Entry(frm,font=('arial',20,'bold'),bd=5)
    cb_adhar.place(relx=.4,rely=.4)
    btn_pas=Button(frm,text='Send OTP ',bg='powder blue',font=('arial',15,'bold'))
    btn_pas.place(relx=.4,rely=.6)

    btn_back=Button(frm,text='Back 🔁',font=('arial',14,'bold'),bg='powder blue',command=call_main_frame)
    btn_back.place(relx=.01,rely=.01)
    
def customer_frm():
    frm=Frame(root,highlightbackground='black',highlightthickness=2) 
    frm.configure(bg="#48619D")
    frm.place(relx=.0,rely=.165,relwidth=1,relheight=.73)

    def call_main_frame():
        frm.destroy()
        main_frame()
    def logout():
        frm.destroy()
        main_frame()
    
    def view():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is View Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)

    def edit():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is Edit Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)

    def deposit():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is Deposit Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)

    def withdraw():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is withdraw Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)

    def trans():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is transfer Amount Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)

    def hist():
        cfrm=Frame(frm,highlightbackground='white',highlightthickness=2)
        cfrm.configure(bg='alice blue')
        cfrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_view=Label(frm,text='This is View history Screen',font=('arial',15,'bold','underline'))
        lbl_view.place(relx=.43,rely=.3)




    lbl_add=Label(frm,text=' Welcome ... ',font=('arial',20,'bold','underline'),bg='#48619D')
    lbl_add.place(relx=.45,rely=.05)

    btn_logout=Button(frm,text='Logout',font=('arial',12,'bold'),bg='#F3C623',command=logout)
    btn_logout.place(relx=.9,rely=.01)
    imag=Image.open('default.png').resize((150,150))

    img_pill=ImageTk.PhotoImage(imag,master=root)
    lbel_profile=Label(root,image=img_pill)
    lbel_profile.configure(image=img_pill)
    lbel_profile.image=img_pill
    img_pill=ImageTk.PhotoImage(imag,master=root)
    lbel_profile.place(relx=.02,rely=0.18)
    btn_logout=Button(frm,text='🔁',font=('arial',12,'bold'),bg='powder blue')
    btn_logout.place(relx=.13,rely=.22)

    btn_view=Button(frm,text='  View Details  ',font=('arial',12,'bold'),bg='powder blue',bd=5,width='14',command=view)
    btn_view.place(relx=.02,rely=.3)

    btn_edit=Button(frm,text='  Edit Details  ',font=('arial',12,'bold'),bg='white',bd=5,width='14',command=edit)
    btn_edit.place(relx=.02,rely=.4)

    btn_deposit=Button(frm,text='  Deposite Amt  ',font=('arial',12,'bold'),bg='green',bd=5,width='14',command=deposit)
    btn_deposit.place(relx=.02,rely=.5)

    btn_withdraw=Button(frm,text='  Withdraw Amt  ',font=('arial',12,'bold'),bg='red',bd=5,width='14',command=withdraw)
    btn_withdraw.place(relx=.02,rely=.6)

    btn_trans=Button(frm,text='  Transfer Amt  ',font=('arial',12,'bold'),bg='white',fg='red',bd=5,width='14',command=trans)
    btn_trans.place(relx=.02,rely=.7)

    btn_hist=Button(frm,text='  View History  ',font=('arial',12,'bold'),bg='brown',bd=5,width='14',command=hist)
    btn_hist.place(relx=.02,rely=.8)





    



def admin_frm():
    frm=Frame(root,highlightbackground='black',highlightthickness=2) 
    frm.configure(bg='alice blue')
    frm.place(relx=.0,rely=.165,relwidth=1,relheight=.73)
    
    def call_main_frame():
        frm.destroy()
        main_frame()
    def logout():
        frm.destroy()
        main_frame()

    

    

    def open():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        # frm.configure(bg='alice blue')
        # ifrm.place(relx=.0,rely=.165,relwidth=1,relheight=.73)
        ifrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_title=Label(frm,text="Open an Account",
                font=('arial',15,'bold'),bg='#002147',fg='Alice blue')
        lbl_title.place(relx=.45,rely=.3)

        lbl_name=Label(frm,text="Name",
                font=('arial',15),bg='white',fg='black')
        lbl_name.place(relx=.25,rely=.4)

        e_name=Entry(frm,font=('arial',15),bd=5)
        e_name.focus()
        e_name.place(relx=.25,rely=.46)

        lbl_email=Label(frm,text="Email",
                font=('arial',15),bg='white',fg='black')
        lbl_email.place(relx=.25,rely=.52)
        
        e_email=Entry(frm,font=('arial',15),bd=5)
        e_email.place(relx=.25,rely=.58)

        lbl_mobile=Label(frm,text="Mobile No.",
                font=('arial',15),bg='white',fg='black')
        lbl_mobile.place(relx=.25,rely=.64)
        
        e_mobile=Entry(frm,font=('arial',15),bd=5)
        e_mobile.place(relx=.25,rely=.7)

        lbl_adhar=Label(frm,text="Adhaar",
                font=('arial',15),bg='white',fg='black')
        # lbl_adhar.place(relx=.25,rely=.76)
        lbl_adhar.place(relx=.45,rely=.4)

        e_adhar=Entry(frm,font=('arial',15),bd=5)
        e_adhar.place(relx=.25,rely=.82)

        lbl_dob=Label(frm,text="Date of Birth",
                font=('arial',15),bg='white',fg='black')
        # lbl_dob.place(relx=.45,rely=.4)
        lbl_dob.place(relx=.25,rely=.76)
        
        e_dob=Entry(frm,font=('arial',15),bd=5)
        e_dob.place(relx=.45,rely=.46)
        
        lbl_pan=Label(frm,text="Pan card ",
                font=('arial',15),bg='white',fg='black')
        # lbl_adhar.place(relx=.25,rely=.76)
        lbl_pan.place(relx=.45,rely=.52)

        e_pan=Entry(frm,font=('arial',15),bd=5)
        e_pan.place(relx=.45,rely=.58)

        lbl_adr=Label(frm,text="Address ",
                font=('arial',15),bg='white',fg='black')
        # lbl_adhar.place(relx=.25,rely=.76)
        lbl_adr.place(relx=.45,rely=.64)

        e_adr=Entry(frm,font=('arial',15),bd=5)
        e_adr.place(relx=.45,rely=.7)

        btn_save=Button(frm,text='Save',font=('arial',12,'bold'),bg='powder blue')
        btn_save.place(relx=.45,rely=.8)
        btn_reset=Button(frm,text='Reset',font=('arial',12,'bold'),bg='powder blue')
        btn_reset.place(relx=.5,rely=.8)






    def close():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        # frm.configure(bg='alice blue')
        ifrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_title=Label(frm,text=" Close Account  ",
                font=('arial',15,'bold'),bg='#002147',fg='Alice blue')
        lbl_title.place(relx=.45,rely=.3)
        lbl_acn=Label(frm,text=' ACN 👤 ',font=('arial',20,'bold'),bg="powder blue")
        lbl_acn.place(relx=.35,rely=.4)
        e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
        e_acn.place(relx=.45,rely=.4)
        e_acn.focus()
        btn_otp=Button(frm,text='Send OTP',font=('arial',12,'bold'),bg='powder blue')
        btn_otp.place(relx=.48,rely=.55)


    def view():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        # frm.configure(bg='alice blue')
        # ifrm.place(relx=.15,rely=.3,relwidth=.68,relheight=.65)
        ifrm.place(relx=.2,rely=.25,relwidth=.6,relheight=.7)
        lbl_title=Label(frm,text=" View Account  ",
                font=('arial',15,'bold'),bg='#002147',fg='Alice blue')
        lbl_title.place(relx=.45,rely=.3)
        lbl_acn=Label(frm,text=' ACN 👤 ',font=('arial',20,'bold'),bg="powder blue")
        lbl_acn.place(relx=.35,rely=.4)
        e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
        e_acn.place(relx=.45,rely=.4)
        e_acn.focus()
        btn_view=Button(frm,text='View',font=('arial',14,'bold'),bg='powder blue')
        btn_view.place(relx=.68,rely=.4)




   
    btn_back=Button(frm,text='Back 🔁',font=('arial',12,'bold'),bg='#F3C623',command=call_main_frame)
    btn_back.place(relx=.01,rely=.01)
    lbl_add=Label(frm,text=' Welcome Admin ',font=('arial',20,'bold','underline'),bg="powder blue")
    lbl_add.place(relx=.45,rely=.05)

    btn_logout=Button(frm,text='Logout',font=('arial',12,'bold'),bg='#F3C623',command=logout)
    btn_logout.place(relx=.9,rely=.01)
    btn_open=Button(frm,text='Open Account',font=('arial',12,'bold'),bg='green',fg='white',command=open)
    btn_open.place(relx=.15,rely=.15)
    btn_close=Button(frm,text='Close Account',font=('arial',12,'bold'),bg='red',fg='white',command=close)
    btn_close.place(relx=.45,rely=.15)
    btn_view=Button(frm,text='View Account',font=('arial',12,'bold'),bg='navy blue',fg='white',command=view)
    btn_view.place(relx=.7,rely=.15)
    




def main_frame():
    def referesh_captcha():
        nonlocal gen_captcha
        gen_captcha=generate.generate_captcha()
        lbl_captcha.config(text=gen_captcha)

    def call_fp_frame():
        frm.destroy()
        fp_frame()
    
    def login():
        utype=cb_user.get()
        if utype=='Admin':
            frm.destroy()
            lbel_img.destroy
            admin_frm()

        elif utype=="Customer":
            frm.destroy()
            customer_frm()
        else:
             messagebox.showerror("login","invalid user type")

    # root=parent of frame attribute 
    frm=Frame(root,highlightbackground='black',highlightthickness=2) 
    frm.configure(bg='Alice Blue')
    frm.place(relx=.55,rely=.165,relwidth=.44,relheight=.71)

    lbl_acn=Label(frm,text=' ACN 👤 ',font=('arial',20,'bold'),bg="powder blue")
    lbl_acn.place(relx=.2,rely=.1)
    lbl_pass=Label(frm,text=' Pass ',font=('arial',20,'bold'),bg="powder blue")
    lbl_pass.place(relx=.2,rely=.2)
    lbl_user=Label(frm,text=' User ',font=('arial',20,'bold'),bg="powder blue")
    lbl_user.place(relx=.2,rely=.3)



    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show="*****")
    e_pass.place(relx=.4,rely=.2)
    cb_user=Combobox(frm,values=['Customer','Admin'],font=('arial',20,'bold'))
    cb_user.current(0)
    cb_user.place(relx=.4,rely=.3)

    gen_captcha=generate.generate_captcha()
    lbl_captcha=Label(frm,text=gen_captcha, font=('Courier New',15,'bold'),width=15,bg='yellow')
    lbl_captcha.place(relx=.25,rely=.4)
    lbl_cap=Label(frm,text=' Captcha ',font=('arial',20,'bold'),bg="medium purple",fg='white')
    lbl_cap.place(relx=.15,rely=.5)
    e_cap=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_cap.place(relx=.4,rely=.5)
    btn_referesh=Button(frm,text='refresh 🔄',bg="powder blue",font=('arial',15,'bold'),command=referesh_captcha)
    btn_referesh.place(relx=.59,rely=.4)

    btn_login=Button(frm,text='Login 🔐',bg='powder blue',font=('arial',14,'bold'),command=login)
    btn_login.place(relx=.3,rely=.6)



    btn_referesh=Button(frm,text='Reset 🔁',font=('arial',14,'bold'),bg='powder blue')
    btn_referesh.place(relx=.5,rely=.6)
    btn_forget=Button(frm,text= "Forget Password🔑",font=('arial',13,'bold'),bg='powder blue',command=call_fp_frame )
    btn_forget.place(relx=.35,rely=.7)



    btn_referesh=Button(frm,text='refresh 🔄',font=('arial',15,'bold'),command=referesh_captcha)
    btn_referesh.place(relx=.59,rely=.4)




    

    # img=Image.open(logo).resize((250,150))
    # img_pil=ImageTk.PhotoImage(img,master=root)
    # lbl_img.configure(image=img_pil)
    # lbl_img.image=img_pil


    imag=Image.open('system.png').resize((820,605))

    img_pill=ImageTk.PhotoImage(imag,master=root)
    lbel_img=Label(root,image=img_pill)
    lbel_img.configure(image=img_pill)
    lbel_img.image=img_pill
    img_pill=ImageTk.PhotoImage(imag,master=root)
    lbel_img.place(relx=0,rely=0.165)



def f_frame():
    # root=parent of frame attribute 
    ffrm=Frame(root,highlightbackground='black',highlightthickness=2) 
    ffrm.configure(bg='lavender')
    
    lbl_footer=Label(root,text='Developed by:Vishakha\n:📞7251008737',
                 font=('arial',20,'bold'),bg='lavender')
    lbl_footer.pack(side='bottom')
    ffrm.place(relx=0,rely=.89,relwidth=1,relheight=.38)







lbl_title=Label(root,text="Banking Automation",
                font=('arial',50,'bold','underline'),bg='#002147',fg='#F3C623')
lbl_title.pack()
dt=time.strftime("📅%A-%d-%m-%Y ⏰%r")
lbl_tt=Label(root,text='',font=('arial',20,'bold'),bg='#002147',fg='#F3C623')
# use to place it at center
lbl_tt.pack()
update_time()

img=Image.open('bank.png').resize((200,150))

img_pil=ImageTk.PhotoImage(img,master=root)
lbl_img=Label(root,image=img_pil)
lbl_img.place(relx=0,rely=0)

# imag=Image.open('bank1.png').resize((500,200))

# img_pill=ImageTk.PhotoImage(imag,master=root)
# lbel_img=Label(root,image=img_pill)
# lbel_img.configure(image=img_pill)
# lbel_img.image=img_pill
# img_pill=ImageTk.PhotoImage(imag,master=root)
# lbel_img.place(relx=0.1,rely=0.2)
update_logo()
f_frame()
main_frame()
root.mainloop()