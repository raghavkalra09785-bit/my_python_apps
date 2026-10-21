# CALCULATOR APP 
import customtkinter as ctk

app = ctk.CTk()
app.state("zoomed")
app.title("Calculator")

ctk.set_appearance_mode("dark")

calculator_title = ctk.CTkLabel(
    app,
    text= "CALCULATOR",
    width= 300,
    height= 90,
    fg_color="#202738",
    text_color="#00CED1",
    corner_radius= 50,
    font= ("Helvetica",23)
)

calculator_title.place(relx= 0.5,y= 5,anchor= "n")

frame_1= ctk.CTkFrame(
    app,
    width= 400,
    height= 570,
    corner_radius= 25,
    fg_color= "#202738",
    border_width= 2,
    border_color= "#607D9B"
    
)


frame_1.place(relx= 0.5,rely= 0.55, anchor= "center")

text_1 = ctk.CTkEntry(
                      frame_1,
                      width= 340,
                      height= 85,
                      fg_color="#182233",
                      text_color="#FFFFFF",
                      border_color="#00CED1",
                      border_width= 2,
                      corner_radius= 15,
                      font= ("Arial",30,"bold")
                          )

text_1.place(relx= 0.52,y= 70,anchor= "center")

def press_1():
    text_1.insert("end",1)

button_1 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "1",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_1

)

button_1.place(relx= 0.15,y= 528, anchor= "center")

def press_2():
    text_1.insert("end", 2)

button_2 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "2",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_2

)

button_2.place(relx= 0.40,y= 528, anchor= "center")

def press_3():
    text_1.insert("end", 3)

button_3 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "3",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_3

)

button_3.place(relx= 0.65,y= 528, anchor= "center")

def press_4():
    text_1.insert("end", 4)

button_4 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "4",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_4

)

button_4.place(relx= 0.65,y= 440, anchor= "center")

def press_5():
    text_1.insert("end", 5)

button_5 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "5",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_5

)

button_5.place(relx= 0.40,y= 440, anchor= "center")

def press_6():
    text_1.insert("end", 6)

button_6 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "6",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_6

)

button_6.place(relx= 0.15,y= 440, anchor= "center")

def press_7():
    text_1.insert("end", 7)

button_7 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "7",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_7

)

button_7.place(relx= 0.65,y= 350, anchor= "center")

def press_8():
    text_1.insert("end", 8)

button_8 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "8",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_8

)

button_8.place(relx= 0.40,y= 350, anchor= "center")

def press_9():
    text_1.insert("end", 9)

button_9 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "9",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_9

)

button_9.place(relx= 0.15,y= 350, anchor= "center")

def press_0():
    text_1.insert("end", 0)

button_0 = ctk.CTkButton(
    frame_1,
    width= 90,
    height= 75,
    text= "0",
    fg_color="#263449",
    hover_color="#344B66",
    text_color="#FFFFFF",
    border_color="#607D9B",
    border_width= 2,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_0

)

button_0.place(relx= 0.15,y= 260, anchor= "center")

def press_equal():
    text_1.insert("end", "=")

def press_equal():
    expression_1 = text_1.get()

    try:
        result= eval(expression_1)
        text_1.delete(0, "end")
        text_1.insert("end", str(result))

    except:
        text_1.delete(0, "end")
        text_1.insert("end", "ERROR")
        

button_11 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "=",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_equal

)

button_11.place(relx= 0.65,y= 170, anchor= "center")

def press_plus():
    text_1.insert("end", "+")

button_12 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "+",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_plus

)

button_12.place(relx= 0.88,y= 170, anchor= "center")

def press_AC():
    text_1.delete(0, "end")

button_AC= ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "AC",
    fg_color="#A5A5A5",
    hover_color="#D4D4D2",
    text_color="#000000",
    border_color="#C7C7C7",
    border_width=1,
    corner_radius=20,
    font= ("Arial",20),
    command= press_AC

)

button_AC.place(relx= 0.40,y=170, anchor= "center" )

def press_minus():
    text_1.insert("end", "-")

button_13 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "-",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_minus
)

button_13.place(relx= 0.88,y= 260,anchor= "center")

def press_multiply():
    text_1.insert("end", "*")

button_14 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "*",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_multiply
)

button_14.place(relx= 0.88,y= 350,anchor= "center")

def press_divdide():
    text_1.insert("end","/")

button_15 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "÷",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_divdide
)

button_15.place(relx= 0.88,y= 528,anchor="center")

def press_modulas():
    text_1.insert("end", "%")

button_16 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "%",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",20,"bold"),
    command= press_modulas
)

button_16.place(relx= 0.88,y= 440,anchor= "center")

def press_decimal():
    text_1.insert("end", ".")

button_17 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= ".",
    fg_color="#FF9F0A",
    hover_color="#E68A00",
    text_color="#FFFFFF",
    border_color="#FFB340",
    border_width=1,
    corner_radius= 20,
    font= ("Arial",35,"bold"),
    command= press_decimal
)

button_17.place(relx= 0.65,y= 260, anchor= "center")

def press_back():
    text_1.delete(len(text_1.get()) -1, "end")

button_18 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "⌫",
    fg_color="#A5A5A5",
    hover_color="#D4D4D2",
    text_color="#000000",
    border_color="#C7C7C7",
    border_width=1,
    corner_radius=20,
    font=("Arial", 20),
    command= press_back
)

button_18.place(relx=0.40 ,y=260 ,anchor= "center")

button_19 = ctk.CTkButton(
    frame_1,
    width= 80,
    height= 75,
    text= "Exit",
    fg_color="#A5A5A5",
    hover_color="#D4D4D2",
    text_color="#000000",
    border_color="#C7C7C7",
    border_width=1,
    corner_radius=20,
    font=("Arial", 20),
    command= app.quit
)

button_19.place(relx=0.15 ,y=170 ,anchor= "center")

app.mainloop()