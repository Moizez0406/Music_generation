import numpy as np
from config.config import SEQ_LENGTH

# Generate the music sequence
def generate_music_sequence(initial_seed, sequence_length, num_unique_notes, model):
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
    return initial_seed