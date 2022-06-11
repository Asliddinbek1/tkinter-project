from tkinter import *

from menu import  makeMenu
#from websitetk import root



window = Tk()
window.title(" 🏫  14-MAKTAB FOND HISOBI 🏦 : Umumiy maktab sinflar malumot jamlanmasi" " Maktab kotibasi uchun nashr . Kotiba : A.S.jabborova 👩🏿‍💻 ")
from styles import style
window.configure(bg='#ffe24c')


bt_del = Button(window, text='Q U I T ⏪ ', bg='#86ff46', command=window.quit)
bt_del.place(relx=1.0, rely=1.0, anchor=SE)
    
# bt_gm = Button(window, text='GMAILGA MUROJAT  📡', bg='#ffe24c', command=gmailts)
# bt_gm.place(relx=0.8, rely=1.0, anchor=SE)


menubar = makeMenu(window)
window.config(menu=menubar)
window.state('zoomed')



# mbar = mekmenu(window)
# window.config(menu=mbar)
# window.state('zoomed')





window.mainloop()
