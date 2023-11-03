import numpy as np
from config.config import SEQ_LENGTH, UNIQUE_NOTE_DURATION


# Generate the music sequence
def generate_music_sequence(initial_seed, sequence_length, num_unique_notes, model):
    for _ in range(sequence_length):
        if len(initial_seed) >= SEQ_LENGTH:
            # Prepare the last SEQ_LENGTH elements as input data
            input_sequence = np.array(
                initial_seed[-SEQ_LENGTH:]).reshape(1, SEQ_LENGTH, 1)

            # Expand the input sequence to match the expected shape (None, None, 44)
            input_sequence = np.tile(input_sequence, (1, 1, num_unique_notes))

            # Predict the next note using the model
            predicted_probs = model.predict(input_sequence)[0]

            # Sample the next note based on the predicted probabilities
            next_note = np.random.choice(num_unique_notes, p=predicted_probs)

            # Add the next note to the initial seed
            initial_seed.append(next_note)
    return initial_seed


# Generate the duration sequence
def generate_duration_sequence(initial_duration, sequence_length, duration_model, num_unique_durations=UNIQUE_NOTE_DURATION):
    generated_durations = initial_duration.copy()  # Start with initial durations

    for _ in range(sequence_length):
        if len(generated_durations) >= SEQ_LENGTH:
            # Prepare the last SEQ_LENGTH elements as input data for duration
            input_duration_sequence = np.array(
                generated_durations[-SEQ_LENGTH:]).reshape(1, SEQ_LENGTH, 1)

            # Predict the next duration using the duration model
            predicted_duration_probs = duration_model.predict(
                input_duration_sequence)[0]

            # predicted_duration_probs /= np.sum(predicted_duration_probs) # Enable if any error

            # Sample the next duration based on the predicted probabilities
            next_duration = np.random.choice(
                num_unique_durations, p=predicted_duration_probs)

            # Add the next duration to the generated durations
            generated_durations.append(next_duration)

    return generated_durations
