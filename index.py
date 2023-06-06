from tkinter import *
import os
from PIL import ImageTk, Image
from datetime import datetime
import random
import string

#Home page
Home = Tk()
Home.title('Banking app')
Home.geometry("650x720")
Home.configure(bg='#a1b3c6')
#Home.configure(background= "white")


def helo():
    print("helooooo")

# Open and resize the button image
button_image = Image.open("C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\blue-glossy-button1.jpg")
button_image = button_image.resize((220, 90))

# Convert the image to Tkinter-compatible format
button_photo = ImageTk.PhotoImage(button_image)



#Functions
def registration_logic():
    global spacer
    global timestamp
    name = temp_name.get()
    age = temp_age.get()
    gender = temp_gender.get()
    password = temp_password.get()
    password2 = temp_password2.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    spacer = "**************************************************"
    account_id = []

    while len(account_id) != 22:
        char = random.choice(string.ascii_letters + string.digits)
        account_id.append(char)

    accountNUM = (''.join(account_id))


    if name == "" or age == "" or gender == "" or password == "":
        notify.config(fg="red", text="All Feild Are Required.*")
        print("all fleilds are required")
        return
    
    if password != password2:
        notify.config(fg="red", text="Passwords do not match!")
        print("passwords dont match")
        return

    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + accountNUM + ".txt"
    if os.path.exists(file_path):
        notify.config(fg="red", text="Account Already Exists.*")
        print("Account already exists")
        return
    else:

        new_file = open(file_path,"w")
        new_file.write(name+'\n')
        new_file.write(accountNUM+'\n')
        new_file.write(password+'\n')
        new_file.write(age+'\n')
        new_file.write(gender+'\n')
        new_file.write("0"+'\n')
        new_file.close()
        notify.config(fg="green", text="Account Created Successfully."+ "\n" +"Your Account Number is: "+accountNUM+"\n"+"Your password is: "+password) 


    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + accountNUM + "_transaction_data.txt"
    if os.path.exists(file_path):
        notify.config(fg="red", text="Transaction Data Already Exists.*")
        print("Transaction Data already exists")
        return
    else:
        
        new_file = open(file_path,"a")
        new_file.write("Account Open: " + str(timestamp) + "\n")
        new_file.close()
        print("Transaction Data Already Exists.*")         


def register():

    
    #variables
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global temp_balance 
    global notify
    global temp_password2
    temp_name = StringVar()
    temp_age = StringVar()
    temp_gender = StringVar()
    temp_password = StringVar()
    temp_balance = StringVar()
    temp_password2 = StringVar()

    #register screen
    Register_screen = Toplevel(Home)
    Register_screen.title('Register')
    Register_screen.geometry("650x650")
    Register_screen.configure(bg='#a1b3c6')
    

    #Labels
    Label(Register_screen, text = "Please Fill In Your Information", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 150, pady = 10)
    Label(Register_screen, text = "Name and surname", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 1, sticky = W)
    Label(Register_screen, text = "Age", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 2, sticky = W)
    Label(Register_screen, text = "Gender", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 3, sticky = W)
    Label(Register_screen, text = "Password", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 4, sticky = W)
    Label(Register_screen, text = "Password check", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 5, sticky = W)
    notify = Label(Register_screen, text = "", font = ('calibri', 14), bg = "#a1b3c6")
    notify.grid(row = 6, sticky = N, pady=10 )


    #Entry
    Entry(Register_screen,textvariable=temp_name ).grid(row=1, column=0)
    Entry(Register_screen,textvariable=temp_age ).grid(row=2, column=0)
    Entry(Register_screen,textvariable=temp_gender ).grid(row=3, column=0)
    Entry(Register_screen,textvariable=temp_password, show="*" ).grid(row=4, column=0)
    Entry(Register_screen,textvariable=temp_password2, show="*" ).grid(row=5, column=0)
    Button(Register_screen, text = "Register", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60,font = ('calibri', 14), command = registration_logic).grid(row=7, pady = 10, sticky=N)

    print("register")
    Button(Register_screen, text="Close", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=Register_screen.destroy).grid(row=8, pady=10, sticky=N)

