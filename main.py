import numpy as np
from utils.music_theory import *
from utils.midi_processing import *
from models.lstm_model.model import create_lstm_model
from config.config import SEQ_LENGTH, LSTM_EPOCHS, BATCH_SIZE

all_note_sequences = load_midi_file("data/raw_data/midi_files")
# all_note_sequences = load_midi_file("/home/moises/workspace")

# Convert merged note sequences to one-hot encoding
all_one_hot_sequences = midi_to_one_hot(all_note_sequences)
num_unique_notes = len(all_one_hot_sequences[0])

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
model = create_lstm_model(SEQ_LENGTH, num_unique_notes)
# Train the model
model.fit(X, y, epochs=LSTM_EPOCHS, batch_size=BATCH_SIZE)
# Save the trained model
# model.save("out/Tmodels/music_model_combined.keras")
model.save("out/Tmodels/NEW_notes_model.keras")

