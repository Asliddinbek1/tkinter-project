from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from models import District, Fond, Region
from tkinter import messagebox
import smtplib
from gmailts import onOpenGmailWindow

def donothing():
    print("error")

def oncloseTopWindow(window, toplevel):
    window.deiconify()
    window.state('zoomed')
    toplevel.destroy()
    toplevel.geometry('400x200')

def onOpenRegionWindow(window):
    window.withdraw()
    regionwindow = Toplevel()
    regionwindow.protocol('WM_DELETE_WINDOW', lambda: oncloseTopWindow(window, regionwindow))
    regionwindow.title("SINFLAR 1-11 📙 ")
    regionwindow.geometry('1080x600')
    regionwindow.resizable(0, 0)
    regionwindow.configure(bg='#86ff46')

    lb_name = Label(regionwindow, text="S I N F L A R  (KIRITING)➕  ", bg='#ffe24c')
    lb_name.place(relx=0.4,rely=0.1, anchor=CENTER)

    str_region_name = StringVar()

    entry_name = Entry(regionwindow, text=str_region_name, bd=8)
    entry_name.place(relx=0.6,rely=0.1, anchor=CENTER)

    columns = ('region_name', )
    table = ttk.Treeview(regionwindow, columns=columns, show='headings')
    table.heading('region_name', text='S I N F 📍 ')
    table.place(relx=0.5,rely=0.4, anchor=CENTER)

    sel_region = None

    def onAddRegion():
        region = Region(entry_name.get())
        region.save()
        table.insert('', END, iid=region.id, values=region)

    def onClick(event):
        try:
            global sel_region
            id = int(table.focus())
            sel_region = Region.get_by_id(id)
            str_region_name.set(sel_region.name)
        except ValueError as err:
            pass
            #messagebox.showerror("O'chirishda xatolik", str(err))
        except Exception as err:
            messagebox.showerror("XATOLIK ‼️ ", str(err))

    def onUpdateRegion():
        global sel_region
        focused = table.focus()
        sel_region.name = str_region_name.get()
        sel_region.save()
        str_region_name.set('')
        table.item(focused, values=sel_region)
        sel_region = None

    def onDeleteRegion():
        global sel_region
        if sel_region:
            sel_region.delete()
            sel_region = None
            selected_item = table.selection()[0]
            table.delete(selected_item)
    table.bind('<<TreeviewSelect>>', onClick)

    btn_add = Button(regionwindow, text='Q O` S H I S H ➕ ', bg='#ffe24c', command=onAddRegion)
    btn_add.place(relx=0.3,rely=0.7, anchor=CENTER)

    btn_update = Button(regionwindow, text='Y A N G I L A S H ♻️ ', bg='#ffe24c', command=onUpdateRegion)
    btn_update.place(relx=0.5,rely=0.7, anchor=CENTER)


    btn_del = Button(regionwindow, text='O` C H I R I S H ➖ ', bg='#ffe24c', command=onDeleteRegion)
    btn_del.place(relx=0.7,rely=0.7, anchor=CENTER)

    btn_b = Button (regionwindow,  text='Q U I T ⏪ ', bg='#ffe24c', command=regionwindow.quit)
    btn_b.place(relx=0.5,rely=0.8, anchor=CENTER)

    for region in Region.objects():
        table.insert('', END, iid=region.id, values=region)
    
