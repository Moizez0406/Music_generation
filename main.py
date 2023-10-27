from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.utils import to_categorical
from utils.music_theory import *
from utils.midi_processing import midi_to_note_sequences, midi_to_one_hot
from utils.data_processing import load_midi_file
from config.config import LSTM_INPUT_SHAPE, OUTPUT_SHAPE, LSTM_EPOCHS, BATCH_SIZE
import numpy as np

# Constants for data preparation
SEQ_LENGTH = 20
num_unique_notes = 43
STEP = 1

# Load your MIDI note sequences here
midi_file_path = "data/raw_data/midi_files/alla-turca.mid"
note_sequences = midi_to_note_sequences(midi_file_path)
print("Note Sequences from MIDI file:", note_sequences)

# Convert note sequences to one-hot encoded data
one_hot_sequences = midi_to_one_hot(note_sequences)

num_unique_notes = len(one_hot_sequences[0])

X = []
y = []

for i in range(0, len(one_hot_sequences) - SEQ_LENGTH, 1):
    input_sequence = one_hot_sequences[i : i + SEQ_LENGTH]
    output_note = one_hot_sequences[i + SEQ_LENGTH]
    X.append(input_sequence)
    y.append(output_note)

X = np.reshape(X, (len(X), SEQ_LENGTH, num_unique_notes))
y = np.array(y)

# Build the LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, num_unique_notes)))
model.add(Dense(num_unique_notes, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam")

# Train the model
model.fit(X, y, epochs=100, batch_size=64)

# Save the trained model
model.save("out/Tmodels/music_model.keras")
# model.save("out/Tmodels/music_model.h5") #Condered Legacy