def login_logic():
    timestamp1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global login_accountNUM
    login_accountNUM = temp_login_accountNUM.get()
    login_password = temp_login_password.get()
    account_exists = False

    
    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + ".txt"
    if os.path.exists(file_path):
        account_exists = True
        with open(file_path, "r") as account_file:
            lines = account_file.readlines()
            stored_password = lines[2].strip()
            if login_password == stored_password:
                options_page()
                
                file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + "_transaction_data.txt"
                if os.path.exists(file_path):
                    print("Transaction Data file found")
                    new_file = open(file_path,"a")
                    new_file.write("****************************NEW LOG***************************************"+"\n")
                    new_file.write("Login Time: "+str(timestamp1) +"\n")
                    new_file.write('\n')
                    new_file.close()
                    print("Login Data recorded")
                    return

                print("Login Success")
                # Perform actions after successful login
                # You can add code here to open a new window or perform any other desired actions.
                
                return
            else:
                print("Incorrect password")
                # Update the login_notify label with an appropriate error message
                login_notify.config(fg="red", text="Incorrect password.")
                return
        

    if not account_exists:
        print("Account does not exist")
        # Update the login_notify label with an appropriate error message
        login_notify.config(fg="red", text="Account does not exist.")
    
    account_file.close()

def login():
    global login_notify
    global Login_screen
    global temp_login_accountNUM
    global temp_login_password
    temp_login_accountNUM = StringVar()
    temp_login_password = StringVar()

    Login_screen = Toplevel(Home)
    Login_screen.title('Login')
    Login_screen.geometry("650x650")
    Login_screen.configure(bg='#a1b3c6')
    

    #Labels
    Label(Login_screen, text = "Please Fill In Your Information", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 150, pady = 10)
    Label(Login_screen, text = "Account Number", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 1, sticky = W)
    Label(Login_screen, text = "Password", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 2, sticky = W)
    login_notify = Label(Login_screen, text = "", font = ('calibri', 14), bg = "#a1b3c6")
    login_notify.grid(row = 6, sticky = N, pady=10 )


    #Entry
    Entry(Login_screen,textvariable=temp_login_accountNUM  ).grid(row=1, column=0)
    Entry(Login_screen,textvariable=temp_login_password, show="*" ).grid(row=2, column=0)
    
    #Button
    Button(Login_screen, text = "Login", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60,font = ('calibri', 14), command = login_logic).grid(row=7, pady = 10, sticky=N)  
    Button(Login_screen, text="Close", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60,font=('calibri', 14), command=Login_screen.destroy).grid(row=8, pady=10, sticky=N)
def options_page():


    options_screen = Toplevel(Home)
    options_screen.title('options')
    options_screen.geometry("650x800")
    options_screen.configure(bg='#a1b3c6')
    

    Label(options_screen, text = "Welcome to CITI Bank", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 150, pady = 10)
    Label(options_screen, text = "Unlocking Your Financial Potential.", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 1, column = 0, sticky = N, padx = 150, pady = 10)
    Label(options_screen, image = img).grid(row = 2, sticky = N, pady = 10)

    Button(options_screen, text = "View Account Details ",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font = ('calibri', 14), command=View_account).grid(row=3, pady = 10,sticky=N)
    Button(options_screen, text = "Deposit",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font = ('calibri', 14), command=deposit).grid(row=4, pady = 10, sticky=N)
    Button(options_screen, text="Withdraw",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14),  command=withdraw).grid(row=5, pady=10, sticky=N)
    Button(options_screen, text="Display Transaction Data",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=display_transaction_data).grid(row=6, pady=10, sticky=N)
    Button(options_screen, text="Close",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=options_screen.destroy).grid(row=7, pady=10, sticky=N)


    
