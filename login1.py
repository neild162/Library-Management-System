from tkinter import *     #we are importing tkinter module
import pymysql      # here we are connection database with python through pymysql module
from tkinter import messagebox 
from PIL import ImageTk,Image
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

root = Tk()                      
#making main window

root.configure(background='skyblue')      
#providing color to background image
root.title("Login or Register")
image2 =Image.open('C:\\Users\\neil1\\OneDrive\\Desktop\\Neil\\SEM4\\CollegePythonFiles\\python-project\\bg.jpg')
image2 = image2.resize((1500, 900))
image1 = ImageTk.PhotoImage(image2)
#w = image1.width()
#h = image1.height()
#root.geometry("%dx%d+0+0" % (w, h))
label1 = Label(root, image=image1)
label1.pack()
root.geometry('1500x900')         
#providing shape





mypass = "neil"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()





global E  #global is metohd which can change variable value anytime
global E1

global p
global p1


def create():
    top1 = Toplevel()   #this will make another window inside main window.  
    top1.geometry('500x300')
    top1.configure(background='skyblue')

    head = Label(top1,text = 'CREATE ACCOUNT',font = ('TIMES NEW ROMAN',30),bg='skyblue')
    head.place(x=50,y=10)
    l = Label(top1, text='Name',font = ('TIMES NEW ROMAN',25), bg = 'skyblue')
    l.place(x=10,y=70)
    E=Entry(top1,bd=10,width=20, textvariable=p, font = ('arial',20),bg='white')
    E.place(x=150,y=60)
    l1 = Label(top1, text='Password',font = ('TIMES NEW ROMAN',25), bg = 'skyblue')
    l1.place(x=10,y=140)
    E1=Entry(top1,bd=10,width=20, textvariable=p1, font = ('arial',20),bg='white')
    E1.place(x=150,y=130)
    
    submit = Button(top1,text='Create',width=15,height=3,bd=10,bg='red',command=create_as)
    submit.place(x=160,y=210)
    


p=StringVar()  #these are textvariable which is given in entry box
p1=StringVar()


def create_as():
    t = (str(p.get()))  # here we get these textvariable in a variable.
    t1 = (str(p1.get()))
    

    #if t!=0 or t1!=0:  #this condition tell that if any column is left empty it will give message
    #    messagebox.showerror("Error","All field are mandatory")  #here message is given
    #else:
    #db = sql.connect('localhost','root',mypass,mydatabase)  #here are connecting with database
    #cursor=db.cursor() #it will bound connection with database
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    y = "insert into member(Name,Password)values('%s','%s')"%(t,t1)  #inserting data in table
    cur.execute(y)  #it will execute the value and insert value into database 
    con.commit()
    con.close()
    messagebox.showinfo('success','successfully inserted') #if value is inserted ,it will give the message.


#NOW WE WORK FOR LOGIN SYSTEM

global r
global r1
global E
global E1
def login_into():
    top= Toplevel()
    top.configure(background='skyblue')
    top.geometry('500x300')

    l = Label(top, text='LOGIN HERE',font = ('TIMES NEW ROMAN',25),bg= 'skyblue')
    l.place(x=150,y=10)
    l = Label(top, text='Username',font = ('TIMES NEW ROMAN',25),bg='skyblue')
    l.place(x=10,y=70)
    E=Entry(top,bd=10,width=20, textvariable=r, font = ('arial',20),bg='white')
    E.place(x=150,y=60)
    l1 = Label(top, text='Password',font = ('TIMES NEW ROMAN',25),bg= 'skyblue')
    l1.place(x=10,y=140)
    E1=Entry(top,bd=10,width=20, textvariable=r1, font = ('arial',20),bg='white')
    E1.place(x=150,y=130)
    submit = Button(top,text='Login',width=30,bd=10,bg='red',height=3,command=login_as)
    #submit = Button(top,text='login',width=30,bd=10,bg='red',height=3,command=lambda:[login_as(),top.destroy(),root.destroy(),top1.destroy()])

    submit.place(x=160,y=210)
    #root.destroy()
#NOW WE WILL FETCH VALUE FROM DATABASE FOR LOGIN 


r=StringVar()
r1=StringVar()
def login_as():
    t= (str(r.get()))
    t1=(str(r1.get()))
    h=(t,t1)  #here we are taking value into tuple
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    y = ("select * from member where Name =%s and Password =%s ")  #here %s will get the data
    result=cur.execute(y,h)
    if result==True:  # checking condition if value is database is true then it will fetch it
        #top=Tk()
        #top.geometry('1500x900')
        #top.title('login details')
        #top.configure(background = 'skyblue')
        root2 = Tk()
        root2.title("Library")
        #root2.minsize(width=400,height=400)
        root2.geometry("1500x900")
        root2.configure(background='skyblue') 
        #image4 =Image.open('C:\\Users\\neil1\\OneDrive\\Desktop\\Neil\\SEM4\\CollegePythonFiles\\python-project\\library.jpg')
        #image4 = image4.resize((600, 500))
        #image3= ImageTk.PhotoImage(image4)

        #label2 = Label(root2, image=image3)
        #label2.pack()

# Take n greater than 0.25 and less than 5
        same=True
        n=0.25

       



        headingFrame1 = Frame(root2,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

        headingLabel = Label(headingFrame1, text="Welcome to our Virtual Library", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        btn1 = Button(root2,text="Add Book Details",bg='black', fg='white', command=addBook)
        btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
        btn2 = Button(root2,text="Delete Book",bg='black', fg='white', command=delete)
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
        btn3 = Button(root2,text="View Book List",bg='black', fg='white', command=View)
        btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
        btn4 = Button(root2,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
        btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
        btn5 = Button(root2,text="Return Book",bg='black', fg='white', command = returnBook)
        btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
        newWindow = Toplevel(root2)
        root2.deiconify()
        root2.mainloop()

        top1.destroy()
        top.destroy()
        #root.quit()
        root.quit()
        root.destroy()
        #newWindow = Toplevel(root2)
        #root2.deiconify()
    elif result==False:
        ans=messagebox.showerror('error','login fail')
        root.quit()  
        root2.quit()   

   
    
      




def main():
    #head = Label(root,text = 'Login or Register',font = ('TIMES NEW ROMAN',40))
    #head.place(x=600,y=200)
    login = Button(root,text='Login',width=35,height=5,bd=10,bg='red',font = ('TIMES NEW ROMAN',10),command=login_into)
    login.place(x=600,y=380)
    acc=Button(root,text='Create Account',width=35,height=5,bd=10,bg='red',font = ('TIMES NEW ROMAN',10),command=create)
    acc.place(x=600,y=480)

    root.mainloop()
main()        
















