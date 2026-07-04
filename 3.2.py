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
    
def admin_frm():
    frm=Frame(root,highlightbackground='black',highlightthickness=2) 
    frm.configure(bg='Alice Blue')
    def call_main_frame():
        frm.destroy()
        main_frame()
    frm.place(relx=.55,rely=.165,relwidth=.44,relheight=.71)
    btn_back=Button(frm,text='Back 🔁',font=('arial',12,'bold'),bg='powder blue',command=call_main_frame)
    btn_back.place(relx=.01,rely=.01)
    lbl_add=Label(frm,text=' Welcome Admin ',font=('arial',20,'bold','underline'),bg="powder blue")
    lbl_add.place(relx=.35,rely=.1)

    btn_logout=Button(frm,text='Logout',font=('arial',12,'bold'),bg='powder blue')
    btn_logout.place(relx=.85,rely=.01)
    btn_open=Button(frm,text='Open Account',font=('arial',12,'bold'),bg='green',fg='white')
    btn_open.place(relx=.15,rely=.2)
    btn_close=Button(frm,text='Close Account',font=('arial',12,'bold'),bg='red',fg='white')
    btn_close.place(relx=.4,rely=.2)
    btn_view=Button(frm,text='View Account',font=('arial',12,'bold'),bg='navy blue',fg='white')
    btn_view.place(relx=.65,rely=.2)
    




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
            admin_frm()
        elif utype=="Customer":
            pass
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
                font=('arial',50,'bold','underline'),bg='navy blue',fg='Alice blue')
lbl_title.pack()
dt=time.strftime("📅%A-%d-%m-%Y ⏰%r")
lbl_tt=Label(root,text='',font=('arial',20,'bold'),bg='powder blue',fg='green')
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