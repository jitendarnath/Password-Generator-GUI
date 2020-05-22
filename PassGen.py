import string
from random import randint,choice
from tkinter import *
import tkinter.messagebox as tmsg

#function for generating password
def pass_gen():
    all_chars = string.ascii_letters +string.punctuation +string.digits 
    password = "".join(choice(all_chars) for x in range(myslider.get()))        
    password_entry.delete(0,END)
    password_entry.insert(0,password)

def save_pass():
    msg=tmsg.askquestion("Save As","Do you want to save?")
    with open("D:\\Programming\\Python\\Project\\records.txt","a") as f:
        f.write(f"\n{account_name.get(), username.get(), password_entry.get()}")
        f.close()
    print("Saved Changes ..!!")

def records():
    top= Toplevel()
    top.title('Records')
    top.geometry("850x500")
    top.iconbitmap("Images/logo.ico")
    top.config(background='#002447')
    
#Defining the Window
window = Tk()
window.title("Pass-Gen")
window.geometry("850x550")
window.iconbitmap("Images/logo.ico")
window.config(background='#002447')

#main Frame
frame = Frame(window,bg='#002447')

#Image
width = 340
height = 488
img = PhotoImage(file="Images/password.png").zoom(20).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#002447', bd=0, highlightthickness=0)
canvas.create_image(width/2,height/2,image=img)
canvas.grid(row=0,column=0,sticky=W)

right_frame = Frame(frame, bg='#002447')

#Application Label
label_title = Label(right_frame,text="Password Generator",font=("lucida",25,"bold","underline"),bg='#002447',fg='Yellow',pady=10)
label_title.pack()

pass_len = Label(right_frame,text="Choose your password Length:",font=("lucida",15),bg='#002447',fg='light blue',pady=3)
pass_len.pack()

myslider=Scale(right_frame, from_=5, to=20,orient=HORIZONTAL,tickinterval=5,bg='#002447',fg='light blue',highlightthickness=0)
myslider.pack(fill=X)

#appearing password text box
right_sub_frame1= Frame(right_frame, bg='#002447')

password_entry = Entry(right_sub_frame1,font=("Courier New",19),bg='#002447',fg='PeachPuff')
password_entry.grid(row=0,column=0,ipady=3)
password_entry.insert(0," Click Generate -->")

generate_password_button = Button(right_sub_frame1,text="Generate",font=("Helvetica",14),bg='white',fg='#002447',command=pass_gen,relief=RAISED)
generate_password_button.grid(row=0,column=1)


right_sub_frame1.pack(pady=15)

right_sub_frame2= LabelFrame(right_frame,text=" Store Password : ",font=("Helvetica",14), bg='#002447',fg='light blue',padx=15,pady=10)

account_name = Entry(right_sub_frame2,font=("Helvetica",15),bg='#002447',fg='PeachPuff')
account_name.grid(row=0,columnspan=2,sticky="we",pady=5,ipadx=22,ipady=3)
account_name.insert(0," Enter account name")

username = Entry(right_sub_frame2,font=("Helvetica",15),bg='#002447',fg='PeachPuff')
username.grid(row=1,column=0,pady=5,ipadx=22,ipady=3)
username.insert(0," Enter username")

save_pw_button = Button(right_sub_frame2,text="Save",font=("Helvetica",12),bg='white',fg='#002447',command=save_pass,relief=RAISED)
save_pw_button.grid(row=1,column=1,ipadx=15,ipady=0)

right_sub_frame2.pack(fill=X)

right_frame.grid(row=0, column=1,sticky=W)

footer_title = Label(text="2020 | Jitendar Nath | VIT", font="Sanseriff 10",bg='#002447',fg='grey',borderwidth=1,relief=RIDGE,pady=5)
footer_title.pack(side=BOTTOM,fill=X)

frame.pack(expand=YES)

#Menu Bar
main_menu = Menu(window)

m1 = Menu(main_menu,tearoff=0)
m1.add_command(label="New",command=pass_gen)
m1.add_command(label="Save", command=save_pass)
m1.add_separator()
m1.add_command(label="Save As", command=save_pass)
m1.add_command(label="Quit", command=window.quit)
main_menu.add_cascade(label="Menu",menu=m1)
window.config(menu=main_menu)

m2 = Menu(main_menu,tearoff=0)
m2.add_command(label="Log", command=records)
m2.add_command(label="Help", command=window.quit)

main_menu.add_cascade(label="Options",menu=m2)

window.config(menu=main_menu)
    
window.mainloop()