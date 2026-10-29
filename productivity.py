# My productivity arena app
import customtkinter as ctk
import os
from datetime import date
import tkinter.messagebox as messagebox
import webbrowser

app = ctk.CTk()
app.geometry("1200x800")
app.title("MY PRODUCTIVITY ARENA")
app.config(bg= "#111827" )
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

home_page = ctk.CTkFrame(
    app,
    width= 950,
    height= 800,
    fg_color="#111827"
)

to_do_list_page = ctk.CTkFrame(
    app,
    width= 950,
    height= 800,
    fg_color= "#111827"
)

quick_notes_page = ctk.CTkFrame(
    app,
    width= 950,
    height= 800,
    fg_color= "#111827"
)

about_page = ctk.CTkFrame(
    app,
    width= 950,
    height=800,
    fg_color= "#111827"
)

webbrowser_page = ctk.CTkFrame(
    app,
    width= 950,
    height= 800,
    fg_color= "#111827"
)

view_note_page = ctk.CTkFrame(
    app,
    width= 950,
    height= 800,
    fg_color="#111827"
)

def home_to_view_note():
    home_page.forget()
    view_note_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    view_note_page.tkraise()
    view_note_page.lift()

def view_note_to_home():
    view_note_page.forget()
    home_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    home_page.tkraise()
    home_page.lift()

def home_to_about():
    home_page.forget()
    about_page.place(x= 0,y= 0, relwidth= 1,relheight= 1 )
    about_page.tkraise()
    about_page.lift()

def about_to_home():
    about_page.forget()
    home_page.place(x= 0,y=0,relwidth= 1,relheight= 1)
    home_page.tkraise()
    home_page.lift()

def home_to_list():
    home_page.forget()
    to_do_list_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    to_do_list_page.tkraise()
    to_do_list_page.lift()

def list_to_home():
    to_do_list_page.forget()
    home_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    home_page.tkraise()
    home_page.lift()

def home_to_notes():
    home_page.forget()
    quick_notes_page.place(x= 0 ,y= 0, relwidth= 1, relheight= 1)
    quick_notes_page.tkraise()
    quick_notes_page.lift()

def notes_to_home():
    quick_notes_page.forget()
    home_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    home_page.tkraise()
    home_page.lift()

def home_to_webopener():
    home_page.forget()
    webbrowser_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    webbrowser_page.tkraise()
    webbrowser_page.lift()

def webopener_to_home():
    webbrowser_page.forget()
    home_page.place(x= 0,y= 0,relwidth= 1,relheight= 1)
    home_page.tkraise()
    home_page.lift()

date = date.today().strftime("%d-%m-%Y")
date_label = f"Today date is: {date} "

view_note_button = ctk.CTkButton(
    home_page,
    text= "view saved notes",
    width= 50,
    height= 30,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= home_to_view_note

)

view_note_button.place(relx=0.95,y= 150,anchor= "ne")

greeting = ctk.CTkLabel(
    home_page,
    text= date_label,
    width= 200,
    height= 50, 
    font= ("Segoe UI", 25,"bold"),
    text_color="#00D4FF",
    bg_color="#111827",    
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,        
    corner_radius=20
)

greeting.place(relx= 0.5,y= 0,anchor= "n")

heading= ctk.CTkLabel(
    home_page,
    text= "MY PRODUCTIVITY ARENA ",
    width= 250,
    height= 70,
    corner_radius= 25,
    font= ("Segoe UI", 50, "bold"),
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2
)

heading.place(relx= 0.5,y=60,anchor= "n")

sub_head= ctk.CTkLabel(
    home_page,
    text= "YOUR PERSONAL PRODUCTIVITY SPACE \n USE NOW",
    font= ("Segoe UI", 15, "italic"),
    text_color= "white",
    bg_color= "#111827",
)

sub_head.place(relx= 0.5,y= 130,anchor= "n")

to_do_list = ctk.CTkButton(
    home_page,
    text= "TO DO LIST",
    width= 350,
    height= 150,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= home_to_list
)

to_do_list.place(relx= 0.05,y= 650,anchor= "sw")


quck_notes = ctk.CTkButton(
    home_page,
    text= "QUICK NOTES",
    width= 350,
    height= 150,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= home_to_notes
)

quck_notes.place(relx= 0.45,y= 650,anchor= "s")

web_opener = ctk.CTkButton(
    home_page,
    text= "IMPORTANT WEBSITES",
    width= 350,
    height= 150,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= home_to_webopener
)

web_opener.place(relx= 0.75,y= 650,anchor= "s")

