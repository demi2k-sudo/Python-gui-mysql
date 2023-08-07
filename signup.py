from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from pymysql import*

def clear():
    emailEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    usernameEntry.delete(0,END)
    signup_window.destroy()
    import signup2

def  connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All fields or required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Confirm password again')

    else:
        try:
            con=connect(host='localhost',user='root',password='16022004')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Network issue, Try again')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        
        query = 'select* from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row = mycursor.fetchone()
        
        if row != None:
            messagebox.showerror('Error','Username already exists')
        
        else:          
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            
            clear()


signup_window = Tk()
signup_window.title("Signup page")
signup_window.resizable(False,False)

background = ImageTk.PhotoImage(file ='bg.jpg' )

bgLabel = Label(signup_window,image=background)
bgLabel.grid()

frame = Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading = Label(frame,text='CREATE AN ACCOUNT',
                font = ('Microsoft Yahei UI Light',18,'bold'),
                bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=11,pady=11)

emailLabel = Label(frame,text='Email',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx = 25,pady=(10,0))

emailEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
emailEntry.grid(row=2,column=0,sticky='w',padx = 25)

usernameLabel = Label(frame,text='Username',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx = 25,pady=(10,0))

usernameEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
usernameEntry.grid(row=4,column=0,sticky='w',padx = 25 )

passwordLabel = Label(frame,text='Password',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx = 25,pady=(10,0))

passwordEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
passwordEntry.grid(row=6,column=0,sticky='w',padx = 25 )

confirmLabel = Label(frame,text='Confirm Password',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx = 25,pady=(10,0))

confirmEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
confirmEntry.grid(row=8,column=0,sticky='w',padx = 25,pady=(0,10))

check = IntVar()

signupButton=Button(frame,text='NEXT',font=('Open Sans',16,'bold'),
                    fg='white',bg='firebrick1',activebackground='firebrick1',
                    cursor='hand2',bd=0,width=19,activeforeground='white',
                    command=connect_database)
signupButton.grid(row=10,column=0)


signup_window.mainloop()