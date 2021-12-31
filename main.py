import webbrowser
from tkinter import *
from selenium import webdriver

app = Tk()
app.title("CHECK PROJETOS")
app.geometry('{}x{}'.format(300, 250))

btn1 = Button(app, text="Projeto UST", bg="gray", command=lambda: webbrowser.open('https://docs.google.com/document/d/1oYj3CfoQvGHGN6Puvq1KgmDbFCS1l8Thg-ZOPZ_dK-Y/edit?usp=sharing'))
btn1.pack(padx=5, pady=5)
#btn1.grid(row=0, column=2, padx=5, pady=5)
btn2 = Button(app, text="Projeto BCK", bg="gray", command=lambda: webbrowser.open('https://docs.google.com/document/d/13W-6s_QUmcrtjJtZbRWPBEIY8S_r8HH1Ae8HK0WyPHc/edit?usp=sharing'))
btn2.pack(padx=5, pady=5)
#btn2.grid(row=1, column=2, padx=5, pady=5)

app.mainloop()



# codigos de teste
#def ust():'
    #driver = webdriver.Chrome(executable_path="./chromedriver.exe").get('https://docs.google.com/document/d/1oYj3CfoQvGHGN6Puvq1KgmDbFCS1l8Thg-ZOPZ_dK-Y/edit?usp=sharing')
    #driver.get('https://docs.google.com/document/d/1oYj3CfoQvGHGN6Puvq1KgmDbFCS1l8Thg-ZOPZ_dK-Y/edit?usp=sharing')
#ust()



