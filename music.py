import pretty_midi
import json
from utils.music_theory import *  # Asegúrate de importar TIEMPO_NEGRA u otras duraciones necesarias

TEMPO = 120  # Este es un ejemplo. Puedes ajustar el valor según tus preferencias (BPM).

# Define una función para convertir notas numéricas en notas MIDI dentro del rango válido [0, 127]
def convert_to_midi_notes(sequence):
    midi_notes = []
    for note_info in sequence:
        # Mapea la nota al rango de tono MIDI válido [0, 127]
        midi_note = max(0, min(note_info["note"], 127))
        # Crea un objeto de nota MIDI con la duración proporcionada
        note = pretty_midi.Note(velocity=100, pitch=midi_note, start=0, end=TIEMPO_NEGRA * note_info["duration"])
        midi_notes.append(note)
    return midi_notes

# Carga la secuencia generada desde el archivo JSON
with open('out/jsondata/generated_music_sequence.json', 'r') as json_file:
    generated_sequence = json.load(json_file)

# Convierte las notas numéricas en notas MIDI con las duraciones asociadas
midi_notes = convert_to_midi_notes(generated_sequence)

# Crea un objeto PrettyMIDI
midi_data = pretty_midi.PrettyMIDI(initial_tempo=TEMPO)

# Crea una instancia de Instrumento para el piano (u otro instrumento de tu elección)
instrument = pretty_midi.Instrument(program=0)  # 0 corresponde al Acoustic Grand Piano

# Agrega las notas generadas al instrumento
for midi_note in midi_notes:
    instrument.notes.append(midi_note)

# Agrega el instrumento a los datos MIDI
midi_data.instruments.append(instrument)

# Guarda la música generada como un archivo MIDI
midi_data.write('out/music/generated_music.mid')
