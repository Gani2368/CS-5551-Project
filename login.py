from tkinter import *
import tkinter.messagebox
from PIL import Image
import menu





def main():
    root=Tk()
    app=americancheckersLogin(root)
    if __name__ == '__main__':
        root.mainloop()
class americancheckersLogin:
    def __init__(self,master):
        self.master=master
        self.master.title("Americancheckers Login")
        self.master.geometry("1350x650+0+0")
        self.master.config(bg='black')
        self.frame=Frame(self.master, width=50,height=50,bg='black')
        self.frame.pack()
        self.Username=StringVar()
        self.Password = StringVar()
       # self.photo2 = ImageTk.PhotoImage(file='payroll.jpg')
        #self.photo = Label(self.frame, image=self.photo2, bg='white')
        #self.photo.grid(row=1, column=0)
        self.lb1Title = Label(self.frame, text="AMERICAN CHECKERS",font=('arial',50,'bold'),bg='black',fg='red')
        self.lb1Title.grid(row=0, column=0, columnspan=2, pady=20)
        self.LoginFrame1 = LabelFrame(self.frame, width=50, height=50, text="Login", font=('arial', 20, 'bold'),
                                      relief='ridge', bg='black', bd=0, fg='red')
        self.LoginFrame1.grid(row=2, column=0)
        self.LoginFrame2 = LabelFrame(self.frame, width=50, height=50, font=('arial', 20,
                                                                             'bold'), relief='ridge',
                                      bg='black', bd=0, fg='red')
        self.LoginFrame2.grid(row=3, column=0)

        self.lblUsername = Label(self.LoginFrame1, text="Username", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.lblUsername.grid(row=2, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font=('arial', 16, 'bold'), bd=5, textvariable=self.Username
                                 , width=33)
        self.txtUsername.grid(row=2, column=1, padx=10)
        self.lblPassword = Label(self.LoginFrame1, text="Password", font=('arial', 20, 'bold'), bd=15, bg='black',fg='red')
        self.lblPassword.grid(row=3, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('arial', 16, 'bold'), show='*', bd=5, textvariable=self.Password, width=33)
        self.txtPassword.grid(row=3, column=1, columnspan=2, pady=5)

        self.btnLogin = Button(self.LoginFrame2, text="Login", width=10, font=('arial', 14, 'bold'), bg='black',
                               fg='red', command=self.Login_System, bd=8)
        self.btnLogin.grid(row=4, column=0, pady=5, padx=5)
        self.btnReset = Button(self.LoginFrame2, text="Reset", width=10, font=('arial', 14,
                                                                               'bold'), bg='black', bd=8,
                               fg='red', command=self.iReset)
        self.btnReset.grid(row=4, column=1, pady=5, padx=5)
        self.btnExit = Button(self.LoginFrame2, text="Exit", width=10, font=('arial', 14,
                                                                             'bold'), bg='black', bd=8,
                              fg='red', command=self.iExit)
        self.btnExit.grid(row=4, column=2, pady=5, padx=5)
    def log(self):
        menu.men()



    def Login_System(self):
            user = (self.Username.get())

            pas = (self.Password.get())
            if user == str('gani') and pas == str('2368'):
                self.log()
            else:
                tkinter.messagebox.askyesno("American checkers Login", "Invalid Login Details")
                self.Username.set("")
                self.Password.set("")

    def iReset(self):
            self.Username.set("")

            self.Password.set("")

    def iExit(self):
            self.iExit = tkinter.messagebox.askyesno("American checkers Login System", "Confirm if you want to exit  ")
            if self.iExit > 0:
                self.master.destroy()
                return
if __name__ == "__main__":
    main()