def View_account():

    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + ".txt"
    with open(file_path, "r") as account_file:
        lines = account_file.readlines()
        stored_name = lines[0].strip()
        stored_accountnum = lines[1].strip()
        
        stored_age =  lines[3].strip()
        stored_gender = lines[4].strip()
        stored_balance = lines[5].strip()
        account_file.close()

    view_screen = Toplevel(Home)
    view_screen.title('options')
    view_screen.geometry("650x650")
    view_screen.configure(bg='#a1b3c6')
    

    Label(view_screen, text = "CITI Bank", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 250, pady = 10)

    Label(view_screen, text = "Name: "+stored_name, font = ('calibri', 14), bg = "#a1b3c6").grid(row = 1, column = 0, sticky = W, padx = 0, pady = 10)

    Label(view_screen, text = "Account Number: "+stored_accountnum, font = ('calibri', 14), bg = "#a1b3c6").grid(row = 2, column = 0, sticky = W, padx = 0, pady = 10)
    
   


    Label(view_screen, text = "Age: "+stored_age, font = ('calibri', 14), bg = "#a1b3c6").grid(row = 3, column = 0, sticky = W, padx = 0, pady = 10)
    
    Label(view_screen, text = "Gender: "+stored_gender, font = ('calibri', 14), bg = "#a1b3c6").grid(row = 4, column = 0, sticky = W, padx = 0, pady = 10)
    
    Label(view_screen, text = "Balance: R"+stored_balance, font = ('calibri', 14), bg = "#a1b3c6").grid(row = 5, column = 0, sticky = W, padx = 0, pady = 10)
    
    Button(view_screen, text="Close", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=view_screen.destroy).grid(row=6, pady=10, sticky=N)    
    

def deposit_logic():
    global login_accountNUM
    amount = temp_amount.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if amount == "":
        deposit_notify.config(fg="red", text="Please enter an amount.")
        return
    
    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + ".txt"
    if os.path.exists(file_path):
        with open(file_path, "r+") as account_file:
            lines = account_file.readlines()
            stored_balance = float(lines[5].strip())
            new_balance = stored_balance + float(amount)
            lines[5] = str(new_balance) + '\n'
            account_file.seek(0)
            account_file.writelines(lines)
            account_file.truncate()
            account_file.close()

            file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + "_transaction_data.txt"
            new_file = open(file_path,"a")
            new_file.write("Deposit Amount: "+ str(amount)+"\n")
            new_file.write("Transaction Time: "+str(timestamp) +"\n")
            new_file.write("Balance: "+str(new_balance))
            new_file.write('\n')
            new_file.close()
        
        deposit_notify.config(fg="green", text="Deposit successful. New balance: R%.2f" % new_balance)
    else:
        deposit_notify.config(fg="red", text="Account does not exist.")

def deposit():
    global temp_amount
    global deposit_notify
    temp_amount = StringVar()

    deposit_screen = Toplevel(Home)
    deposit_screen.title('Deposit')
    deposit_screen.geometry("650x650")
    deposit_screen.configure(bg='#a1b3c6')
    


    # Labels
    Label(deposit_screen, text = "DEPOSIT", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 250, pady = 10)
    Label(deposit_screen, text="Enter Amount to Deposit:", font=('calibri', 14), bg = "#a1b3c6").grid(row=1, sticky=N)
    deposit_notify = Label(deposit_screen, text="", font=('calibri', 14), bg = "#a1b3c6")
    deposit_notify.grid(row=3, sticky=N, pady=10)

    # Entry
    Entry(deposit_screen, textvariable=temp_amount).grid(row=2, column=0, sticky=N)

    # Button
    Button(deposit_screen, text="Deposit",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=deposit_logic).grid(row=4, pady=10, sticky=N)
    Button(deposit_screen, text="Close",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=deposit_screen.destroy).grid(row=5, pady=10, sticky=N)

