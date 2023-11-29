import pretty_midi
import json
from utils.music_theory import *  # Asegúrate de importar TIEMPO_NEGRA u otras duraciones necesarias

TEMPO = 120  # Este es un ejemplo. Puedes ajustar el valor según tus preferencias (BPM).

# Carga la secuencia generada desde el archivo JSON
# with open('out/jsondata/generated_music_sequence.json', 'r') as json_file:
    # generated_sequence = json.load(json_file)
with open('out/jsondata/generated_music_sequence.json', 'r') as json_file:
    generated_sequence = json.load(json_file)

# Formatea la secuencia generada según el formato [nota, duración]
formatted_sequence = []
for note in generated_sequence:
    # Asigna una duración fija a cada nota (por ejemplo, TIEMPO_NEGRA)
    duration = TIEMPO_NEGRA  # Puedes ajustar esta duración según tus preferencias
    formatted_sequence.append([note, duration])
    
# Define una función para convertir notas numéricas en notas MIDI dentro del rango válido [0, 127]
def convert_to_midi_notes(sequence):
    midi_notes = []
    current_time = 0  # Lleva el seguimiento del tiempo actual para asignar las duraciones de las notas
    for note_info in sequence:
        # Mapea la nota al rango de tono MIDI válido [0, 127]
        midi_note = max(0, min(note_info[0], 127))
        # Calcula el tiempo de finalización de la nota basado en la duración proporcionada
        end_time = current_time + TIEMPO_SEMICORCHEA * note_info[1]
        # Crea un objeto de nota MIDI con la duración proporcionada
        note = pretty_midi.Note(velocity=100, pitch=midi_note, start=current_time, end=end_time)
        midi_notes.append(note)
        # Actualiza el tiempo actual para la próxima nota
        current_time = end_time
    return midi_notes


try:
    # Convierte las notas numéricas en notas MIDI con las duraciones asociadas
    midi_notes = convert_to_midi_notes(formatted_sequence)
    midi_data = pretty_midi.PrettyMIDI(initial_tempo=TEMPO)
    instrument = pretty_midi.Instrument(program=0)  # 0 corresponde al Acoustic Grand Piano

    # Agrega las notas generadas al instrumento
    for midi_note in midi_notes:
        instrument.notes.append(midi_note)

    # Agrega el instrumento a los datos MIDI
    midi_data.instruments.append(instrument)

    # Guarda la música generada como un archivo MIDI
    midi_data.write('out/music/generated_OnlyBadi.mid')
    print("Archivo MIDI generado con éxito.")
except Exception as e:
    print(f"Error al generar el archivo MIDI: {e}")
