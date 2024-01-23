import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from music21 import converter, instrument, chord
import numpy as np

def midi_to_chord_array(file_path):
    midi = converter.parse(file_path)
    parts = instrument.partitionByInstrument(midi)

    chords = []
    for part in parts.parts:
        if 'Piano' in str(part):  # Assuming piano part for simplicity
            chords_to_parse = part.recurse().notesAndRests
            current_chord = []

            for element in chords_to_parse:
                if isinstance(element, chord.Chord):
                    current_chord.append('.'.join(str(n) for n in element.pitches))
                elif isinstance(element, note.Note):
                    if current_chord:
                        chords.append(current_chord)
                        current_chord = []

            if current_chord:
                chords.append(current_chord)

    return np.array(chords)

# Replace 'path/to/your/midi/file.mid' with the path to your MIDI file
midi_file_path = 'data/raw_data/midi_files/cap24.mid'
harmony = midi_to_chord_array(midi_file_path)


# Dummy data (replace with your actual data)
X_train = np.random.rand(100, 10, 1)  # 100 samples, 10 time steps, 1 feature
y_train = np.random.rand(100, 10, 1)

# Model architecture
model = Sequential()
model.add(LSTM(units=50, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
