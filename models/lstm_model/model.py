from keras.models import Sequential
from keras.layers import LSTM, Dense


def create_lstm_model(SEQ_LENGTH, num_unique_notes):
    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(128, input_shape=(SEQ_LENGTH, num_unique_notes)))
    model.add(Dense(num_unique_notes, activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    
    return model