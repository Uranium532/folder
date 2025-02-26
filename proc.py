from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('700x480') #Setting window size
win.config(bg='black')

#open image button func
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title='Select File type',
                                         filetypes=(('PNG file','*.png'),('JPG file','*.jpg'),('All file','*.txt'))
                                         )  

    img = Image.open(open_file)   
    img = ImageTk.PhotoImage(img)  
    Lf1.configure(image=img) 
    Lf1.image=img              


#Hide data button Func(Encrypt)
def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
         msg = text1.get(1.0,END)
         hide_msg = lsb.hide(str(open_file),msg)
         messagebox.showinfo('Success','Message encrypted!.Please save your image')
    elif password == '':
        messagebox.showerror('Error','Please enter secret key!')
    else:
        messagebox.showerror('Invalid key','Key does not matched!')  
        code.set('')  


# save image button func
def save_img():
    hide_msg.save('Encrypteddata.png')
    messagebox.showinfo('Success','Imaged saved successfully')


# show data button func (Decrypt)
def show_data():
    password = code.get()
    if password == '1234':
        show_msg = lsb.reveal(open_file)
        text1.delete(1.0,END)
        text1.insert(END,show_msg)
    elif password == '':
        messagebox.showerror('Error','Please enter secret key!')
    else:
        messagebox.showerror('Invalid key','Key does not matched!')  
        code.set('')     



#  setting default image
logo = PhotoImage(file='logo1.png')
Label(win,image=logo,bd=0).place(x=500,y=30)

# Setting Title
Label(win,text='Stenographer',font='impack 40 bold', bg='black',fg='orange').place(x=620,y=30)

#frame1
f1 = Frame(win, width=700,height=400,bd=5,bg='purple')
f1.place(x=100, y=180)

#frame1 image 
Lf1 = Label(f1,bg='purple')
Lf1.place(x=0,y=0)

#frame2
f2 = Frame(win, width=600,height=300,bd=5,bg='coral')
f2.place(x=900, y=220)

#frame2 text field
text1 = Text(f2,font='ariel 15 bold',wrap=WORD,bg='coral')
text1.place(x=0,y=0,width=600,height=300)


#label for secret key
Label(win,text='Enter secret key',font='15',bg='black',fg='green').place(x=660,y=590)

#Secret key input field
code = StringVar()
Skey = Entry(win,textvariable=code,bd=2,font='impack 15 bold',show='*')
Skey.place(x=630,y=630)

#Buttons
open_b = Button(win,text='upload image',bg='yellow',fg='black',font='ariel 16 bold',cursor='hand2',command=open_img)
open_b.place(x=150,y=680)

save_b = Button(win,text='save image',bg='green',fg='white',font='ariel 16 bold',cursor='hand2',command=save_img)
save_b.place(x=450,y=680)

Hide_b = Button(win,text='Encrypt',bg='red',fg='white',font='ariel 16 bold',cursor='hand2',command=hide)
Hide_b.place(x=890,y=680)

show_b = Button(win,text='Decrypt',bg='blue',fg='white',font='ariel 16 bold',cursor='hand2',command=show_data)
show_b.place(x=1150,y=680)



mainloop()
