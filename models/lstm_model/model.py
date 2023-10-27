from tensorflow import keras


def create_lstm_model(input_shape, output_shape):
    # Define the input layer
    inputs = keras.layers.Input(shape=input_shape)

    # LSTM layer with return_sequences=True for sequence prediction
    lstm1 = keras.layers.LSTM(128, return_sequences=True)(inputs)

    # LSTM layer without return_sequences for the final prediction
    lstm2 = keras.layers.LSTM(128)(lstm1)

    # Output layer with softmax activation for categorical prediction
    outputs = keras.layers.Dense(output_shape, activation='softmax')(lstm2)

    # Create the model
    model = keras.models.Model(inputs=inputs, outputs=outputs)

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model