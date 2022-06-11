import webbrowser
from tkinter import *
from aiohttp import payload_type

root = Tk()

root.title("Web saytlardan foydalanish 🌐 ")
root.geometry("1100x600")
root.configure(background='#ffe24c')

def instagram():

    webbrowser.open("https://www.instagram.com/14_maktab_news/")

def twitter():

    webbrowser.open("https://login.kundalik.com/")

def youtube():

    webbrowser.open("https://www.youtube.com/results?search_query=kundalik+kom+rasmiy")

def whatsappweb():

    webbrowser.open("https://chat.whatsapp.com/LqyHsiQuozEKoHuvjiC0qp")

def telegram():

    webbrowser.open("https://t.me/maktab14bekobod")

def bot():

    webbrowser.open("https://t.me/Odamemasbot")


# def gaamee():
#     root = Tk()   
#     width = 900
#     height = 500

#     canvas = tk.Canvas(root, bg='white', width=width, height=height)
#     canvas.pack()

#     ball = canvas.create_oval(430, 10, 470, 50, fill='green')

#     platform_y = height - 20
#     platform = canvas.create_rectangle(width//2-50, platform_y, width//2+50, platform_y+10, fill='black')

#     # ball moving speed
#     xspeed = yspeed = 2
#    # move_ball()

Label(root, text="⬇️KERAKLI PLATFORMALARNI OCHISH  ⬇️", font="Helvtica 12 bold", bg='#86ff46').pack()


bt_de = Button(root, text=' RO`YHATNI OCHISH  💲  ', bg='#c8ff62', command=root.quit, font="LUCIDA 12 bold").pack(padx=20, pady=20)


myinstagram = Button(root, text="     INSTAGRAM    📸  ", bg="#c8ff62", command=instagram,font="LUCIDA 12 bold").pack(padx=20,pady=20)

#mytwitter = Button(root, text="TWITTER", bg="skyblue", command=twitter,font="LUCIDA 12 bold").pack(padx=20,pady=20)

myyoutube = Button(root, text="KUNDALIK.COM YT▶️",bg="#c8ff62", command=youtube,font="LUCIDA 12 bold").pack(padx=20,pady=20)

mywhatsapp = Button(root, text="WHATSAPP WEB 📞 ", bg="#c8ff62", command=whatsappweb,font="LUCIDA 12 bold").pack(padx=20,pady=20)

mytelegram= Button(root, text="  TELEGRAM  ✈️   " , bg="#c8ff62", command=telegram,font="LUCIDA 12 bold").pack(padx=20,pady=20)

myyoutube = Button(root, text="KUNDALIK.COM WEB🌐",bg="#c8ff62", command=twitter,font="LUCIDA 12 bold").pack(padx=20, pady=20)

mybot = Button(root, text='7/24 YORDAM BOT  🤖 ', bg="#c8ff62", command=bot,font="LUCIDA 12 bold",).pack(padx=20, pady=20)

# mygame = Button(root, text=' G A M E ' , bd="#c8ff62", command=gaamee, font="LUCIDA 12 bold",).pack(padx=20, pady=20)

font="LUCIDA 12 bold"

root.mainloop()