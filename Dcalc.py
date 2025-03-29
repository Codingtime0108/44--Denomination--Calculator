from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denominator Calculator")
root.geometry("400x650")
root.configure(bg = "light blue")

upload = Image.open("app_img.jpg")

upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)

lbl = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg="light blue")
lbl.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == "ok":
        topwin()

button1 = Button(root,
                 text="Let's get started",
                 command=msg,
                 bg= "brown",
                 fg= "black")
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title( "Denominations Calculator")
    top.configure(bg='light pink')
    top.geometry("600x350+50+50" )


    label = Label(top, text="Enter total amount, Please round your number to 2 Significant figures", bg='light grey')
    entry = Entry(top)
    Lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey.')

    l1 = Label(top, text="50000", bg='light grey')
    l2 = Label (top, text="10000", bg='light grey')
    l3 = Label(top, text="5000", bg='light grey')
    l4 = Label(top, text="1000", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note50000 = amount // 50000
            amount %= 50000
            note10000 = amount // 10000
            amount %= 50000
            note5000 = amount // 5000
            amount %= 50000
            note1000 = amount // 1000
            amount %= 1000

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t4.delete(0,END)

            t1.insert(END, str(note50000))
            t2.insert(END, str(note10000))
            t3.insert(END, str(note5000))
            t4.insert(END, str(note1000))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    btn = Button(top, text= "Calculate", command=calculator, bg = "brown", fg = "white")

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)
    
    l1.place(x= 180, y= 200)
    l2.place(x= 180, y= 230)
    l3.place(x= 180, y= 260)
    l4.place(x= 180, y= 290)
    
    t1.place(x= 270, y= 200)
    t2.place(x= 270, y= 230)
    t3.place(x= 270, y= 260)
    t4.place(x= 270, y= 290)

    top.mainloop()
root.mainloop()
    