python_projects = ctk.CTkButton(
    home_page,
    text= "PYTHON PROJECTS",
    width= 650,
    height= 150,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= lambda:webbrowser.open("https://github.com/raghavkalra09785/my_python_apps")
)

python_projects.place(relx= 0.5,y= 350,anchor= "center")

about_button = ctk.CTkButton(
    home_page,
    text= "ABOUT",
    width= 50,
    height= 25,
    corner_radius= 20,
    bg_color= "#111827",
    hover_color="#00D4FF",
    fg_color="#1F2937",
    text_color="#FFFFFF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 30,"bold"),
    command= home_to_about
)

about_button.place(relx= 0.00,y= 10,anchor= "nw")

heading_about_page = ctk.CTkLabel(
    about_page,
    text= "ABOUT THIS APP",
    width= 200,
    height= 70,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    corner_radius= 25,
    font= ("Segoe UI", 50,"bold")
)

heading_about_page.place(relx= 0.5,y= 10,anchor= "n")

about_content_about_page = ctk.CTkLabel(
    about_page,
    text= "this app is a productivity app made by raghav kalra with python and customtkinter",
    bg_color= "#111827",
    fg_color="#111827",
    text_color= "white",
    font= ("Segoe UI", 20, "italic")
)

about_content_about_page.place(relx= 0.5,y= 250,anchor= "center")

learn_more_aboutpage = ctk.CTkLabel(
    about_page,
    text= "learn more from here",
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "blue",
    font= ("Segoe UI", 20,"underline")
)

learn_more_aboutpage.place(relx= 0.5,y= 280,anchor= "center")

back_about_to_home = ctk.CTkButton(
    about_page,
    text= "<- BACK",
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica", 20, "bold"),
    command= about_to_home
)

back_about_to_home.place(relx= 0.00,y= 00,anchor= "nw")

back_from_list = ctk.CTkButton(
    to_do_list_page,
    text= "<- Back",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",20,"bold"),
    command= list_to_home
)

back_from_list.place(relx= 0.00,y= 00,anchor= "nw")

to_do_list_frame = ctk.CTkFrame(
    to_do_list_page,
    height= 350,
    width= 900,
    fg_color= "#111827",
    bg_color= "#111827",
    border_color= "#A78BFA",
    border_width= 2
    )

to_do_list_frame.place(relx= 0.40,y= 350,anchor= "center")

heading_list_page = ctk.CTkLabel(
    to_do_list_page,
    text= "TO DO LIST APP",
    width= 200,
    height= 70,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    corner_radius= 25,
    font= ("Segoe UI", 50,"bold")
    )
heading_list_page.place(relx= 0.5,y=10,anchor= "n")

task_1_in_list = ctk.CTkLabel(
    to_do_list_frame,
    text= "MGD - Motion Graphics designing",
    bg_color="#111827",
    fg_color= "#111827",
    text_color= "white",
    font= ("Segoe UI", 20,"underline")
)

task_1_in_list.place(relx= 0.05,y=20,anchor= "nw")

task_2_in_list = ctk.CTkLabel(
    to_do_list_frame,
    text= "GD - Graphics designing",
    bg_color="#111827",
    fg_color= "#111827",
    text_color= "white",
    font= ("Segoe UI", 20,"underline")
)

task_2_in_list.place(relx= 0.05,y=70,anchor= "nw")

task_3_in_list = ctk.CTkLabel(
    to_do_list_frame,
    text= "CODING - Python Coding and app development concepts",
    bg_color="#111827",
    fg_color= "#111827",
    text_color= "white",
    font= ("Segoe UI", 20,"underline")
)

task_3_in_list.place(relx= 0.05,y=120,anchor= "nw")

task_4_in_list = ctk.CTkLabel(
    to_do_list_frame,
    text= "STUDY OF SCHOOL",
    bg_color="#111827",
    fg_color= "#111827",
    text_color= "white",
    font= ("Segoe UI", 20,"underline")
)

task_4_in_list.place(relx= 0.05,y=170,anchor= "nw")

task_5_in_list = ctk.CTkLabel(
    to_do_list_frame,
    text= "IAIO - Learning concepts of AI",
    bg_color="#111827",
    fg_color= "#111827",
    text_color= "white",
    font= ("Segoe UI", 20,"underline")
)

task_5_in_list.place(relx= 0.05,y=220,anchor= "nw")

def task_1():
    task_1_in_list.configure(font= ("Segoe UI", 20, "overstrike"))

