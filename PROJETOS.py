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

btn4 = Button(fr_quadro1, text="PROJETO SWITCH", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1Fe78a_yhU25Kf-xcZGNRVENBVxnxv2QPxZVM89ZMcsk/edit?usp=sharing'))
btn4.place(x=10, y=150)

############################################################################################
label3 = tkinter.Label(fr_quadro2, text="CITI:", font="arial 11 bold", fg="white", bg="#006494")
label3.place(x=70, y=10)

btn6 = Button(fr_quadro2, text="PROJETO REDE SEDE", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1E8JWB5KX0I1KHT-mHcSvd3k6ma0gYeJwEtUM_eluJ28/edit?usp=sharing'))
btn6.place(x=10, y=60)

btn7 = Button(fr_quadro2, text="PROJETO MANUTENÇÃO FIBRA", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1L28nyzWYh8tUlvKIJVBZGm5zDGQoz0RWasxVSm5MR7k/edit?usp=sharing'))
btn7.place(x=10, y=90)

btn8 = Button(fr_quadro2, text="PROJETO SUPRIMENTOS TI", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1c14cjP8qLQQWna0X8Vz9zEvQgtUOW93IBgCtsXb5yXA/edit?usp=sharing'))
btn8.place(x=10, y=120)
############################################################################################
label4 = tkinter.Label(fr_quadro3, text="CABD:", font="arial 11 bold", fg="white", bg="#006494")
label4.place(x=80, y=10)

btn9 = Button(fr_quadro3, text="SUPORTE ORACLE", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1LhBnhVOWkW8bJf9MAcPs-6yovgMW4NzI6jv4Y6wDrIY/edit?usp=sharing'))
btn9.place(x=10, y=60)
############################################################################################
label5 = tkinter.Label(fr_quadro4, text="CAD:", font="arial 11 bold", fg="white", bg="#006494")
label5.place(x=90, y=10)

btn10 = Button(fr_quadro4, text="WORK WITH PLUS", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1oHIJ-qxu1YSKZwMiKjFoSDSyoD6kvSXIM8Nl-15dSpU/edit?usp=sharing'))
btn10.place(x=10, y=60)

btn11 = Button(fr_quadro4, text="GENEXUS", bg="#89CFF0", font="arial 9 bold", command=lambda: webbrowser.open('https://docs.google.com/document/d/1I_6li-R463wz6x77hIIzaX07pNOnnjBNMUFHt0nE76c/edit?usp=sharing'))
btn11.place(x=10, y=90)

############################################################################################

app.mainloop()








