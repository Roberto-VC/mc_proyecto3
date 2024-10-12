from music import *
import random

# Set up the tempo

score = Score("Joyful Beats", 120.0)
# Define the transition matrix for the primary notes
primary_transition_matrix = [
    [0.4, 0.3, 0.2, 0.05, 0.05, 0.0, 0.0],  # From C
    [0.3, 0.4, 0.2, 0.0, 0.1, 0.0, 0.0],  # From D
    [0.2, 0.2, 0.4, 0.1, 0.1, 0.0, 0.0],  # From E
    [0.1, 0.0, 0.1, 0.4, 0.3, 0.0, 0.0],  # From F
    [0.2, 0.1, 0.1, 0.3, 0.4, 0.0, 0.0],  # From G
    [0.1, 0.0, 0.0, 0.1, 0.2, 0.4, 0.2],  # From A
    [0.0, 0.1, 0.0, 0.0, 0.1, 0.3, 0.5],  # From B
]

# Define the transition matrix for the accompanying notes
accompanying_transition_matrix = [
    [0.3, 0.15, 0.15, 0.05, 0.05, 0.0, 0.0, 0.3],  # From C (includes rest)
    [0.2, 0.2, 0.2, 0.0, 0.1, 0.0, 0.0, 0.3],  # From D
    [0.2, 0.1, 0.2, 0.1, 0.1, 0.0, 0.0, 0.3],  # From E
    [0.1, 0.0, 0.1, 0.2, 0.2, 0.0, 0.0, 0.3],  # From F
    [0.2, 0.1, 0.1, 0.2, 0.2, 0.0, 0.0, 0.3],  # From G
    [0.1, 0.0, 0.0, 0.1, 0.1, 0.3, 0.1, 0.3],  # From A
    [0.0, 0.1, 0.0, 0.0, 0.1, 0.3, 0.4, 0.3],  # From B
    [0.1, 0.0, 0.1, 0.0, 0.1, 0.0, 0.0, 0.7],  # From Rest (always stay at rest)
]

harmony_transition_matrix = [
    [0.3, 0.2, 0.2, 0.1, 0.1, 0.0, 0.0, 0.1],  # From C
    [0.2, 0.3, 0.2, 0.1, 0.1, 0.0, 0.0, 0.1],  # From D
    [0.2, 0.1, 0.3, 0.1, 0.1, 0.0, 0.0, 0.1],  # From E
    [0.1, 0.0, 0.1, 0.3, 0.2, 0.0, 0.0, 0.1],  # From F
    [0.2, 0.1, 0.1, 0.2, 0.3, 0.0, 0.0, 0.1],  # From G
    [0.1, 0.0, 0.0, 0.1, 0.1, 0.4, 0.1, 0.1],  # From A
    [0.0, 0.1, 0.0, 0.0, 0.1, 0.3, 0.5, 0.1],  # From B
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],  # From Rest (no longer always stay at rest)
]

percussion_transition_matrix = [
    [0.5, 0.2, 0.1, 0.1, 0.1],  # From Kick
    [0.2, 0.5, 0.2, 0.0, 0.1],  # From Snare
    [0.1, 0.1, 0.5, 0.2, 0.1],  # From Hi-hat
    [0.1, 0.1, 0.1, 0.5, 0.2],  # From Cymbal
    [0.1, 0.1, 0.1, 0.1, 0.5],  # From Rest
]

# List of MIDI pitches for primary notes (C, D, E, F, G, A, B)
primary_midi_pitches = [60, 64, 67, 65, 69, 71, 72]

# List of MIDI pitches for accompanying notes (E, F, G, A, B, C, D)
accompanying_midi_pitches = [60, 64, 67, 65, 69, 71, 72, REST]

harmony_midi_pitches = [60, 64, 67, 65, 69, 71, 72, REST]  # Adding 0 for Rest

percussion_midi_pitches = [MTR, OTR, RBL, RC1, REST]  # Kick, Snare, Hi-hat, Cymbal, Rest



# Generate a melody using the Markov chain
def generate_melody(transition_matrix, num_notes):
    melody = []
    current_state = random.randint(0, len(transition_matrix) - 1)
    
    for _ in range(num_notes):
        melody.append(current_state)
        # Generate a random number to decide the next state based on the transition probabilities
        rand_value = random.random()
        cumulative_probability = 0.0
        
        for next_state, probability in enumerate(transition_matrix[current_state]):
            cumulative_probability += probability
            if rand_value < cumulative_probability:
                current_state = next_state
                break
        
    return melody

# Generate the primary melody
num_notes = 64
primary_states = generate_melody(primary_transition_matrix, num_notes)
accompanying_states = generate_melody(accompanying_transition_matrix, num_notes)
harmony_states = generate_melody(harmony_transition_matrix, num_notes/4)
percussion_states = generate_melody(percussion_transition_matrix, num_notes/4)



# Create a Phrase for the primary melody
primary_phrase = Phrase()
for state in primary_states:
    note = Note(primary_midi_pitches[state], 1)
    primary_phrase.addNote(note)

# Create a Phrase for the accompanying melody
accompanying_phrase = Phrase()
for state in accompanying_states:
    note = Note(accompanying_midi_pitches[state], 1)
    accompanying_phrase.addNote(note)
    
harmony_phrase = Phrase()
for state in harmony_states:   
    pitch = harmony_midi_pitches[state]
    note = Note(harmony_midi_pitches[state], 4)
    harmony_phrase.addNote(note)
    
percussion_phrase = Phrase()
for state in percussion_states:
    pitch = percussion_midi_pitches[state]
    note = Note(pitch, 4)  # Set all notes to quarter notes (1.0)
    percussion_phrase.addNote(note)
    

# Create a Part to play both phrases
part1 = Part("An example flute part", PIANO, 1)
part2 = Part("An example flute part", PIANO, 1)
part3 = Part("An example flute part", VIOLIN, 3)
part4 = Part("An example flute part", FLUTE, 2)
percussion_part = Part("Percussion Part", 0, 9)
part1.addPhrase(primary_phrase)
part2.addPhrase(accompanying_phrase)
part3.addPhrase(harmony_phrase)
part4.addPhrase(accompanying_phrase)
score.addPart(part1)
score.addPart(part2)
score.addPart(part3)
score.addPart(part4)
percussion_part.addPhrase(percussion_phrase)
score.addPart(percussion_part)



# Play the composition
View.sketch(score)
Play.midi(score)