task_1_complete_button = ctk.CTkButton(
    to_do_list_frame,
    text= "COMPLETE",
    height= 20,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    command= task_1
)

task_1_complete_button.place(relx= 0.85,y= 20,anchor= "ne")

def task_2_complete():
    task_2_in_list.configure(font= ("Segoe UI",20, "overstrike"))

task_2_complete_button = ctk.CTkButton(
    to_do_list_frame,
    text= "COMPLETE",
    height= 20,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    command= task_2_complete
)

task_2_complete_button.place(relx= 0.85,y= 70,anchor= "ne")

def task_3_complete():
    task_3_in_list.configure(font= ("Segoe UI", 20, "overstrike"))

task_3_complete_button = ctk.CTkButton(
    to_do_list_frame,
    text= "COMPLETE",
    height= 20,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    command= task_3_complete
)

task_3_complete_button.place(relx= 0.85,y= 120,anchor= "ne")

def task_4_complete():
    task_4_in_list.configure(font= ("Segoe UI", 20 , "overstrike"))

task_4_complete_button = ctk.CTkButton(
    to_do_list_frame,
    text= "COMPLETE",
    height= 20,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    command= task_4_complete
)

task_4_complete_button.place(relx= 0.85,y= 170,anchor= "ne")

def task_5_complete():
    task_5_in_list.configure(font= ("Segoe UI" ,20 ,"overstrike"))

task_5_complete_button = ctk.CTkButton(
    to_do_list_frame,
    text= "COMPLETE",
    height= 20,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    command= task_5_complete
)

task_5_complete_button.place(relx= 0.85,y= 220,anchor= "ne")

notes_back_home_button = ctk.CTkButton(
    quick_notes_page,
    text= "<- Back",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",20,"bold"),
    command= notes_to_home
)
    
notes_back_home_button.place(relx= 0.00,y= 00,anchor= "nw")

back_to_home_from_webopener = ctk.CTkButton(
    webbrowser_page,
    text= "<- Back",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",20,"bold"),
    command= notes_to_home
    )
        
back_to_home_from_webopener.place(relx= 0.00,y= 00,anchor= "nw")

heading_notes_page = ctk.CTkLabel(
    quick_notes_page,
    text= "QUICK NOTES",
    width= 200,
    height= 70,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    corner_radius= 25,
    font= ("Segoe UI", 50,"bold")
        )

heading_notes_page.place(relx= 0.5,y=10,anchor= "n")

heading_web_page = ctk.CTkLabel(
    webbrowser_page,
    text= "IMPORTANT WEBSITES",
    width= 200,
    height= 70,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    corner_radius= 25,
    font= ("Segoe UI", 50,"bold")
    )

heading_web_page.place(relx= 0.5,y=10,anchor= "n")

webbrowser_page_frame = ctk.CTkFrame(
    webbrowser_page,
    width= 600,
    height= 100,
    fg_color="#1F2937",
    bg_color="#111827",
    border_color="#00D4FF",
    border_width=2,
    corner_radius=25
)

webbrowser_page_frame.place(relx= 0.5,y= 450,anchor= "center")

spotify_button = ctk.CTkButton(
    webbrowser_page_frame,
    text= "SPOTIFY",
    fg_color="#1DB954",
    hover_color="#1ED760",
    text_color="#FFFFFF",
    border_color="#1DB954",
    border_width=2,
    font=("Bahnschrift SemiBold", 25, "bold"),
    command= lambda: webbrowser.open("https://open.spotify.com/")
)

spotify_button.place(relx= 0.05,y= 20,anchor= "nw")

youtube_button = ctk.CTkButton(
    webbrowser_page_frame,
    text= "YOUTUBE",
    fg_color="#FF0000",
    hover_color="#CC0000",
    text_color="#FFFFFF",
    border_color="#FF0000",
    border_width=2,
    font=("Bahnschrift SemiBold", 25, "bold"),
    command= lambda: webbrowser.open("https://www.youtube.com/")
)

youtube_button.place(relx= 0.40,y= 20,anchor= "nw")

github_button = ctk.CTkButton(
    webbrowser_page_frame,
    text= "GITHUB",
    fg_color="#24292F",
    hover_color="#40464D",
    text_color="#FFFFFF",
    border_color="#FFFFFF",
    border_width=2,
    font=("Bahnschrift SemiBold", 25, "bold"),
    command= lambda: webbrowser.open("https://github.com/")
)

github_button.place(relx= 0.75,y= 20,anchor= "nw")

