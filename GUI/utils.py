import tkinter as tk
import pygame
from PIL import Image, ImageTk
import os


selected_file = None  # Variable to store the selected file path


def on_label_click(filename):
    global selected_file
    selected_file = filename


# Function to load and display MIDI files with music icons
def load_icons(path_files, path_icons, extension, frame, bg, click_event=False, ):
    folder_path = path_files
    icon_path = path_icons
    icon = Image.open(icon_path)
    # Resize the music icon as needed
    icon = icon.resize((50, 50), Image.LANCZOS)
    photo = ImageTk.PhotoImage(icon)

    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            icon_label = tk.Label(frame, image=photo, bg=bg)
            icon_label.image = photo  # Keep a reference to the image to prevent garbage collection
            icon_label.pack(pady=5)

            # Add the file name as a label
            file_name_label = tk.Label(
                frame, text=filename, fg="white", bg=bg)
            file_name_label.pack()

            if click_event:
                # Bind the label to the click event
                icon_label.bind("<Button-1>", lambda event,
                                filename=filename: on_label_click(os.path.join(folder_path, filename)))


def on_play_clicked():
    global selected_file
    if selected_file:
        # Play the selected MIDI file using your preferred method/library
        # For example, you can use the pygame library to play MIDI files
        pygame.mixer.init()
        pygame.mixer.music.load(selected_file)
        pygame.mixer.music.play()
    print("Button clicked.")
