from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import simpledialog,messagebox
import mysql.connector as connector


class LoginPage:
    def __init__(self,login):
        self.login=login
        self.login.title("Login Page")
        self.login.geometry("400x200+550+200")
        self.login.configure(bg="snow")
        self.login.resizable(False, False)
        
        self.label = Label(self.login,text="Welcome",bg="navajowhite4",fg="white",font=("georgia",15,"bold"),width=29,height=2)
        self.label.place(x=0,y=10)

        signin=Button(self.login,text="Sign In",bg="azure3",fg="black",height=1,width=8,font=("Arial",14,"bold"),bd=2,relief=RIDGE,cursor="hand2",command=self.showSignin)
        signin.place(x=150,y=80)

        signup=Button(self.login,text="Sign Up",bg="azure3",fg="black",height=1,width=8,font=("Arial",14,"bold"),bd=2,relief=RIDGE,cursor="hand2",command=self.showSignup)
        signup.place(x=150,y=130)

    def showSignin(self):
        self.login.destroy()
        signin=Tk()
        obj1=SignIn(signin)
        signin.mainloop()
    def showSignup(self):
        self.login.destroy()
        signup=Tk()
        obj3=SignUp(signup)
        signup.mainloop()
        
class SignIn:
    def __init__(self,signin):
        self.signin=signin
        self.signin.title("Login Page")
        self.signin.geometry("400x200+550+200")
        self.signin.configure(bg="snow")
        self.signin.resizable(False, False)
        self.con1 = connector.connect(host='localhost', port='3306', user='root', database='do_list', password='Abhi@1720') 

        username=Label(self.signin,text="Username :",bg="snow",fg="black",font=("georgia",14,"bold"),height=1,width=10)
        username.place(x=55,y=30)

        password=Label(self.signin,text="Password :",bg="snow",fg="black",font=("georgia",14,"bold"),height=1,width=10)
        password.place(x=55,y=80)

        self.entry1=Entry(self.signin,width=12,font=("georgia",14),bd=2)
        self.entry1.place(x=200,y=32)

        self.entry2=Entry(self.signin,width=12,font=("georgia",14),bd=2)
        self.entry2.place(x=200,y=82)

        login_btn=Button(self.signin,text="LOGIN",font=("georgia",12),bd=2,height=1,width=8,bg="navajowhite4",fg="white",command=self.loginBtn)
        login_btn.place(x=150,y=120)

        signup_btn=Button(self.signin,text="Don't have an account?",font=("georgia",13),bd=2,height=1,width=17,bg="navajowhite4",fg="white",command=self.signup)
        signup_btn.place(x=98,y=160)
        
    def loginBtn(self):
        self.username_value = self.entry1.get()
        self.password_value = self.entry2.get()

        try:
            query = (f"SELECT * FROM user WHERE username = '{self.username_value}' AND password = '{self.password_value}';")
            cur = self.con1.cursor()
            cur.execute(query)
            user_data = cur.fetchone()
            if user_data:
                messagebox.showinfo("Success", "Login Successful")            
                self.signin.destroy()
                root = Tk()
                obj2 = ToDoList(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except Exception as e:
            print(f"Error: {e}")

    def signup(self):
        self.signin.destroy()
        signup=Tk()
        obj3=SignUp(signup)
        signup.mainloop()

class SignUp:
    def __init__(self,signup):
        self.signup=signup
        self.signup.title("Login Page")
        self.signup.geometry("400x200+550+200")
        self.signup.configure(bg="snow")
        self.signup.resizable(False, False)
        self.con1 = connector.connect(host='localhost', port='3306', user='root', database='do_list', password='Abhi@1720') 

        username=Label(self.signup,text="Username :",bg="snow",fg="black",font=("georgia",12,"bold"),height=1,width=12)
        username.place(x=45,y=20)

        password=Label(self.signup,text="Password :",bg="snow",fg="black",font=("georgia",12,"bold"),height=1,width=12)
        password.place(x=45,y=70)

        # cpassword=Label(self.signup,text="Confirm Password :",bg="snow",fg="black",font=("georgia",12,"bold"),height=1,width=15)
        # cpassword.place(x=30,y=120)

        self.entry1=Entry(self.signup,width=12,font=("georgia",13),bd=2)
        self.entry1.place(x=200,y=22)

        self.entry2=Entry(self.signup,width=12,font=("georgia",13),bd=2)
        self.entry2.place(x=200,y=72)

        # self.entry3=Entry(self.signup,width=12,font=("georgia",13),bd=2)
        # self.entry3.place(x=200,y=122)

        signup_btn=Button(self.signup,text="SIGNUP",font=("georgia",12),bd=2,height=1,width=8,bg="navajowhite4",fg="white",command=self.SignupBtn)
        signup_btn.place(x=150,y=147)

    def SignupBtn(self):
        self.username_value = self.entry1.get()
        self.password_value = self.entry2.get()
        # self.cpassword_value= self.entry3.get()

        try:
            query = (f"SELECT * FROM user WHERE user_id= '1' AND username = '{self.username_value}' AND password = '{self.password_value}';")
            cur = self.con1.cursor()
            cur.execute(query)
            existing_username = cur.fetchone()

            if existing_username:
                messagebox.showerror("Error", "Username and Password  already exists. Please choose a different username.")
            else:
                insert_query = (f"INSERT INTO user (username, password) VALUES ('{self.username_value}', '{self.password_value}');")
                cur2 = self.con1.cursor()
                cur2.execute(insert_query)
                self.con1.commit()
                messagebox.showinfo("Success", "Registration Successful")
                
                self.signup.destroy()
                root=Tk()
                obj4=ToDoList(root)
                root.mainloop()
        except Exception as e:
            print(f"Error: {e}")
            # messagebox.showerror("Error", f"An error occurred: {str(e)}")
            messagebox.showerror("Error", "Username and Password  already exists. Please choose a different username.")


class ToDoList:
    def __init__(self,root):
        self.root=root
        self.root.title("ToDoList")
        self.root.geometry("500x600+500+100")
        self.root.configure(bg="snow")
        self.root.resizable(False, False)
        self.con=connector.connect(host='localhost',port='3306',user='root',database='do_list',password='Abhi@1720') 
        
        self.frame=Frame(self.root,bg="cornsilk3",width=350,height=600)
        self.frame.place(x=150,y=0)

        # title_frame=Frame(frame,bg="navajowhite4",width=350,height=100)
        # title_frame.place(x=150,y=0)

        self.title_label = Label(self.root,text="~.THINGS TO DO.~",bg="navajowhite4",fg="white",font=("georgia",20,"bold"),width=28,height=3)
        self.title_label.place(x=0,y=0)

        self.entry=Entry(self.frame,width=23,font=("georgia",19),bd=2)
        self.entry.place(x=0,y=120)

        # btn1=Button(self.root,text="Add Task",bg="cornsilk3",fg="navajowhite4",height=2,width=11,font=("Arial",16,"bold"),bd=1,cursor="hand2")
        # btn1.place(x=10,y=250)

        btn1=Button(self.root,text="Add Task",bg="cornsilk3",fg="tomato4",height=1,width=8,font=("Arial",18,"bold"),bd=1,cursor="hand2",command=self.AddTask)
        btn1.place(x=10,y=240)

        btn2=Button(self.root,text="Delete",bg="cornsilk3",fg="tomato4",height=1,width=8,font=("Arial",18,"bold"),bd=1,cursor="hand2",command=self.DeleteTask)
        btn2.place(x=10,y=320)

        btn3=Button(self.root,text="Done",bg="cornsilk3",fg="tomato4",height=1,width=8,font=("Arial",18,"bold"),bd=1,cursor="hand2",command=self.Donetask)
        btn3.place(x=10,y=400)

        btn4=Button(self.root,text="Exit",bg="cornsilk3",fg="tomato4",height=1,width=8,font=("Arial",18,"bold"),bd=1,cursor="hand2",command=self.Exit)
        btn4.place(x=10,y=480)

        list_frame=Frame(self.frame,bg="white",width=350,height=460)
        list_frame.place(x=0,y=180)

        # scroll = Scrollbar(list_frame, orient=VERTICAL)
        # self.list_done = Listbox(list_frame, width=55, font=("Times new roman", 17), height=26,bg="navajowhite3", fg="black", selectbackground="steelblue4", cursor="hand2", yscrollcommand=scroll.set)
        # scroll.config(command=self.list_done.yview)  
        # scroll.pack(side=RIGHT, fill=Y)
        # self.list_done.pack(side=RIGHT,fill=BOTH)
        # self.style.configure('Custom.Treeview', background='navajowhite3')
        self.display_tree=ttk.Treeview(list_frame,column=('task'),height=20)
        self.display_tree.pack(fill=BOTH,expand=1)

        self.display_tree.config(show="headings")
        self.display_tree.heading('task',text='Task')

        self.display_tree.column('task', width=350)
        self.display_tree.tag_configure('bg_color', background='navajowhite3')  
        self.display_tree.tag_configure('fg_color', foreground='black') 
        self.display_tree['style'] = 'Custom.Treeview'

        query='SELECT task FROM do_list.task'
        cur=self.con.cursor()
        cur.execute(query)
        for data in cur:
            task = data[0]
            self.display_tree.insert('',END,value=(task,), tags=('bg_color', 'fg_color'))

        self.style = ttk.Style()
        self.style.configure('Custom.Treeview', font=("Times New Roman", 14))

    def AddTask(self):
        task = self.entry.get()
        if task:
            user_time = simpledialog.askstring("Time", "Enter time (HH:MM:SS):")

            try:
                # Check if the entered time is in the correct format
                datetime.strptime(user_time, '%H:%M:%S')

                # Combine the time with a placeholder date (e.g., today's date)
                task_with_time = f"{datetime.now().date()} {user_time} {task}"
                
                self.entry.delete(0, END)
                self.display_tree.insert('', END, values=(task_with_time,), tags=('bg_color', 'fg_color'))

                query =(f"INSERT INTO task (task) VALUES ('{task_with_time}');")

                cur=self.con.cursor()
                cur.execute(query)
                self.con.commit()
                messagebox.showinfo(title="Succeeded",message=(f"Information saved successfully"))

            except ValueError:
                messagebox.showerror("Error", "Invalid time format. Please use HH:MM:SS.")
    # def AddTask(self):
    #     task = self.entry.get()
    #     if task:
    #         task_text = task

    #         self.entry.delete(0, END)
    #         self.display_tree.insert('', END, values=(task_text,), tags=('bg_color', 'fg_color'))

    #         query = f"INSERT INTO task (task) VALUES ('{task_text}');"

    #         cur = self.con.cursor()
    #         cur.execute(query)
    #         self.con.commit()
    #         messagebox.showinfo(title="Succeeded", message="Information saved successfully")

    def DeleteTask(self):
        selected_task = self.display_tree.selection()
        if selected_task:
            selected_item = self.display_tree.item(selected_task)
            task = selected_item['values'][0]

            try:
                query = "DELETE FROM task WHERE task = %s"
                cur = self.con.cursor()
                cur.execute(query, (task,))
                self.con.commit()
                messagebox.showinfo(title="Success", message="Task deleted successfully")

                self.display_tree.delete(selected_task)

            except Exception as e:
                print(f"Error deleting task: {str(e)}")
                messagebox.showerror("Error", "An error occurred while deleting the task.")

        
    def Donetask(self):
        selected_task = self.display_tree.selection()
        if selected_task:
            selected_item = self.display_tree.item(selected_task)
            task = selected_item['values'][0]

            marked_task = "✔ " + task
            query = "UPDATE task SET task = %s WHERE task = %s"
            cur = self.con.cursor()
            cur.execute(query, (marked_task, task))
            self.con.commit()
            messagebox.showinfo(title="Succeeded",message=(f"Congratulations!! Completed Task"))

            self.display_tree.item(selected_task, values=(marked_task,))

    def Exit(self):
       exit()

login=Tk()
obj=LoginPage(login)
login.mainloop()