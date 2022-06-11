from tkinter import *
from tkinter import messagebox


import smtplib


def sendgmail(receiver, msg):
    sender = '14.MAKTAB.RECTORANT'
    # receiver = ''
    password = 'fduhgljlpmekansj'
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender, password)
    # msg = ''
    smtpserver.sendmail(sender, receiver, msg)
    print('sent')
    smtpserver.close()




def donothing():
    print("error")

def oncloseTopWindow(window, toplevel):
    window.deiconify()
    window.state('zoomed')
    toplevel.destroy()
    Toplevel.geometry('400x200')


def onOpenGmailWindow(window):
    window.withdraw()
    gmailwindow = Toplevel()
    gmailwindow.protocol('WM_DELETE_WINDOW', lambda: oncloseTopWindow(window, gmailwindow))
    gmailwindow.title("G M A I L 📙")
    gmailwindow.geometry('500x400')
    gmailwindow.resizable(0, 0)
    gmailwindow.configure(bg='#86ff46')

    lb_gm = Label(gmailwindow, text="OLUVCHI GMAILI ↙️  ", bg='#ffe24c' )
    lb_gm.place(relx=0.3, rely=0.3, anchor=CENTER)

    str_bb = StringVar
    en_name = Entry(gmailwindow, text=str_bb, bd=8)
    en_name.place(relx=0.7, rely=0.3, anchor=CENTER)


    lbname = Label(gmailwindow, text="X A B A R  💭  ", bg='#ffe24c')
    lbname.place(relx=0.3, rely=0.4, anchor=CENTER)
    
        
    entr_name = Entry(gmailwindow,bd=8)
    entr_name.place(relx=0.7, rely=0.4, anchor=CENTER)

    btn_add = Button(gmailwindow, text='Y U B O R I S H ↗️ ', bg='#ffe24c', command=lambda: sendgmail(en_name.get(), entr_name.get()))
    btn_add.place(relx=0.5, rely=0.6 , anchor=CENTER)






# def mekmenu(window):
#     mbar = Menu(window)

#     edmenu = Menu(mbar, tearoff=3)
#     mbar.add_cascade(label="GMAIL ", menu=edmenu)
#     edmenu.add_command(label="YUBORISH", command=lambda:onOpenGmailWindow(window) )


    