import tkinter as tk
import time 
from PIL import Image, ImageTk

# Main window
root = tk.Tk()
root.title("Photo slideshow album")
root.geometry("900x600")

# List of image path
image_path =[
    r"c:\Users\Raghav kalra\Desktop\Graphics designing and motion graphics data\Graphics designing\13.jpeg",
    r"c:\Users\Raghav kalra\Desktop\Graphics designing and motion graphics data\Graphics designing\25.jpeg",
    r"c:\Users\Raghav kalra\Desktop\Graphics designing and motion graphics data\Graphics designing\26.jpeg",
    r"c:\Users\Raghav kalra\Desktop\Graphics designing and motion graphics data\Graphics designing\28.jpeg",
]

image_size = (800,500)
images= []
for path in image_path:
    img= Image.open(path)
    img= img.resize(image_size)
    images.append(img) # Adding each image in list

# Convert PIL images into tkinter compatible list 
final_image= []
for img in images:
    photo = ImageTk.PhotoImage(img) 
    final_image.append(photo)

# Label widgets to keep photos
image_label = tk.Label(root)
image_label.pack(pady= 30)

# slideshow Function
def start_slideshow():
    for photo in final_image:
        image_label.config(image=photo)
        image_label.image= photo
        root.update()
        time.sleep(2)

# Button
play_button= tk.Button(
    root,
    text= "Play the slideshow",
    font= ("Arial", 17),
    command=start_slideshow
    )

play_button.pack(pady=40)

root.mainloop()


