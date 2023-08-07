from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from pymysql import*

def clear():
    unameEntry.delete(0,END)
    profEntry.delete(0,END)
    phoneEntry.delete(0,END)
    statusEntry.delete(0,END)
    check.set(0)
    sign2.destroy()
    import main

def  connect_database():
    if unameEntry.get()=='' or statusEntry.get()=='' or profEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','All fields or required')
    elif check.get()==0:
        messagebox.showerror('Error','Agree to the terms and conditions')
    else:
        try:
            con=connect(host='localhost',user='root',password='16022004')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Network issue, Try again')
            return

        mycursor.execute('use userdata')         
        query = 'insert into phone (username,phone) values(%s,%s)'
        mycursor.execute(query,(unameEntry.get(),phoneEntry.get()))
        query = 'insert into profession (username,profession) values(%s,%s)'
        mycursor.execute(query,(unameEntry.get(),profEntry.get()))
        query = 'insert into status (username,status) values(%s,%s)'
        mycursor.execute(query,(unameEntry.get(),statusEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is successful')
        clear()

def login_page():
    sign2.destroy()
    import main

sign2 = Tk()
sign2.title("Signup page")
sign2.resizable(False,False)

background = ImageTk.PhotoImage(file ='bg.jpg' )

bgLabel = Label(sign2,image=background)
bgLabel.grid()

frame = Frame(sign2,bg='white')
frame.place(x=554,y=100)

heading = Label(frame,text='CREATE AN ACCOUNT',
                font = ('Microsoft Yahei UI Light',18,'bold'),
                bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=11,pady=11)

emailLabel = Label(frame,text='Enter Username again',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx = 25,pady=(10,0))

unameEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
unameEntry.grid(row=2,column=0,sticky='w',padx = 25)

usernameLabel = Label(frame,text='Status',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx = 25,pady=(10,0))

statusEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
statusEntry.grid(row=4,column=0,sticky='w',padx = 25 )
statusEntry.insert(0,'Hey there! I\'m using Megagram')

passwordLabel = Label(frame,text='Profession',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx = 25,pady=(10,0))

profEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
profEntry.grid(row=6,column=0,sticky='w',padx = 25 )

confirmLabel = Label(frame,text='Phone number',
                   font=('Microsoft Yahei UI Light',10,'bold'),
                   bg = 'white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx = 25,pady=(10,0))

phoneEntry = Entry(frame,width=30,
                   font=('Microsoft Yahei UI Light',10,'bold'))
phoneEntry.grid(row=8,column=0,sticky='w',padx = 25 )

check = IntVar()

termsandconditions = Checkbutton(frame, text='I agree to the Terms & Conditions',
                                 font=('Microsoft Yahei UI Light',9)
                                 ,fg='grey',bg='white',activebackground='white',
                                 activeforeground='grey',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,sticky='w',padx=25,pady=10)

signupButton=Button(frame,text='Sign up',font=('Open Sans',16,'bold'),
                    fg='white',bg='firebrick1',activebackground='firebrick1',
                    cursor='hand2',bd=0,width=19,activeforeground='white',
                    command=connect_database)
signupButton.grid(row=10,column=0)

alreadyLabel = Label(frame,bg='white',text='Already have an account?',font=('Open Sans',9,'bold'),fg='firebrick1')
alreadyLabel.grid(row = 11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Login',font=('Open Sans',9,'underline'),
                   fg='grey',bg='white',activebackground='white',
                   cursor='hand2',bd=0,activeforeground='firebrick1',command=login_page)
loginButton.place(x=175,y=386)

sign2.mainloop()