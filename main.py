from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def notes_func():
    def save():
        query = 'select note from notes where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        n = mycursor.fetchone()
        if (n!=None):
            query = 'delete from notes where username=%s'
            mycursor.execute(query,(usernameEntry.get()))
        query = 'insert into notes(username,note) values(%s,%s)'
        mycursor.execute(query,(usernameEntry.get(),noteEntry.get())) 
        con.commit()
    try:
        con=pymysql.connect(host='localhost',user='root',password='16022004')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error', 'Connection not estabilished')
        return
    query = 'use userdata'
    mycursor.execute(query)
    notepg = Toplevel()
    notepg.resizable(0,0)
    notepg.title('Tweets')
    nimage = ImageTk.PhotoImage(file='note.png')
    bgn = Label(notepg,image=nimage)
    bgn.pack() 
    noteEntry = Entry(notepg,width =25, font=('Courier new',11,'bold'),bd=1 )
    noteEntry.place(x=45,y=100,height=230)
    query = 'select note from notes where username=%s'
    mycursor.execute(query,(usernameEntry.get()))
    n = mycursor.fetchone()
    if (n!=None):
        noteEntry.insert(0,n[0])
    saveButton = Button(notepg,text='save',cursor='hand2',bd=0,bg='white',command=save)
    saveButton.place(x=120,y=350)
    notepg.mainloop()     
       
