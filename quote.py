# Motivational quote app
import customtkinter as ctk
import random
from PIL import Image
import pyperclip
from tkinter import messagebox

app = ctk.CTk()
app.title("MOTIVATONAL QUOTES APP")
app.geometry("900x600")
app.configure(fg_color= "#141824")
ctk.set_appearance_mode("dark")

list_quote = [
    "Believe in yourself and keep moving forward.",
    "Small steps lead to big achievements.",
    "Never stop learning, never stop growing.",
    "Dream big, work hard, stay focused.",
    "Every expert was once a beginner.",
    "Your only limit is the one you set yourself.",
    "Success starts with the decision to try.",
    "Make progress, not excuses.",
    "Consistency beats temporary motivation.",
    "Learn from yesterday, live for today.",
    "Difficult roads often lead to great destinations.",
    "Failure is a lesson, not the end.",
    "Be patient, your time will come.",
    "Great things take time and effort.",
    "Focus on becoming better every day.",
    "Your future depends on what you do today.",
    "Turn your challenges into opportunities.",
    "Work quietly and let your progress speak.",
    "Stay curious, stay creative, stay hungry to learn.",
    "One day, your hard work will make you proud."
]

text_1 = ctk.CTkLabel(app,
                    text= "WELCOME TO THE MOTIVATIONAL QUOTE APP",
                    bg_color="#141824",
                    fg_color= "#244038",
                    text_color="#F8FAFC",
                    font= ("Helvetica",40),
                    corner_radius= 30
 )

text_1.place(relx= 0.5,y= 15,anchor= "n")

quote_frame = ctk.CTkFrame(
    app,
    width= 600,
    height= 200,
    corner_radius= 25,
    fg_color= "#202738",
    border_width= 2,
    border_color= "#394867"
)

quote_frame.place(relx= 0.5, rely= 0.50, anchor= "center")

quote_label =  ctk.CTkLabel(
    quote_frame,
    text="",
    text_color="#FFD166",
    font=("Helvetica", 22),
    fg_color= "#141824",
    wraplength=700
)

quote_label.place(relx=0.5, rely=0.45, anchor="center")

def change_quote():
    random_quote= random.choice(list_quote)
    quote_label.configure(text= random_quote)

button_1 = ctk.CTkButton(
    app,
    text= "new quote",
    bg_color=  "#141824",
    fg_color= "#800080",
    text_color= "white",
    width=220,
    height=45,
    corner_radius=16,
    font= ("Helvetica",24),
    command= change_quote
)

button_1.place(relx= 0.5, y= 100,anchor= "n")

def copy():
    current_quote = quote_label.cget("text")

    if current_quote:
        pyperclip.copy(current_quote)
        messagebox.showinfo("Saved to clipboard !",
                            "Saved to clipboard succesfully",
                            parent= app
                            )

    else:
        messagebox.showwarning("NO QUOTE",
                               "First generate a quote",
                               parent= app
                               )

button_2 = ctk.CTkButton(
    app,
    text= "Copy the quote",
    fg_color="#00CED1",
    hover_color="#009688",
    text_color= "#FFFFFF",
    width=220,
    height=45,
    corner_radius=16,
    font=("Helvetica", 20, "bold"),
    command= copy
    )

button_2.place(relx= 0.5,y= 200,anchor= "center")

def save_quote():
    current_quote = quote_label.cget("text")

    if current_quote:
        with open("favourite.txt","a", encoding= "utf-8") as favourite_Quote:
            favourite_Quote.write(current_quote + "\n+\n")

        messagebox.showinfo("Add to favourite",
                            "Saved to favourite",
                            parent= app
                            )

    else:
        messagebox.showwarning("Click favourite",
                               "First press the favourite button",
                               parent= app
                               )

button_3 = ctk.CTkButton(
    app,
    text= "Save to the favourites",
    command= save_quote,
    fg_color= "#16A085"

)

button_3.plac = ctk.CTkButton(
    app,
    text="Save Favorite ❤️",
    command=save_quote

)

button_3.place(relx=0.35, y=470, anchor="center")


def show_favourite():
    try:
        with open("favourite.txt","r", encoding= "utf-8") as file:
            favourites = file.read()
            messagebox.showinfo("My Favourites", favourites)

        if not favourites.strip():
            ("No favourites! first add to favorites")
            return

    except FileNotFoundError:
        messagebox.showinfo("Favourite not found",
                               "Favourites are not added"
                               )

button_4 = ctk.CTkButton(
    app,
    text= "View favourites",
    command= show_favourite,
    fg_color= "#2980B9"

)

button_4.place(relx= 0.5, y= 470, anchor= "center")

def reset_data():
    messagebox.askyesno("PERMISSION TO DELETE DATA",
                        "Do you want to delete all your data"
                        )
    with open("favourite.txt", "w",encoding= "ytf-8") as file:
        pass

button_5 = ctk.CTkButton(
    app,
    text= "Clear all data",
    command= reset_data,
    fg_color= "#C0392B"
)

button_5.place(relx= 0.65, y= 470, anchor= "center")

app.mainloop()