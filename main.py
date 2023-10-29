from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.utils import to_categorical
from utils.music_theory import *
from utils.midi_processing import midi_to_note_sequences, midi_to_one_hot
from utils.data_processing import load_midi_file
from config.config import SEQ_LENGTH, OUTPUT_SHAPE, LSTM_EPOCHS, BATCH_SIZE
import numpy as np

# Load multiple MIDI files and merge the note sequences
midi_files = ["data/raw_data/midi_files/alla-turca.mid", "data/raw_data/midi_files/cap24.mid", "data/raw_data/midi_files/Fur Elise.mid"
              , "data/raw_data/midi_files/winter_no1_allegro.mid", "data/raw_data/midi_files/spring_no1_allegro.mid",
                "data/raw_data/midi_files/summer_no3.mid", "data/raw_data/midi_files/Badinerie.mid"]
all_note_sequences = []
for midi_file_path in midi_files:
    note_sequences = midi_to_note_sequences(midi_file_path)
    all_note_sequences.extend(note_sequences)

print("Note Sequences from MIDI file:", note_sequences)

# Convert merged note sequences to one-hot encoding
all_one_hot_sequences = midi_to_one_hot(all_note_sequences)

# Convert note sequences to one-hot encoded data
# one_hot_sequences = midi_to_one_hot(note_sequences)

num_unique_notes = len(all_one_hot_sequences[0])

# Prepare input and output data from merged one-hot encoded sequences
X = []
y = []
for i in range(0, len(all_one_hot_sequences) - SEQ_LENGTH, 1):
    input_sequence = all_one_hot_sequences[i: i + SEQ_LENGTH]
    output_note = all_one_hot_sequences[i + SEQ_LENGTH]
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
model.fit(X, y, epochs=LSTM_EPOCHS, batch_size=BATCH_SIZE)



# Save the trained model
model.save("out/Tmodels/music_model_combined.keras")
# model.save("out/Tmodels/music_model.h5") #Condered Legacy