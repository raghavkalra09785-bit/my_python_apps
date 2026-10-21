# Calculator app
import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("CLICK COUNTER")
root.state("zoomed")
root.configure(bg="#141824")

count = 0

def increase():
    global count
    count +=1
    text.config(text=count)

def decrease():
    global count
    count -=1
    text.config(text=count)
    
def reset():
    global count
    count = 0
    text.config(text=count)

def custom_increment():
    global count
    by_user = int(custom_entry.get())
    count +=by_user
    text.config(text=count)


button_1 = tk.Button(
            root,
            text= "+1",
            width= 10,
            height= 1,
            bg= "#16A34A",
            fg= "#FFFFFF",
            font= ("Arial",12),
            command= increase
            )

button_1.place(relx=0.5, y=250, anchor="center")

button_2 = tk.Button(
    root,
    text= "-1",
    width= 10,
    height= 1,
    bg= "#DC2626",
    fg= "#FFFFFF",
    font= ("Arial",12),
    command= decrease
)

button_2.place(relx=0.5, y=300, anchor="center")

button_3 = tk.Button(
    root,
    text= "Reset",
    width= 20,
    height= 2,
    bg= "#242938",
    fg= "#FFFFFF",
    bd= 0,
    highlightbackground= "#8B7CFF",
    highlightthickness= 2,
    font= ("helvetica',12"),
    command= reset

)

button_3.place(relx=0.5, y=350, anchor="center")

text= tk.Label(
    root,
    text= count,
    width= 22,
    height= 2,
    bg= "#242938",
    fg= "#F1F5F9",
    font= ("Arial",17)

)

text.place(
    relx=0.5,
    y=150,
    anchor="n"
)

text_2 = tk.Label(
    root,
    text= "Welcome to the click counter app",
    bg= "#141824",
    fg="#F1F5F9",
    activebackground= "#141824",
    relief= "flat",
    bd= 0,
    font= ("Segoe UI",30)
)

text_2.place(
    relx=0.5,
    y=10,
    anchor="n"
)

text_3 = tk.Label(
    root,
    text= "Click Counter App",
    bg="#141824",
    fg="#F1F5F9",
    activebackground= "#141824",
    relief= "flat",
    bd= 0,
    font=("helvetica",18)

)

text_3.place(
    relx=0.5,
    y=75,
    anchor="n"
)

image = Image.open(r"c:\Users\Raghav kalra\Downloads\i-removebg-preview.png")
image = image.resize((300,300))
image = image.rotate(-40,expand= True)

photo = ImageTk.PhotoImage(image)

add_image = tk.Label(
    root,
    image= photo,
    bg= "#141824",
    bd= 0
)

add_image.place(relx= 0.6,y= 550,anchor= "sw")

custom_entry = tk.Entry(
        root,
        bg="#242938",
        fg="#F1F5F9",
        insertbackground= "#FFFFFF",
        width= 20,
        font= ("Helvetica",17),
        justify= "center"
)

custom_entry.place(relx=0.5, y=420, anchor="center")

button_4 = tk.Button(
    root,
    text= "Enter the custom count ",
    bg="#242938",
    fg="#FFFFFF",
    width= 20,
    height= 2,
    font=("Helvetica",10),
    command= custom_increment
)

button_4.place(relx=0.5, y=475, anchor="center")


root.mainloop()


