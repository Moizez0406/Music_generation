from keras.models import load_model
from config.config import SEQ_LENGTH
from models.music_model.build_notes import generate_music_sequence, generate_duration_sequence
import numpy as np
import json

# Load the trained model
modelNotes = load_model('out/Tmodels/NEW_notes_model.keras')
num_unique_notes = modelNotes.output_shape[1]
initial_seed = [71, 69, 68, 69, 72, 57, 60, 64,
                74, 60, 64, 72, 71, 60, 64, 72, 76, 57, 60, 64]

# Set the desired length of the generated sequence
sequence_length = 500
generated_sequence = generate_music_sequence(
    initial_seed, sequence_length, num_unique_notes, modelNotes)

# Add random silcences:

try:
    # Save the generated sequence as a JSON file
    with open('out/jsondata/generated_music_sequence_NEW.json', 'w') as json_file:
        json.dump(generated_sequence, json_file)

    # with open('out/jsondata/generated_duration_sequence.json', 'w') as json_file:
    #     json.dump(generated_durations, json_file)

    print("Archivo JSON generado con éxito.")
except Exception as e:
    print(f"Error al generar el archivo MIDI: {e}")