def onOpenDistrictWindow(window):
    window.withdraw()
    districtwindow = Toplevel()
    districtwindow.protocol('WM_DELETE_WINDOW', lambda: oncloseTopWindow(window, districtwindow))
    districtwindow.title("O` Q U V C H I L A R  🚻")
    districtwindow.geometry('1150x500')
    districtwindow.resizable(0, 0)
    districtwindow.configure(background='#86ff46')

    sel_region = None
    cbb_regions = ttk.Combobox(districtwindow, value=tuple(Region.rows()))
    cbb_regions.place(relx=0.3,rely=0.1, anchor=CENTER)
    def selectedRegion(event):
        global sel_region
        array = cbb_regions.get().split(' ')
        id = int(array[0])
        sel_region = Region.get_by_id(id)

    current_var = ()
    
    cbb_regions.bind("<<ComboboxSelected>>", selectedRegion)


    lb_name = Label(districtwindow, text="O` Q U V C H I L A R  🚻➕ ", bg='#ffe24c')
    lb_name.place(relx=0.5,rely=0.1, anchor=CENTER)

    str_district_name = StringVar()
    entry_name = Entry(districtwindow, text=str_district_name, bd=8)
    entry_name.place(relx=0.7,rely=0.1, anchor=CENTER)

    columns = ('region_name', 'district_name')
    table = ttk.Treeview(districtwindow, columns=columns, show='headings')
    table.heading('region_name', text='S I N F L A R ✔️ ')
    table.heading('district_name', text='O` Q U V C H I L A R ✔️ ')
    table.place(relx=0.5,rely=0.4, anchor=CENTER)

    sel_district = None
    def onAddDistrict():
        global sel_region
        district = District(entry_name.get(), sel_region.id)
        district.save()
        table.insert('', END, iid=district.id, values=district)


    def onClick(event):
        global sel_district, sel_region
        try:
            id = int(table.focus())
            sel_district = District.get_by_id(id)
            str_district_name.set(sel_district.name)
            sel_region = Region.get_by_id(sel_district.regionId)
            i = 0
            for item in Region.objects():
                if item.id == sel_district.regionId:
                    break
                i += 1
            cbb_regions.current(i)
        except:
            pass


    def onUpdateDistrict():
        global sel_region, sel_district
        focused = table.focus()
        sel_district.name = str_district_name.get()
        sel_district.save()
        str_district_name.set('')
        table.item(focused, values=sel_district)
        sel_region = None

    def onDeleteDistrict():
        global sel_region, sel_district
        if sel_district:
            sel_district.delete()
            sel_district = None
            selected_item = table.selection()[0]
            table.delete(selected_item)

    table.bind('<<TreeviewSelect>>', onClick)

    btn_add = Button(districtwindow, text='Q O` S H I S H ➕ ', bg='#ffe24c', command=onAddDistrict)
    btn_add.place(relx=0.3,rely=0.7, anchor=CENTER)

    btn_update = Button(districtwindow, text='Y A N G I L A S H ♻️',bg='#ffe24c', command=onUpdateDistrict)
    btn_update.place(relx=0.5,rely=0.7, anchor=CENTER)

    btn_del = Button(districtwindow, text='O` C H I R I S H ➖',bg='#ffe24c', command=onDeleteDistrict)
    btn_del.place(relx=0.7,rely=0.7, anchor=CENTER)
    btn_ba = Button (districtwindow,  text='Q U I T ⏪ ',bg='#ffe24c', command=districtwindow.quit)
    btn_ba.place(relx=0.5,rely=0.8, anchor=CENTER)
    
    for district in District.objects():
        table.insert('', END, iid=district.id, values=district)