def call_contact():

    def dial():
        def cut():
            dialpg.destroy()
        dialpg = Toplevel()
        dialpg.resizable(0,0)
        dialpg.title('Calling')
        dimage = ImageTk.PhotoImage(file='dial.png')
        bgd = Label(dialpg,image=dimage)
        bgd.pack()
        cutimg = PhotoImage(file='cut.png')
        cutButton = Button(dialpg,image=cutimg,cursor='hand2',bd=0,bg='white',command=cut)
        cutButton.place(x=120,y=350)
        conlabel = Label(dialpg,text='Connected.',font = ('Courier new',12,'bold'),bg='white',fg='firebrick3')
        conlabel.place(x=100,y=320)
        contlabel = Label(dialpg,text=contactEntry.get(),font = ('Courier new',15,'bold'),bg='white',fg='firebrick3')
        contlabel.place(x=100,y=270)
        dialpg.mainloop()
        
    def search():
        contactname = contactEntry.get()
        query = 'select * from data where username=%s'
        mycursor.execute(query,(contactEntry.get()))
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','The person is not in MegaGram',parent = contact)
        else:
            name = Label(contact,text=contactname,font = ('Courier new',18,'bold'),fg='firebrick3',bg='white')
            name.place(x=100,y=375)
            ringimg = PhotoImage(file='ring.png')
            ringButton = Button(contact,image=ringimg,cursor='hand2',bd=0,bg='white',command=dial)
            ringButton.place(x=150,y=450)
            contact.mainloop()
                        
    try:
        con=pymysql.connect(host='localhost',user='root',password='16022004')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error', 'Connection not estabilished')
        return
    query = 'use userdata'
    mycursor.execute(query)
    contact = Toplevel()
    contact.resizable(0,0)
    contact.title('Contacts')
    cimage = ImageTk.PhotoImage(file='people.png')
    bgc = Label(contact,image=cimage)
    bgc.pack()      
    contactEntry = Entry(contact,width = 20, font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick3' )
    contactEntry.place(x=85,y=275)
    searchimg = PhotoImage(file='lens.png')
    searchButton = Button(contact,image=searchimg,bd=0,cursor='hand2',command=search)
    searchButton.place(x=275,y=275)
    contact.mainloop()

def profile_info():
    try:
        con=pymysql.connect(host='localhost',user='root',password='16022004')
        mycursor=con.cursor()
    except:
        messagebox.showerror('Error', 'Connection not estabilished')
        return
    query = 'use userdata'
    mycursor.execute(query)
    query = 'select * from data where username=%s and password=%s'
    username = usernameEntry.get()
    mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
    row = mycursor.fetchone()
    
    popup = Toplevel()
    popup.resizable(0,0)
    popup.title('User info')
    pimage = ImageTk.PhotoImage(file='pop.jpg')
    bgpop = Label(popup,image=pimage)
    bgpop.pack()       
    heading2 = Label(popup,text='User Info',font = ('Arial',23),borderwidth=1,relief='solid')
    heading2.place(x=100,y=30)
    query = 'select * from phone where username=%s'
    mycursor.execute(query,(username))
    phone = mycursor.fetchone()[1]
    query = 'select * from profession where username=%s'
    mycursor.execute(query,(username))
    profession = mycursor.fetchone()[1]
    query = 'select * from status where username=%s'
    mycursor.execute(query,(username))
    status = mycursor.fetchone()[1]
    query = 'select email from data where username=%s'
    mycursor.execute(query,(username))
    email = mycursor.fetchone()[0]
    print(phone,profession,status,email)
    usernameOp = Label(popup,text='Username :'+username,font = ('Courier new',12,'bold'),borderwidth=1,relief='solid')
    usernameOp.place(x=35,y=100)
    mailOp = Label(popup,text='Mail: '+email,font = ('Courier new',12,'bold'),borderwidth=1,relief='solid')
    mailOp.place(x=35,y=150)
    statOp = Label(popup,text=status,font = ('Courier new',12,'bold'),borderwidth=1,relief='solid')
    statOp.place(x=35,y=200)
    profOp = Label(popup,text='My profession: '+profession,font = ('Courier new',12,'bold'),borderwidth=1,relief='solid')
    profOp.place(x=35,y=250)
    contactOp = Label(popup,text='Contact: '+phone,font = ('Courier new',12,'bold'),borderwidth=1,relief='solid')
    contactOp.place(x=35,y=300)
    popup.mainloop()
                
def signup_page():
    login_window.destroy()
    import signup

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get() =='':
        messagebox.showerror('error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='16022004')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection not estabilished')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            menu = Toplevel()
            menu.resizable(0,0)
            
            menu.title('Menu')
            mimage = ImageTk.PhotoImage(file='menu.png')
            bgmenu = Label(menu,image=mimage)
            bgmenu.pack()       
            
            call = PhotoImage(file='call.png')
            callButton = Button(menu,image=call,bd=0,cursor='hand2',command=call_contact)
            callButton.place(x=100,y=300)
            
            notes = PhotoImage(file='notes.png')
            notesButton = Button(menu,image=notes,bd=0,cursor='hand2',command=notes_func)
            notesButton.place(x=200,y=300)
            
            profile = PhotoImage(file='profile.png')
            profileButton = Button(menu,image=profile,bd=0,cursor='hand2',command=profile_info)
            profileButton.place(x=300,y=300)
            menu.mainloop()
                        
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        passwordEntry.config(show='*')

login_window = Tk()
login_window.resizable(0,0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)

heading = Label(login_window,text='USER LOGIN',font = ('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry = Entry(login_window,width = 25, font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick3' )
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

Frame(login_window,width=250,height=2).place(x=580,y=222)

passwordEntry = Entry(login_window,width = 25, font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick3' )
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

Frame(login_window,width=250,height=2).place(x=580,y=282)

openeye=PhotoImage(file='closeye.png')
eyeButton = Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
eyeButton.place(x=800,y=255)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',
                   activebackground='firebrick1',cursor='hand2',bd=0,width=19,activeforeground='white'
                   ,command=login_user)
loginButton.place(x=578,y=350)

orLabel = Label(login_window,bg='white',text='-------------- OR --------------',font=('Open Sans',16),fg='firebrick1')
orLabel.place(x=583,y=400)

facebook_Logo = PhotoImage(file='facebook.png')
fbButton = Button(login_window,image=facebook_Logo,bd=0,bg='white',activebackground='white',cursor='hand2')
fbButton.place(x=640,y=440)

google_Logo = PhotoImage(file='google.png')
googleButton = Button(login_window,image=google_Logo,bd=0,bg='white',activebackground='white',cursor='hand2')
googleButton.place(x=690,y=440)

twitter_Logo = PhotoImage(file='twitter.png')
twitterButton = Button(login_window,image=twitter_Logo,bd=0,bg='white',activebackground='white',cursor='hand2')
twitterButton.place(x=740,y=440)

signupLabel = Label(login_window,bg='white',text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new account',font=('Open Sans',9,'underline'),fg='grey',bg='white',
                        activebackground='white',cursor='hand2',bd=0,activeforeground='firebrick1',
                        command=signup_page)
newaccountButton.place(x=722,y=500)

login_window.mainloop()
