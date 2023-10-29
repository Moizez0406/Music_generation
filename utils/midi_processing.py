import pretty_midi
import numpy as np
import os


def load_midi_file(file_path):
    # Get a list of all files in the specified directory
    midi_files = [os.path.join(file_path, file) for file in os.listdir(file_path) if file.endswith(".mid")]

    all_note_sequences = []
    for midi_file_path in midi_files:
        note_sequences = midi_to_note_sequences(midi_file_path)
        all_note_sequences.extend(note_sequences)
    
    return all_note_sequences
        
def midi_to_note_sequences(midi_file_path):
    midi_data = pretty_midi.PrettyMIDI(midi_file_path)
    note_sequences = []
    
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            pitch = note.pitch
            note_sequences.append(pitch)
    
    return note_sequences

def midi_to_one_hot(note_sequences):
    # Create a mapping of pitch values to integers
    pitch_to_int = {pitch: idx for idx, pitch in enumerate(set(note_sequences))}
    num_classes = len(pitch_to_int)

    # One-hot encode the note sequences
    one_hot_sequences = []
    for pitch in note_sequences:
        one_hot_vector = np.zeros(num_classes)
        one_hot_vector[pitch_to_int[pitch]] = 1
        one_hot_sequences.append(one_hot_vector)

    # Return one-hot encoded sequences
    return np.array(one_hot_sequences)