def onOpenFondWindow(window):
    window.withdraw()
    fondwindow = Toplevel()
    fondwindow.protocol('WM_DELETE_WINDOW', lambda: oncloseTopWindow(window, fondwindow))
    fondwindow.title("F O N D (m a n u a l)")
    fondwindow.geometry('1150x500')
    fondwindow.resizable(0, 0)
    fondwindow.configure(background='#86ff46')


    sel_region = None
    bb_regions = ttk.Combobox(fondwindow, value=tuple(Region.rows()))
    bb_regions.grid(row=0, column=0)
    def selectedRegion(event):
        global sel_region
        array = bb_regions.get().split(' ')
        id = int(array[0])
        sel_region = Region.get_by_id(id)

    current_var = ()


    sel_district= None

    cbb_district = ttk.Combobox(fondwindow, value=tuple(District.rows()))
    cbb_district.grid(row=0, column=1)
    def selectedDistrict(event):
        global sel_district
        array = cbb_district.get().split(' ')
        id = int(array[0])
        sel_district = District.get_by_id(id)

    current_var = ()
    
    cbb_district.bind("<<ComboboxSelected>>", selectedDistrict)

    lb_nam = Label(fondwindow, text="O` Q U V C H I L A R  🚻➕ ", bg='#ffe24c')
    lb_nam.grid(row=0, column=1)

    str_fond_name = StringVar()
    entry_nam = Entry(fondwindow, text=str_fond_name)
    entry_nam.grid(row=0, column=2)



    columns = ('region_name', 'district_name', 'fond_name')
    table = ttk.Treeview(fondwindow, columns=columns, show='headings')
    table.heading('region_name', text='S I N F L A R ✔️ ')
    table.heading('district_name', text='O` Q U V C H I L A R ✔️ ')
    table.heading('fond_name', text='F O N D ✔️ ')
    table.grid(row=1, column=0, columnspan=3)

    sel_fond = None
    def onAddFond():
        global sel_district
        fond = Fond(entry_nam.get(), sel_district.id)
        fond.save()
        table.insert('', END, iid=fond.id, values=fond)


    def onClick(event):
        global sel_region, sel_fond, sel_district
        try:
            id = int(table.focus())
            sel_fond = District.get_by_id(id)
            str_fond_name.set(sel_fond.name)
            sel_district = District.get_by_id(sel_fond.districtId)
            i = 0
            for item in District.objects():
                if item.id == sel_fond.districtId:
                    break
                i += 1
            cbb_district.current(i)
        except:
            pass

    def onUpdateFond():
        global sel_region, sel_district, sel_fond
        focused = table.focus()
        sel_fond.name = str_fond_name.get()
        sel_fond.save()
        str_fond_name.set('')
        table.item(focused, values=sel_fond)
        sel_district = None

    def onDeleteFond():
        global sel_region, sel_district, sel_fond
        if sel_fond:
            sel_fond.delete()
            sel_fond = None
            selected_item = table.selection()[0]
            table.delete(selected_item)

    table.bind('<<TreeviewSelect>>', onClick)

    tn_add = Button(fondwindow, text='Q O` S H I S H ➕ ', bg='#ffe24c', command=onAddFond)
    tn_add.place(relx=1,rely=1, anchor=SE)

    tn_update = Button(fondwindow, text='Y A N G I L A S H ♻️',bg='#ffe24c', command=onUpdateFond)
    tn_update.grid(row=0, column=4)

    tn_del = Button(fondwindow, text='O` C H I R I S H ➖',bg='#ffe24c', command=onDeleteFond)
    tn_del.grid(row=0, column=5)

    tn_ba = Button (fondwindow,  text='B A C K',bg='#ffe24c', command=fondwindow.quit)
    tn_ba.grid(row=0, column=6)
    
    for fond in Fond.objects():
        table.insert('', END, iid=fond.id, values=fond)





def Faq(window):
    mal = """
    ❤️ ASSALOMU ALEYKUM ❤️ 
    Siz bu dastur orqali maktab jamg`arma ishlari  
    va ro`yhat malumotlarini kiritishingiz 
    yangilash va o`chirish orqali mumtazam  
    foydalanishingiz mumkin  | Nashr 2022 | 🇺🇿  🆓 
     💻 : Asliddin Abdullayev 
    """
    #showinfo(window, mal)
    messagebox.showinfo(title='FAQ', message=mal)






# def gmail(window):
    

#     sender = '14.maktab.rektorant@gmail.com'
#     receiver = ''
#     password = 'your_password'
#     smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
#     smtpserver.ehlo()
#     smtpserver.starttls()
#     smtpserver.ehlo
#     smtpserver.login(sender, password)
#     msg = ''
#     smtpserver.sendmail(sender, receiver, msg)
#     print('Sent')
#     smtpserver.close()


#     window.withdraw()
#     gmailwindow = Toplevel()
#     gmailwindow.protocol('WM_DELETE_WINDOW', lambda: oncloseTopWindow(window, gmailwindow))
#     gmailwindow.title("G M A I L  📧 ")
#     gmailwindow.geometry('1100x500')
#     gmailwindow.resizable(0, 0)


#     b_name = Label(gmailwindow, text="O`QUVCHI GMAILI: ")
#     b_name.pack(padx=0.5, column=0.5, anchor= CENTER)

#     b_name = Label(gmailwindow, text="XABAR YOZISH: ")
#     b_name.pack(padx=0.5, pady=0.5,anchor= CENTER)



