import tkinter
from tkinter import *
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", password="12345",database="registerdb",port=3310 )

root = tkinter.Tk()
root.withdraw()
username = StringVar()
Password = StringVar()

def loginForm():
    def loginUser():
        name = str(username.get())
        password = str(Password.get())
        mydb = mysql.connector.connect(host="localhost", user="root", password="12345", database="registerdb",port=3310)
        mycursor = mydb.cursor()
        sql = "select * from registration where username = %s and password = %s"
        mycursor.execute(sql, [(name), (password)])
        results = mycursor.fetchall()

        if results:
            for i in results:
                print(name,password)
                break
            root.withdraw()
            print('Successfully Login')
            welcome=Tk()
            welcome.geometry("450x230")
            welcome.title('Welcome')
            newLabel=Label(welcome,text="Congratulations you successfully logged in!",font=('arial',13),fg='blue')
            newLabel.pack(pady=30)
            welcome.mainloop()
        else:
            wrongPassword=Label(root,text="Pass or Username is wrong, Try Again!!!!",fg='red')
            wrongPassword.place(x='230', y='125')

    root.deiconify()
    root.title("Login Form")
    root.geometry("450x230")

    usernameLable = Label(root, text="Username: ")
    usernameLable.place(x='70', y='50')

    passwordLable = Label(root, text="Password: ")
    passwordLable.place(x='70', y='80')
    global username, Password

    usernameBox = Entry(root, width='30', textvariable=username)
    usernameBox.place(x='150', y='50')

    passwordBox = Entry(root, width='30', textvariable=Password)
    passwordBox.place(x='150', y='80')

    loginButton = Button(root, text="Login", command=loginUser)
    loginButton.place(x='150', y='120', width='60')

    root.mainloop()



def registrationForm():
    def saveDataintoDB():
        name = str(usernameBox.get())
        password = str(passwordBox.get())
        mycursor = mydb.cursor()
        result = Label(register, text="", font=('arial', 12))
        result.place(x='100', y='160')

        if name == "" or password == "":
            result.config(text="Please complete the required field!", fg="orange")

        else:
            mycursor.execute("SELECT * FROM `registration` WHERE `username` = %s", [name])
            if mycursor.fetchone() is not None:
                result.config(text="Username is already Exist,Try Again!", fg="red")
            else:

                sql = "INSERT INTO registration (username, password) VALUES (%s, %s)"
                val = (name, password)
                mycursor.execute(sql, val)
                mydb.commit()
                print(name)
                print(password)
                print('Data Saved Successfully')
                mydb.close()
                savedData = Tk()
                register.destroy()
                savedData.geometry("450x230")
                savedData.title('Data Saved Successfully')
                newLabel = Label(savedData, text="Data Saved Into MYSQL Database Successfully",font=('arial',13),fg='blue')
                
                newLabel.pack(pady=10)
                newLabel1 = Label(savedData, text="Thank You",font=('arial',13),fg='orange')
                newLabel1.pack(pady=10)
                savedData.mainloop()

    register = tkinter.Tk()
    print('Register New User')
    register.geometry("450x230")
    register.title('Register New User')
    newLabel = Label(register, text="Register New User!", font=('arial',13),fg='blue')
    newLabel.pack(pady=10)

    usernameLable = Label(register, text="Enter-Username: ")
    usernameLable.place(x='70', y='50')

    passwordLable = Label(register, text="Enter-Password: ")
    passwordLable.place(x='70', y='80')

    usernameBox = Entry(register, width='30')
    usernameBox.place(x='165', y='50')

    passwordBox = Entry(register, width='30')
    passwordBox.place(x='165', y='80')

    saveDataButton = Button(register, text="Save-Data", command=saveDataintoDB)
    saveDataButton.place(x='165', y='125', width='80')

    register.mainloop()


def makeChoice():
    choice=tkinter.Tk()
    choice.title("Login Authentication System")
    choice.geometry("450x230")

    newLabel = Label(choice, text="Click Anyone Below!",font=('arial',15),fg='blue')
    newLabel.pack(pady=50)

    LoginButton = Button(choice, text="Login Form", command=loginForm)
    LoginButton.place(x='70', y='100',width='150')

    RegistrationButton = Button(choice, text="Registration Form", command=registrationForm)
    RegistrationButton.place(x='250', y='100',width='150')
    choice.mainloop()

makeChoice()






