from keras.models import load_model
import numpy as np
import json

# Load the trained model
model = load_model('out/Tmodels/music_model_combined.keras')
SEQ_LENGTH = 20

# Get the number of unique notes from the model output shape
num_unique_notes = model.output_shape[1]

# Define your initial sequence with SEQ_LENGTH elements
# initial_seed = [60, 62, 64, 65, 67, 69, 71, 72, 73, 74, 60, 74, 60, 71, 62, 65, 65, 64, 73, 71]
initial_seed = [60, 62, 64, 65, 67, 69, 71, 72, 73, 74, 60, 62, 64, 65, 67, 69, 71, 72, 73, 74]

# Set the desired length of the generated sequence
sequence_length = 500

# Generate the music sequence
for _ in range(sequence_length):
    if len(initial_seed) >= SEQ_LENGTH:
        # Prepare the last SEQ_LENGTH elements as input data
        input_sequence = np.array(initial_seed[-SEQ_LENGTH:]).reshape(1, SEQ_LENGTH, 1)

        # Expand the input sequence to match the expected shape (None, None, 44)
        input_sequence = np.tile(input_sequence, (1, 1, num_unique_notes))

        # Predict the next note using the model
        predicted_probs = model.predict(input_sequence)[0]

        # Sample the next note based on the predicted probabilities
        next_note = np.random.choice(num_unique_notes, p=predicted_probs)

        # Add the next note to the initial seed
        initial_seed.append(next_note)

# Print or save the generated sequence
print("Generated Music Sequence:", initial_seed)

# Save the generated sequence as a JSON file
with open('out/jsondata/generated_music_sequence.json', 'w') as json_file:
    json.dump(initial_seed, json_file)