#     receiver = StringVar()
#     entry_name = Entry(gmailwindow, text=receiver, bg='red')
#     entry_name.grid(row=0, column=2)


#     msg = StringVar()
#     entry_name = Entry(gmailwindow, text=msg, bg='red')
#     entry_name.grid(row=1, column=2)

#     bbtn_add = Button(gmailwindow, text='YUBORISH', command=RUN, bg='brown')
#     bbtn_add.grid(row=0, column=3)




def makeMenu(window):
    menubar = Menu(window)

    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="CHiqish ⏪ ", menu=editmenu)

    # filemenu.add_command(label="New", command=donothing)
    # filemenu.add_command(label="Open", command=donothing)
    # filemenu.add_command(label="Save", command=donothing)
    # filemenu.add_command(label="Close", command=donothing)
    # filemenu.add_separator()
    editmenu.add_command(label="Exit", command=window.quit)


    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="FAQ ❗️  ", menu=filemenu)
    filemenu.add_command(label="Malumot ❓ ", command=lambda:Faq(window))


    # gmailmenu = Menu(menubar, tearoff=3)
    # menubar.add_cascade(Label= 'GMAILGA XABAR ✉️ ', menu=gmailmenu)
    # gmailmenu.add_command(label='O`QUVCHIGA XABAR YOZISH', command=gmaill(window))
    

    # editmenu = Menu(menubar, tearoff=0)
    # menubar.add_cascade(label="Edit", menu=editmenu)
    # editmenu.add_command(label="Undo", command=donothing)
    # editmenu.add_separator()
    # editmenu.add_command(label="Cut", command=donothing)
    # editmenu.add_command(label="Copy", command=donothing)
    # editmenu.add_command(label="Paste", command=donothing)
    # editmenu.add_command(label="Delete", command=donothing)

    servicemenu= Menu(menubar, tearoff=1)
    menubar.add_cascade(label="RO`YHAT TO`LDIRISH   📝   ", menu=servicemenu)
    servicemenu.add_separator()
    servicemenu.add_command(label=" S i n f l a r  🔎 ", command=lambda: onOpenRegionWindow(window))
    servicemenu.add_command(label="O` q u v c h i l a r   🧑‍🎓  ", command=lambda: onOpenDistrictWindow(window))
    #servicemenu.add_command(label="X A B A R L A R 📧  ", command=lambda: gmail(window))
    servicemenu.add_command(label="F o n d ( maktab jamg`armasi )  💰  ", command=lambda: onOpenFondWindow(window))
    #servicemenu.add_command(label="O` q t u v c h i l a r (yillik ro`yhat)   🧑‍🏫   ", command=lambda: onOpenDistrictWindow(window))

    # srvicemenu = Menu(menubar, tearoff=2)
    # menubar.add_cascade(label="RO`YXAT (ALL)   📄   ", menu=srvicemenu)
    # srvicemenu.add_command(label=" S i n f l a r  🔎 ", command=lambda: onOpenRegionWindow(window))
    # srvicemenu.add_command(label="O` q u v c h i l a r   🧑‍🎓  ", command=lambda: onOpenDistrictWindow(window))
    # srvicemenu.add_command(label="F o n d ( yillik davlat uchun )  💰  ", command=lambda: onOpenDistrictWindow(window))
    # srvicemenu.add_command(label="F o n d ( maktab jamg`armasi )  💰  ", command=lambda: onOpenDistrictWindow(window))
    # srvicemenu.add_command(label="O` q t u v c h i l a r (yillik ro`yhat)   🧑‍🏫   ", command=lambda: onOpenDistrictWindow(window))
   
   
   


    edmenu = Menu(menubar, tearoff=3)
    
    menubar.add_cascade(label="GMAIL  📭 ", menu=edmenu)
    edmenu.add_command(label="YUBORISH  🗳 ", command=lambda:onOpenGmailWindow(window))


    
   
   
   
   
   
   
   
    return menubar


# def MakeMenu(districtwindow):
#     menub = Menu(districtwindow)

#     edi = Menu(menub, tearoff=0)
#     menub.add_cascade(label="CHiqish ⏪ ", menu=edi)
    
#     return menub
