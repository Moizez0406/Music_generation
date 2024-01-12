import tkinter as tk
from utils import load_icons,  on_play_clicked
from buttons import *
import os

# Create the main window
root = tk.Tk()
root.title("Music Generation")
root.geometry("500x250+100+100")  # Width x Height + X position + Y position
root.attributes("-alpha", 1)  # 0 - 1 transparency
root.configure(bg="#333")

# Configure the grid layout
root.grid_rowconfigure(0, weight=1)  # Make the row expandable
root.grid_columnconfigure(0, weight=1)  # Make the left column expandable
root.grid_columnconfigure(1, weight=3)  # Make the center column expandable
root.grid_columnconfigure(2, weight=1)  # Make the right column expandable

# Create frames for the three main containers
left_frame = tk.Frame(root, bg="#555")
center_frame = tk.Frame(root, bg="#777")
right_frame = tk.Frame(root, bg="#555")

# Create a Notebook widget for the center frame
center_frame = ttk.Notebook(root)
center_frame.grid(row=0, column=1, sticky="nsew")

# Create tabs
first_tab = tk.Frame(center_frame, bg="#777")
second_tab = tk.Frame(center_frame, bg="#777")
center_frame.add(first_tab, text="Generated Music")
center_frame.add(second_tab, text="Fix some parameters")

# Add content to the frames
label_left = tk.Label(left_frame, text="Music Samples", fg="white", bg="#555")
label_right = tk.Label(
    right_frame, text="Trained Models\n(Select the model from which you want to generate music)", fg="white", bg="#555")

for label in [label_left, label_right]:
    label.pack(pady=20)


# Grid layout: Place the frames in the grid
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=2, sticky="nsew")

create_button("Train the model", on_button_clicked, left_frame)
create_button("Add", abrir_explorador_mid, left_frame)

# Configura la barra de desplazamiento para que se desplace con el mouse y el teclado
scrollbar = tk.Scrollbar(left_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

ttk.Style().theme_use("clam")

# Configura el canvas con la barra de desplazamiento
canvas = tk.Canvas(left_frame, bg="#555", yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=canvas.yview)


load_icons("/home/moises/programming/Music_generation/data/raw_data/midi_files",
           "icons/reproductor-de-musica.png", ".mid", canvas, "#555")

load_icons("/home/moises/programming/Music_generation/out/music",
           "icons/lira.png", ".mid", first_tab, "#777", True)

load_icons("/home/moises/programming/Music_generation/out/Tmodels",
           "icons/neurona.png", ".keras", right_frame, "#555")

create_button("Play", on_play_clicked, first_tab)
# Run the Tkinter main loop
root.mainloop()
