def generate_major_scale(root_note):
    # Define the pattern of intervals for a major scale
    intervals = [0, 2, 4, 5, 7, 9, 11]
    major_scale = [(root_note + interval) % 12 for interval in intervals]
    return major_scale

def generate_minor_scale(root_note):
    # Define the pattern of intervals for a minor scale
    intervals = [0, 2, 3, 5, 7, 8, 10]
    minor_scale = [(root_note + interval) % 12 for interval in intervals]
    return minor_scale

# Definiciones de tiempos
TIEMPO_NEGRA = 1
TIEMPO_BLANCA = 2
TIEMPO_CORCHEA = 0.5
TIEMPO_SEMICORCHEA = 0.25
TIEMPO_FUSA = 0.125
TIEMPO_SEMIFUSA = 0.0625