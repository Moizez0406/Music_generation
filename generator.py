from keras.models import load_model
from utils.music_theory import TIEMPO_NEGRA
import numpy as np
import json

# Load the trained model
model = load_model('out/Tmodels/music_model.keras')
SEQ_LENGTH = 20

# Get the number of unique notes from the model output shape
num_unique_notes = model.output_shape[1]

# Define your initial sequence with SEQ_LENGTH elements
initial_seed = [60, 62, 64, 65, 67, 69, 71, 72, 73, 74, 60, 74, 60, 71, 62, 65, 65, 64, 73, 71]

# Generate music
generated_sequence = [[note, TIEMPO_NEGRA] for note in initial_seed]

# Set the desired length of the generated sequence
sequence_length = 500

# Generate the music sequence
for _ in range(sequence_length):
    if len(generated_sequence) >= SEQ_LENGTH:
        # Print the length of generated_sequence for debugging
        print("Length of generated_sequence:", len(generated_sequence))
        
        # Prepare the input data for the model (reshape if necessary)
        input_sequence = np.array(generated_sequence[-SEQ_LENGTH:]).reshape(1, SEQ_LENGTH, num_unique_notes)

        # Predict the next note using the model
        predicted_probs = model.predict(input_sequence)[0]

        # Sample the next note based on the predicted probabilities
        next_note = np.random.choice(num_unique_notes, p=predicted_probs)

        # Assign a duration (time) to the note
        note_duration = TIEMPO_NEGRA

        # Add the next note and its duration to the generated sequence
        generated_sequence.append([next_note, note_duration])

# Print or save the generated sequence
print("Generated Music Sequence:", generated_sequence)

# Save the generated sequence as a JSON file
with open('out/jsondata/generated_music_sequence.json', 'w') as json_file:
    json.dump(generated_sequence, json_file)