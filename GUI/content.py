import tkinter as tk
from PIL import Image, ImageTk
import os


# Function to load and display MIDI files with music icons
def load_icons(path_files,path_icons, extension, frame):
    # Path to the folder with MIDI files
    folder_path = path_files
    icon_path = path_icons  # Replace this with the path to your music icon image
    icon = Image.open(icon_path)
    icon = icon.resize((50, 50), Image.LANCZOS)  # Resize the music icon as needed
    photo = ImageTk.PhotoImage(icon)

    for filename in os.listdir(folder_path):
        if filename.endswith(extension): 
            icon_label = tk.Label(frame, image=photo, bg="#555")
            icon_label.image = photo  # Keep a reference to the image to prevent garbage collection
            icon_label.pack(pady=5)

            # Add the file name as a label
            file_name_label = tk.Label(frame, text=filename, fg="white", bg="#555")
            file_name_label.pack()

        