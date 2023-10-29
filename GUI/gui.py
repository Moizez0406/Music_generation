import tkinter as tk
from PIL import Image, ImageTk
import os

# Create the main window
root = tk.Tk()
root.title("Music Generation")
root.geometry("500x250+100+100")  # Width x Height + X position + Y position
# Set window transparency (0 to 1, 1 is fully opaque)
root.attributes("-alpha", 1)
root.configure(bg="#333")  # You can use any valid color code here

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)  # Make the row expandable
root.grid_columnconfigure(0, weight=1)  # Make the left column expandable
root.grid_columnconfigure(1, weight=3)  # Make the center column expand more (weight=3)
root.grid_columnconfigure(2, weight=1)  # Make the right column expandable

# Create frames for the three main containers
left_frame = tk.Frame(root, bg="#555")
center_frame = tk.Frame(root, bg="#777")
right_frame = tk.Frame(root, bg="#555")

# Add content to the frames
label_left = tk.Label(left_frame, text="Music Samples", fg="white", bg="#555")
label_left.pack(pady=20)

label_center = tk.Label(center_frame, text="Create Music :D", fg="white", bg="#777")
label_center.pack(pady=20)

label_right = tk.Label(right_frame, text="Trained Models", fg="white", bg="#555")
label_right.pack(pady=20)

# Grid layout: Place the frames in the grid
left_frame.grid(row=0, column=0, sticky="nsew")
center_frame.grid(row=0, column=1, sticky="nsew")
right_frame.grid(row=0, column=2, sticky="nsew")

# Function to load and display MIDI files with music icons
def load_icons():
    # Path to the folder with MIDI files
    folder_path = "D:/Universidad/Semester 5/AI and CV/music_generation/data/raw_data/midi_files"
    music_icon_path = "icons/reproductor-de-musica.png"  # Replace this with the path to your music icon image
    music_icon = Image.open(music_icon_path)
    music_icon = music_icon.resize((50, 50), Image.LANCZOS)  # Resize the music icon as needed
    music_photo = ImageTk.PhotoImage(music_icon)

    for filename in os.listdir(folder_path):
        if filename.endswith(".mid"):  # Assuming all files are MIDI files
            midi_path = os.path.join(folder_path, filename)
            # Display the music icon for each MIDI file
            icon_label = tk.Label(left_frame, image=music_photo, bg="#555")
            icon_label.image = music_photo  # Keep a reference to the image to prevent garbage collection
            icon_label.pack(pady=5)
            # Add the MIDI file name as a label
            label_left.pack()

    # Path to the folder with  Trained models 
    folder_path = "D:/Universidad/Semester 5/AI and CV/music_generation/out/Tmodels"
    neurona_icon_path = "icons/neurona.png"  # Replace this with the path to your music icon image
    neurona_icon = Image.open(neurona_icon_path)
    neurona_icon = neurona_icon.resize((50, 50), Image.LANCZOS)  # Resize the music icon as needed
    icon_photo = ImageTk.PhotoImage(neurona_icon)

    for filename in os.listdir(folder_path):
        if filename.endswith(".keras"):
            keras_path = os.path.join(folder_path, filename)
            # Display the music icon for each MIDI file
            icon_label = tk.Label(right_frame, image=icon_photo, bg="#555")
            icon_label.image = icon_photo  # Keep a reference to the image to prevent garbage collection
            icon_label.pack(pady=5)
            # Add the MIDI file name as a label
            label_right.pack()

    
# Call the function to load and display icons
load_icons()

# Run the Tkinter main loop
root.mainloop()
