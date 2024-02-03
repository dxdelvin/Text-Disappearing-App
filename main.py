from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Text Disappearing App")
root.geometry("500x500")

text_var = StringVar()

guide_label = Label(text="Write or it will be Disappeared",font=('calibre',15,'bold'))
guide_label.place(relx=0.5,rely=0.07,anchor="center")
text_entry = Text(root,width=60,height=23,font=('calibre',10,'normal'))
text_entry.place(relx=0.5,rely=0.5,anchor="center")
def dx():
    global value
    current_value = text_entry.get("1.0", "end-1c")
    print(value)
    if current_value == value:
        text_entry.delete("1.0", "end")
        text_entry.insert("end", "Text is Lost")
        root.after(2000, dx)
    else:
        value = current_value
        root.after(2000, dx)



value = "d"
dx()

root.mainloop()




