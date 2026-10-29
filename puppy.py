# Puppy game 

import customtkinter as ctk
from PIL import Image
import tkinter.messagebox as messagebox

app = ctk.CTk()
app.geometry("1200x800")
app.title("PET DOG SIMULATOR")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app.config(bg= "#111827")

welcome_page = ctk.CTkFrame(
    app,
    width=950,
    height=800,
    fg_color= "#111827"
)

def open_welcome():
    game_page.forget()
    welcome_page.place(x=0, y=0, relwidth=1, relheight=1)
    welcome_page.tkraise()
    welcome_page.lift()

def open_game():
    welcome_page.forget()
    game_page.place(x= 0,y= 0, relwidth=1, relheight= 2)
    game_page.tkraise()

game_page = ctk.CTkFrame(
    app,
    fg_color="#111827"
)

open_welcome()

play_button = ctk.CTkButton(
    welcome_page,
    text= "PLAY GAME",
    fg_color="#00CED1",
    hover_color="#00A6A6",
    text_color="#111827",
    border_color="#FFFFFF",
    border_width= 2,
    font= ("Segoe UI", 50, "bold"),
    command= open_game
    )

play_button.place(relx= 0.5,y= 350,anchor= "center")

ass_1 = Image.open(r"c:\Users\Raghav kalra\Downloads\ass.1-removebg-preview.png")

aset_1 = ctk.CTkImage(
    light_image= ass_1,
    dark_image= ass_1,
    size= (150,150)
)

ass_1_label = ctk.CTkLabel(
    game_page,
    text= "",
    image= aset_1,
    fg_color= "#111827"
)
ass_1_label.place(relx= 0.76,y=-40,anchor= "n")



bitcoin_open = Image.open(r"c:\Users\Raghav kalra\Downloads\Glossy ₹250 Coin Counter.png")

bitcoin_open_label = ctk.CTkImage(
    light_image= bitcoin_open,
    dark_image= bitcoin_open,
    size= (150,60)
)

money_box= ctk.CTkLabel(
    game_page,
    text= "",
    image= bitcoin_open_label,
    fg_color= "#111827"
)

money_box.place(relx= 0.5,y= 140,anchor= "center")

head = ctk.CTkLabel(
    game_page,
    text= "PET DOG SIMULATOR",
    width= 200,
    height= 50,
    fg_color= "#111827",
    font=("Segoe UI", 50, "bold")
)

head.place(relx= 0.5,y= 5, anchor= "n")

subhead = ctk.CTkLabel(
    game_page,
    text= "NOW YOUR PERSONAL DOG TO PLAY \n LET'S PLAY TOGETHER",
    width= 200,
    height= 50,
    fg_color= "#111827",
    font= ("Segoe UI", 15, "italic")
)

subhead.place(relx= 0.5,y= 75,anchor= "n")

puppy_normal_label = ctk.CTkImage(
    Image.open(r"c:\Users\Raghav kalra\Downloads\Joyful Golden Retriever Puppy.png"),
    size= (400,400)
)

show_puppy_eat = ctk.CTkImage(
    Image.open(r"c:\Users\Raghav kalra\Downloads\Golden Retriever Puppy Enjoying Dinner.png"),
    size= (400,400)
)

show_puppy_sleep = ctk.CTkImage(
    Image.open(r"c:\Users\Raghav kalra\Downloads\Sleeping_Golden_Retriever_Puppy_with_Zs-removebg-preview.png"),
    size= (400,400)
)

show_puppy_bark = ctk.CTkImage(
    Image.open(r"c:\Users\Raghav kalra\Downloads\bark.png"),
    size= (400,400)
)

show_puppy_playing = ctk.CTkImage(
    Image.open(r"c:\Users\Raghav kalra\Downloads\playing.png"),
    size= (400,400)
)


dog_label = ctk.CTkLabel(game_page,text= "",image= puppy_normal_label )
dog_label.place(relx= 0.5,y= 350,anchor= "center")

def change_to_eat():
    dog_label.configure(image= show_puppy_eat )