def withdraw_logic():
    global login_accountNUM
    amount = temp_amount1.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if amount == "":
        withdraw_notify.config(fg="red", text="Please enter an amount.")
        return

    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + ".txt"
    if os.path.exists(file_path):
        with open(file_path, "r+") as account_file:
            lines = account_file.readlines()
            stored_balance = float(lines[5].strip())

            if float(amount) > stored_balance:
                withdraw_notify.config(fg="red", text="Insufficient balance.")
                return

            new_balance = stored_balance - float(amount)
            lines[5] = str(new_balance) + '\n'
            account_file.seek(0)
            account_file.writelines(lines)
            account_file.truncate()
            account_file.close()

            file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + "_transaction_data.txt"
            new_file = open(file_path,"a")
            new_file.write("Withdraw Amount: "+ str(amount)+"\n")
            new_file.write("Transaction Time: "+str(timestamp) +"\n")
            new_file.write("Balance: "+str(new_balance))
            new_file.write('\n')
            new_file.close()

        withdraw_notify.config(fg="green", text="Withdrawal successful. New balance: R%.2f" % new_balance)
    else:
        withdraw_notify.config(fg="red", text="Account does not exist.")


def withdraw():
    global temp_amount1
    global withdraw_notify
    temp_amount1 = StringVar()

    withdraw_screen = Toplevel(Home)
    withdraw_screen.title('Withdraw')
    withdraw_screen.geometry("650x650")
    withdraw_screen.configure(bg='#a1b3c6')
    

    # Labels
    Label(withdraw_screen, text = "Withdraw", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 250, pady = 10)
    Label(withdraw_screen, text="Enter Amount to Withdraw:", font=('calibri', 14), bg = "#a1b3c6").grid(row=1, sticky=N)
    withdraw_notify = Label(withdraw_screen, text="", font=('calibri', 14), bg = "#a1b3c6")
    withdraw_notify.grid(row=3, sticky=N, pady=10)

    # Entry
    Entry(withdraw_screen, textvariable=temp_amount1).grid(row=2, column=0)

    # Button
    Button(withdraw_screen, text="Withdraw",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=withdraw_logic).grid(row=4, pady=10, sticky=N)
    Button(withdraw_screen, text="Close",compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=withdraw_screen.destroy).grid(row=5, pady=10, sticky=N)

def display_transaction_data():
    file_path = "C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\user info\\" + login_accountNUM + "_transaction_data.txt"
    with open(file_path, "r") as account_file:
        transaction_data = account_file.read()

    # Create a new window to display the transaction data
    display_transaction_data_screen = Toplevel()
    display_transaction_data_screen.title("Transaction Data")
    display_transaction_data_screen.configure(background= "white")

    # Create a Text widget and set its content to the transaction data
    text_widget = Text(display_transaction_data_screen , width=350, height=350)
    text_widget.insert(END, transaction_data)
    text_widget.configure(state="disabled")
    text_widget.pack()



    print("transaction_statement")


#Home image
img = Image.open('C:\\Users\\Kiran Isaacs\\Desktop\\banking app1\\bank.jpg')
img = img.resize((350,350))
img = ImageTk.PhotoImage(img)


fg = "light green",
bg = "dark green",
# Home page heading and picture
Label(Home, text = "Welcome to CITI Bank", font = ('calibri', 20), bg = "#a1b3c6").grid(row = 0, column = 0, sticky = N, padx = 150, pady = 10)
Label(Home, text = "Unlocking Your Financial Potential.", font = ('calibri', 14), bg = "#a1b3c6").grid(row = 1, column = 0, sticky = N, padx = 150, pady = 10)
Label(Home, image = img, bg = "#a1b3c6").grid(row = 2, sticky = N, pady = 10)

Button(Home,text = "Create Account", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font = ('calibri', 14), command = register).grid(row=3, pady = 10,sticky=N)
Button(Home,text = "Login", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60,  font = ('calibri', 14), command = login).grid(row=4, pady = 10, sticky=N)
Button(Home,text="Close", compound=CENTER, image=button_photo, borderwidth=0,  bg = "#a1b3c6", highlightthickness=0,highlightbackground = "#a1b3c6", height=60, font=('calibri', 14), command=Home.destroy).grid(row=5, pady=10, sticky=N)
#Button(Home, text="Deposit", font=('calibri', 14), width=20, command=deposit).grid(row=5, pady=10, sticky=N)




Home.mainloop()



#click_btn= PhotoImage(file='clickme.png')