import pretty_midi
import json
from utils.music_theory import *  # Make sure to import TIEMPO_NEGRA or other necessary durations
import numpy as np
import time

TEMPO = 120

# Load the generated sequence from the JSON file
with open('out/jsondata/generated_music_sequence.json', 'r') as json_file:
    generated_sequence = json.load(json_file)

# Format the generated sequence as [note, duration]
formatted_sequence = []
for note in generated_sequence:
    # Choose the range for the random note duration
    lower_bound = min(TIEMPO_SEMIFUSA, TIEMPO_FUSA, TIEMPO_SEMICORCHEA, TIEMPO_CORCHEA, TIEMPO_NEGRA, TIEMPO_BLANCA)
    upper_bound = max(TIEMPO_SEMIFUSA, TIEMPO_FUSA, TIEMPO_SEMICORCHEA, TIEMPO_CORCHEA, TIEMPO_NEGRA, TIEMPO_BLANCA)

    # Generate a random note duration within the specified range
    note_duration = np.random.uniform(lower_bound, upper_bound)
    formatted_sequence.append({'note': note, 'duration': note_duration})

# Function to add random silences between notes
# def add_random_silences(sequence, num_silences, min_silence_duration, max_silence_duration):
#     np.random.seed(int(time.time()))  # Set a seed based on the current time
#     new_sequence = []
#     for note_info in sequence:
#         new_sequence.append(note_info)
#         for _ in range(num_silences):
#             silence_duration = np.random.uniform(min_silence_duration, max_silence_duration)
#             new_sequence.append({'note': None, 'duration': silence_duration})
#     return new_sequence

# Number of random silences to add between notes
num_silences = 3

# Minimum and maximum duration of the random silences
min_silence_duration = 0.1
max_silence_duration = 0.5

# Add random silences to the formatted sequence
# sequence_with_silences = add_random_silences(formatted_sequence, num_silences, min_silence_duration, max_silence_duration)

# Function to convert notes to MIDI
def convert_to_midi_notes(sequence):
    midi_notes = []
    current_time = 0
    for note_info in sequence:
        if note_info['note'] is not None:
            midi_note = max(0, min(note_info['note'], 127))
            end_time = current_time + TIEMPO_SEMICORCHEA * note_info['duration']
            note = pretty_midi.Note(velocity=100, pitch=midi_note, start=current_time, end=end_time)
            midi_notes.append(note)
            current_time = end_time
        else:
            current_time += note_info['duration']  # Skip the duration of the silence
    return midi_notes

try:
    midi_notes = convert_to_midi_notes(formatted_sequence)
    midi_data = pretty_midi.PrettyMIDI(initial_tempo=TEMPO)
    instrument = pretty_midi.Instrument(program=0)

    for midi_note in midi_notes:
        instrument.notes.append(midi_note)

    midi_data.instruments.append(instrument)
    midi_data.write('out/music/generated_NEW.mid')
    print("MIDI file generated successfully.")
except Exception as e:
    print(f"Error generating MIDI file: {e}")
