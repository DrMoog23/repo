import mido
from mido import Message, MidiFile, MidiTrack

from scales import note_name_to_number, modes, get_scale_notes

def get_chord_progression(notes):
    roman_numerals = [1, 2, 3, 4, 5, 6, 7]
    chords = []
    for i in roman_numerals:
        chord = [notes[i - 1], notes[(i + 1) % 7], notes[(i + 3) % 7]]
        chords.append(chord)
    return chords

modes = {
    'ionian': [0, 2, 4, 5, 7, 9, 11],
    'dorian': [0, 2, 3, 5, 7, 9, 10],
    'phrygian': [0, 1, 3, 5, 7, 8, 10],
    'lydian': [0, 2, 4, 6, 7, 9, 11],
    'mixolydian': [0, 2, 4, 5, 7, 9, 10],
    'aeolian': [0, 2, 3, 5, 7, 8, 10],
    'locrian': [0, 1, 3, 5, 6, 8, 10],
    'harmonic_minor': [0, 2, 3, 5, 7, 8, 11],
    'locrian_6': [0, 1, 3, 5, 6, 9, 10],
    'ionian_augmented': [0, 2, 4, 5, 8, 9, 11],
    'dorian_sharp_4': [0, 2, 3, 6, 7, 9, 10],
    'phrygian_dominant': [0, 1, 4, 5, 7, 8, 10],
    'lydian_sharp_2': [0, 1, 4, 6, 7, 9, 11],
    'ultralocrian_bb7': [0, 1, 3, 4, 6, 8, 9],
    'melodic_minor_ascending': [0, 2, 3, 5, 7, 9, 11],
    'dorian_b2': [0, 1, 3, 5, 7, 9, 10],
    'lydian_augmented': [0, 2, 4, 6, 8, 9, 11],
    'lydian_dominant': [0, 2, 4, 6, 7, 9, 10],
    'mixolydian_b6': [0, 2, 4, 5, 7, 8, 10],
    'aeolian_b5': [0, 2, 3, 5, 6, 8, 10],
    'locrian_2': [0, 2, 3, 5, 6, 8, 10],
    }


root_note = input("Enter the root note: ").capitalize()
mode = input("Enter the mode: ")
degrees = input("Enter the degrees (separated by commas): ")

try:
    scale_notes = get_scale_notes(mode, root_note)
except ValueError as e:
    print(e)
    exit(1)

degree_list = [int(d.strip()) for d in degrees.split(',')]

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12))

if option.lower() == 'notes':
    for note in scale_notes:
        track.append(Message('note_on', note=note + 36, velocity=64, time=0))
        track.append(Message('note_off', note=note + 36, velocity=64, time=480))
elif option.lower() == 'chords':
    chord_progression = get_chord_progression(scale_notes)
    for degree in degree_list:
        chord = chord_progression[degree - 1]
        for note in chord:
            track.append(Message('note_on', note=note + 36, velocity=64, time=0))
        for note in chord:
            track.append(Message('note_off', note=note + 36, velocity=64, time=480))
else:
    print("Invalid option. Choose 'notes' or 'chords'.")
    exit(1)

output_name = root_note + "_" + mode + "_chord_progression.mid"

mid.save(output_name)
print("Chord progression saved as " + output_name)

