# STOP WATCH APP 

import customtkinter as ctk
import time
import winsound

app = ctk.CTk()
app.geometry("900x600")
app.title("STOP WATCH TIMER")
app.config(bg= "#1E1E2E")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

elapsed_time = 0
running = False
start_timestamp = 0

def update_timer():
    if running:
        current_time = time.perf_counter()
        elapsed = elapsed_time + (time.perf_counter() - start_timestamp)

        hours, remainder = divmod(int(elapsed), 3600)
        minutes,seconds = divmod(remainder, 60)

        timersss.configure(state= "normal")
        timersss.delete(0, "end")
        timersss.insert(0, f"{hours:02}:{minutes:02}:{seconds:02}")
        timersss.configure(state= "readonly")

        app.after(100, update_timer)


frame_1 = ctk.CTkFrame(
    app,
    width=400,
    height=130,
    fg_color="#182233",
    corner_radius=20,
    border_width=2,
    border_color="#00CED1"
)

frame_1.place(relx= 0.48,rely= 0.42,anchor= "center")

circle = ctk.CTkCanvas(
    app,
    width= 520,
    height= 500,
    bg= "#1E1E2E",
    highlightthickness= 0
)

circle.place(relx= 0.5, rely= 0.42,anchor= "center")

circle.create_oval(
    25,25,455,455,
    outline= "#00CED1",
    width= 4
)

frame_1.lift()

def reset_time():
    global running,elapsed_time

    winsound.MessageBeep(winsound.MB_ICONASTERISK)

    running = False
    elapsed_time = 0

    timersss.configure(state= "normal")
    timersss.delete(0, "end")
    timersss.insert(0, "00:00:00")
    timersss.configure(state= "readonly")

reset = ctk.CTkButton(
    app,
    text= "RESET TIME",
    width= 80,
    height= 50,
    corner_radius= 25,
    fg_color="#EF4444",
    hover_color="#DC2626",
    text_color="#FFFFFF",
    border_color="#B91C1C",
    border_width=2,
    font= ("Helvetica", 17),
    command= reset_time
)

reset.place(relx= 0.35,y= 550,anchor= "center")

def start_time():
    global running, start_timestamp

    if not running:
        winsound.MessageBeep(winsound.MB_OK)
    
        start_timestamp = time.perf_counter()
        running = True
        update_timer()

start = ctk.CTkButton(
    app,
    text="START TIME",
    width=80,
    height= 50,
    corner_radius= 25,
    fg_color="#10B981",
    hover_color="#059669",
    text_color="#FFFFFF",
    border_color="#34D399",
    border_width=2,
    font= ("Helvetica",17),
    command= start_time
)

start.place(relx= 0.50,y= 550,anchor= "center")

def pause_timer():
    global running,elapsed_time

    if running:

        winsound.MessageBeep(winsound.MB_ICONASTERISK)

        elapsed_time += time.perf_counter() - start_timestamp
        running = False

pause = ctk.CTkButton(
    app,
    text= "PAUSE TIME",
    width= 80,
    height= 50,
    corner_radius= 25,
    fg_color="#F59E0B",
    hover_color="#D97706",
    text_color="#FFFFFF",
    border_color="#FBBF24",
    border_width=2,
    font= ("Helvetica", 17),
    command= pause_timer
)

pause.place(relx= 0.65,y= 550,anchor= "center")

timersss = ctk.CTkEntry(
    frame_1,
    width=340,
    height=85,
    fg_color="#111827",
    text_color="#00CED1",
    border_color="#00CED1",
    border_width=2,
    corner_radius=15,
    font=("Consolas", 40, "bold"),
    justify= "center"
)

timersss.place(relx= 0.5,rely= 0.45,anchor= "center")

timersss.insert(0, "00:00:00")

app.mainloop()