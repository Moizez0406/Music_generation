import tkinter as tk
from tkinter import ttk
from content import load_icons
from button_action import *
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
# Make the center column expand more (weight=3)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)  # Make the right column expandable

# Create frames for the three main containers
left_frame = tk.Frame(root, bg="#555")
center_frame = tk.Frame(root, bg="#777")
right_frame = tk.Frame(root, bg="#555")

# Add content to the frames
label_left = tk.Label(left_frame, text="Music Samples", fg="white", bg="#555")
label_left.pack(pady=20)

label_center = tk.Label(
    center_frame, text="Create Music :D", fg="white", bg="#777")
label_center.pack(pady=20)

label_right = tk.Label(
    right_frame, text="Trained Models\n(Select the model you want to generate music)", fg="white", bg="#555")
label_right.pack(pady=20)

# Grid layout: Place the frames in the grid
left_frame.grid(row=0, column=0, sticky="nsew")
center_frame.grid(row=0, column=1, sticky="nsew")
right_frame.grid(row=0, column=2, sticky="nsew")


# Función que se ejecutará cuando se haga clic en el botón
def on_button_click():
    print("¡Botón clickeado!")


# Crear un estilo para el botón
style = ttk.Style()
# Ajusta el padding y el borderwidth
style.configure("TButton", padding=6, relief="flat", borderwidth=10)
style.map("TButton", foreground=[('active', 'blue')], background=[
          ('active', '#FFD700')])  # Cambia el color al pasar el mous

# Crear un botón y añadirlo al contenedor utilizando pack
button = ttk.Button(left_frame, text="Train the model",
                    command=on_button_click, style="TButton")
button.pack(side="bottom", pady=10)

label_midi = load_icons("D:/Universidad/Semester 5/AI and CV/music_generation/data/raw_data/midi_files",
                        "icons/reproductor-de-musica.png", ".mid", left_frame)
label_models = load_icons("D:/Universidad/Semester 5/AI and CV/music_generation/out/Tmodels",
                          "icons/neurona.png", ".keras", right_frame)

# Run the Tkinter main loop
root.mainloop()