sub_head_webopener = ctk.CTkLabel(
    webbrowser_page,
    text= "OPEN YOUR WEBSITES BY CLICKING ON THEM",
    text_color="#00D4FF",
    fg_color="#111827",
    bg_color= "#111827",
    border_color="#00D4FF",
    border_width= 1,
    font= ("Segoe UI", 20, "italic")
)

sub_head_webopener.place(relx= 0.5,y= 350,anchor= "center")

quick_notes_area = ctk.CTkTextbox(
    quick_notes_page,
    width= 800,
    height= 450,
    fg_color="#1F2937",
    text_color="#9CA3AF",
    border_color="#00D4FF",
    border_width=2,
    font= ("Segoe UI", 20, "bold"),
    wrap= "word"
)

quick_notes_area.place(relx= 0.5,y= 400, anchor= "center")

saved_note_box = ctk.CTkTextbox(
    view_note_page,
    width= 700,
    height= 500,
    corner_radius= 25,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    font= ("Segoe UI" , 25, "bold")
)

saved_note_box.place(relx= 0.5,y= 400, anchor= "center")

NOTES_FOLDER = "saved_notes"
os.makedirs(NOTES_FOLDER,exist_ok= True)

def save_notes():
    note = quick_notes_area.get("1.0", "end-1c").strip()

    if not note:
        saved_note_box.delete("1.0", "end")
        saved_note_box.insert("1.0", "No saved notes yet!")
        return
    
    existing_files = [
        f for f in os.listdir(NOTES_FOLDER)
        if f.startswith("note_") and f.endswith(".txt")
    ]

    note_number = 1
    while f"note_{note_number}.txt" in existing_files:
        note_number +=1

    file_path = os.path.join(
        NOTES_FOLDER,
        f"note_{note_number}.txt"
    )

    with open (file_path, "w", encoding= "utf-8") as file:
        file.write(note)

    messagebox.showinfo("Saved succesfully","note saved succesfully")

def view_saved_notes():
    saved_note_box.delete("1.0", "end")

    note_file = [
        f for f in os.listdir(NOTES_FOLDER)
        if f.startswith("note_") and f.endswith(".txt")
    ]

    note_file.sort(
        key= lambda name: int(
            name.removeprefix("note_").removesuffix(".txt")
        )
    )

    if not note_file:
        quick_notes_area.insert("1.0", "NO SAVED NOTE! first save a note")
        return

    for file_name in note_file:
        file_path = os.path.join(NOTES_FOLDER,file_name)

    with open(file_path, "r", encoding= "utf-8") as files:
        note = files.read()

    saved_note_box.insert(
        "end",
        f"--- {file_name} ---\n{note}\n\n"
    )

back_from_notes_view_to_home_button = ctk.CTkButton(
    view_note_page,
    text= "<- Back",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",20,"bold"),
    command= view_note_to_home
    )
        
back_from_notes_view_to_home_button.place(relx= 0.00,y= 00,anchor= "nw")

save_button = ctk.CTkButton(
    quick_notes_page,
    text= "save note",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",25,"bold"),
    command= save_notes
)

save_button.place(relx= 0.5,y= 100,anchor= "n")

view_note_button = ctk.CTkButton(
    view_note_page,
    text= "view note",
    width= 200,
    height= 50,
    fg_color= "#111827",
    bg_color= "#111827",
    text_color= "white",
    font= ("Helvetica",25,"bold"),
    command= view_saved_notes
)

view_note_button.place(relx= 0.5,y= 100,anchor= "n")

exit_button = ctk.CTkButton(
    home_page,
    text= "EXIT APP",
    fg_color="#DC2626",
    hover_color="#991B1B",
    text_color="#FFFFFF",
    border_color="#F87171",
    border_width=2,
    font= ("Segoe UI", 25, "bold"),
    command= lambda:(
        app.destroy()
        if messagebox.askyesno("QUIT APP", "Does You Want To Quit The App")
        else None
    )
)

exit_button.place(relx= 0.99,y= 5,anchor= "ne")

view_note_page_head = ctk.CTkLabel(
    view_note_page,
    text= "View notes",
    width= 200,
    height= 70,
    bg_color="#111827",
    text_color="#A78BFA",
    fg_color="#1F2937",
    border_color="#00D4FF",
    border_width=2,
    corner_radius= 25,
    font= ("Segoe UI", 50,"bold")
    )
    
view_note_page_head.place(relx= 0.5,y=10,anchor= "n")


home_page.place(
    x=0, y=0,
    relwidth=1,
    relheight=1
)

app.mainloop()