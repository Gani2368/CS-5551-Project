from tkinter import *
import tkinter.messagebox

def men():

    root=Tk()

    root.title("MENU")

    root.geometry("1350x650+0+0")
    root.config(bg="black")
    lblmenu = Label(root, text="MENU", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
    lblmenu.grid(row=2,column=8)

    btnvsCOMPUTER = Button(root, text="vsCOMPUTER", width=15, font=('arial', 14, 'bold'), bg='black',
                                   fg='red', bd=8)
    btnvsCOMPUTER.grid(row=4, column=0, pady=5, padx=5)
    btnvsOPPONENT = Button(root, text="vsOPPONENT", width=15, font=('arial', 14, 'bold'), bg='black',
                                   fg='red', bd=8)
    btnvsOPPONENT.grid(row=6, column=0, pady=5, padx=5)
    def Exit():

            root.destroy()

    btnexit = Button(root, text="EXIT", width=15, font=('arial', 14, 'bold'), bg='black',
                                   fg='red', bd=8,command=Exit)
    btnexit.grid(row=8, column=0, pady=5, padx=5)



    root.mainloop()
