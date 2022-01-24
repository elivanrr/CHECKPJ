import tkinter
from tkinter import *
import webbrowser

app = Tk()
app.title("CHECK-LIST DE PROJETOS")
app.geometry("920x400")

label1 = tkinter.Label(master=app, text="ESCOLHA A COORDENAÇÃO E O PROJETO", font="arial 11 bold", fg="white", bg="#006494")
label1.place(x=300, y=0)
fr_quadro1 = Frame(app, borderwidth=1, relief="solid")
fr_quadro1.place(x=50, y=50, width=200, height=300)

fr_quadro2 = Frame(app, borderwidth=1, relief="solid")
fr_quadro2.place(x=260, y=50, width=200, height=300)

fr_quadro3 = Frame(app, borderwidth=1, relief="solid")
fr_quadro3.place(x=470, y=50, width=200, height=300)

fr_quadro4 = Frame(app, borderwidth=1, relief="solid")
fr_quadro4.place(x=680, y=50, width=200, height=300)
############################################################################################
label2 = tkinter.Label(fr_quadro1, text="CARCD:", font="arial 11 bold", fg="white", bg="#006494")
label2.place(x=60, y=10)

btn1 = Button(fr_quadro1, text="PROJETO UST", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1oYj3CfoQvGHGN6Puvq1KgmDbFCS1l8Thg-ZOPZ_dK-Y/edit?usp=sharing'))
btn1.place(x=10, y=60)

btn2 = Button(fr_quadro1, text="PROJETO BACKUP", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1MHZUTD4S2nZaR1gz5fKD8Y-L74gqMuYb3MGZOky04RA/edit?usp=sharing'))
btn2.place(x=10, y=90)

btn3 = Button(fr_quadro1, text="PROJETO FIREWALL", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/12352zDpnOkTojZ79pjGONxVTzWJ1felMXAttGFrjnVg/edit?usp=sharing'))
btn3.place(x=10, y=120)

############################################################################################
label3 = tkinter.Label(fr_quadro2, text="CITI:", font="arial 11 bold", fg="white", bg="#006494")
label3.place(x=70, y=10)

btn6 = Button(fr_quadro2, text="PROJETO REDE SEDE", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/12352zDpnOkTojZ79pjGONxVTzWJ1felMXAttGFrjnVg/edit?usp=sharing'))
btn6.place(x=10, y=60)

btn7 = Button(fr_quadro2, text="PROJETO MANUTENÇÃO FIBRA", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1L28nyzWYh8tUlvKIJVBZGm5zDGQoz0RWasxVSm5MR7k/edit?usp=sharing'))
btn7.place(x=10, y=90)
############################################################################################
label4 = tkinter.Label(fr_quadro3, text="CABD:", font="arial 11 bold", fg="white", bg="#006494")
label4.place(x=80, y=10)
############################################################################################
label4 = tkinter.Label(fr_quadro4, text="CAD:", font="arial 11 bold", fg="white", bg="#006494")
label4.place(x=90, y=10)
############################################################################################

app.mainloop()



