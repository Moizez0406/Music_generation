import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import shutil


def on_button_clicked():
    print("Button clicked.")


def actualizar_archivos_en_canvas(canvas, lista_de_archivos):
    # Limpiar el contenido actual del canvas
    canvas.delete("all")

    # Agregar archivos .mid al canvas
    for archivo in lista_de_archivos:
        # Lógica para mostrar los archivos en el canvas
        etiqueta = tk.Label(canvas, text=archivo, fg="white", bg="#555")
        # Ajusta las coordenadas según sea necesario
        canvas.create_window((0, 0), anchor="nw", window=etiqueta)


def abrir_explorador_mid(canvas):
    # Define el filtro para permitir solo archivos con extensión .mid
    tipos_de_archivo = [("Archivos MIDI", "*.mid")]
    archivos_seleccionados = filedialog.askopenfilenames(
        filetypes=tipos_de_archivo)

    # Verifica si se seleccionaron archivos
    if archivos_seleccionados:
        # Carpeta destino donde se copiará el archivo
        carpeta_destino = "/home/moises/programming/Music_generation/data/raw_data/midi_files"
        # carpeta_destino = "D:/Universidad/Semester 5/AI and CV/music_generation/data/raw_data/midi_files"
        # Copia el archivo seleccionado a la carpeta destino
        for archivo in archivos_seleccionados:
            shutil.copy(archivo, carpeta_destino)
        print("Archivos MIDI seleccionados:", archivos_seleccionados)
        # Actualiza los archivos en el canvas
        actualizar_archivos_en_canvas(canvas, archivos_seleccionados)
    else:
        print("Ningún archivo MIDI seleccionado. Por favor, elige otro archivo.")


def create_button(text, command, frame):
    style = ttk.Style()
    # Ajusta el padding y el borderwidth
    style.configure("TButton", padding=6, relief="flat", borderwidth=10)
    style.map("TButton", foreground=[('active', 'blue')], background=[
        ('active', '#FFD700')])  # Cambia el color al pasar el mous

    # Crear un botón y añadirlo al contenedor utilizando pack
    button = ttk.Button(frame, text=text,
                        command=command, style="TButton")
    button.pack(side="bottom", pady=10)
