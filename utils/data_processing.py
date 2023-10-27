import mido


def load_midi_file(file_path):
    mid = mido.MidiFile(file_path)
    notes = []
    for msg in mid.play():
        if msg.type == 'note_on':
            notes.append(msg.note)
    return notes