dog_eat = ctk.CTkButton(
    game_page,
    text= "EAT",
    width= 150,
    height= 30,
    corner_radius= 25,
    fg_color="#00D4FF",
    hover_color="#00A8CC",
    text_color="#111827",
    border_color="#00D4FF",
    border_width=1,
    font= ("Segoe UI", 25, "underline"),
    command= change_to_eat,
)

dog_eat.place(relx= 0.5, y= 600,anchor= "center")

def change_to_play():
    dog_label.configure(image= show_puppy_playing)

dog_play = ctk.CTkButton(
    game_page,
    text= "PLAY",
    width= 150,
    height= 30,
    corner_radius= 25,
    fg_color="#00D4FF",
    hover_color="#00A8CC",
    text_color="#111827",
    border_color="#00D4FF",
    border_width=1,
    font= ("Segoe UI", 25, "underline"),
    command= change_to_play
)

dog_play.place(relx= 0.65, y= 600,anchor= "center")

def change_to_sit():
    dog_label.configure(image=puppy_normal_label )

dog_sit = ctk.CTkButton(
    game_page,
    text= "SIT",
    width= 150,
    height= 30,
    corner_radius= 25,
    fg_color="#00D4FF",
    hover_color="#00A8CC",
    text_color="#111827",
    border_color="#00D4FF",
    border_width=1,
    font= ("Segoe UI", 25, "underline"),
    command= change_to_sit
)

dog_sit.place(relx= 0.80, y= 600,anchor= "center")

def change_to_sleep():
    dog_label.configure(image= show_puppy_sleep)

dog_sleep = ctk.CTkButton(
    game_page,
    text= "SLEEP",
    width= 150,
    height= 30,
    corner_radius= 25,
    fg_color="#00D4FF",
    hover_color="#00A8CC",
    text_color="#111827",
    border_color="#00D4FF",
    border_width=1,
    font= ("Segoe UI", 25, "underline"),
    command= change_to_sleep
)

dog_sleep.place(relx= 0.35, y= 600,anchor= "center")

def change_to_bark():
    dog_label.configure(image= show_puppy_bark)

dog_bark = ctk.CTkButton(
    game_page,
    text= "BARK",
    width= 150,
    height= 30,
    corner_radius= 25,
    fg_color="#00D4FF",
    hover_color="#00A8CC",
    text_color="#111827",
    border_color="#00D4FF",
    border_width=1,
    font= ("Segoe UI", 25, "underline"),
    command= change_to_bark
)

dog_bark.place(relx= 0.20, y= 600,anchor= "center")

heading_animated = Image.open(r"c:\Users\Raghav kalra\Downloads\heading (2).png")

heading_animated_label = ctk.CTkImage(
    light_image= heading_animated,
    dark_image= heading_animated,
    size= (500,300)
)

heading_animated_display = ctk.CTkLabel(
    welcome_page,
    text= "",
    image= heading_animated_label,
    fg_color= "#111827"
)

heading_animated_display.place(relx= 0.5,y= 0,anchor= "n")

exit_button = ctk.CTkButton(
    welcome_page,
    text= "EXIT",
    width= 200,
    height= 50,
    fg_color="#EF4444",
    hover_color="#B91C1C",
    text_color="#FFFFFF",
    border_color="#FCA5A5",
    border_width=2,
    font= ("Segoe UI",35,"underline"),
    command=lambda: (
    app.destroy()
    if messagebox.askyesno("Exit Game", "Are you sure?")
    else None
)
)

exit_button.place(relx= 0.5,y= 450,anchor= "center")

inside_exit_button = ctk.CTkButton(
    game_page,
    text= "EXIT GAME",
    width= 200,
    height= 50,
    fg_color="#EF4444",
    hover_color="#B91C1C",
    text_color="#FFFFFF",
    border_color="#FCA5A5",
    border_width=2,
    font= ("Segoe UI", 25, "bold"),
    command= lambda:(
        app.destroy()
        if messagebox.askyesno("EXIT GAME","Are you sure to exit the game ? ")
        else None
    )

)

inside_exit_button.place(relx= 0.01,y= 0,anchor= "nw")

open_welcome()

app.mainloop()