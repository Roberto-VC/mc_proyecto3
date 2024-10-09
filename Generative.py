from music import *
from random import *

##### musical parameters
comeAlive = 0.35
measures = 4 

##### define the data structure
score = Score("Joyful Beats", 125.0)  # tempo is 125 bpm
drumsPart = Part("Drums", 0, 9)  # using MIDI channel 9 (percussion)
melodyPart = Part("Melody", 0, 0)  # using MIDI channel 0 (melody)
harmonyPart = Part("Harmony", 0, 1)  # using MIDI channel 1 (harmony)

##### create drum phrases
# Kick (bass drum)
bassDrumPhrase = Phrase(0.0)
for i in range(8 * measures):
    dynamics = randint(80, 110)  # Variation in dynamics
    x = randint(0, 1)
    if x == 1:
        n = Note(ACOUSTIC_BASS_DRUM, HN, dynamics)
    else:
        n = Note(REST, HN, dynamics)
    bassDrumPhrase.addNote(n)

# Percussion (cencerro, tom-tom, etc.)
percPhrase = Phrase(0.0)
for i in range(8 * measures):
    r = Note(REST, QN)
    percPhrase.addNote(r)
    
    # Randomly select among instruments
    pitch = choice([ABD, CCM, HMT, RC1])
    dynamics = randint(80, 110)
    n = Note(pitch, QN, dynamics)
    percPhrase.addNote(n)

# Hi-hats
hiHatPhrase = Phrase(0.0)
for i in range(4 * measures):
    oddHit = i % 4 
    doItNow = random() < comeAlive
    
    if oddHit == 1 and doItNow:
        pitch = OHH
    elif oddHit == 0 and doItNow:
        pitch = ABD
    
    dynamics = randint(80, 110)
    n = Note(pitch, HN, dynamics)
    hiHatPhrase.addNote(n)
    
    r = Note(REST, HN)
    hiHatPhrase.addNote(r)


# Whistle
whistlePhrase = Phrase(0.0)
for i in range(2 * measures):
    oddHit = i % 2 == 1
    doItNow = random() < comeAlive
    
    if oddHit and doItNow:
        pitch = MTR
    else:
        pitch = OTR
    
    dynamics = randint(80, 110)
    n = Note(pitch, DHN, dynamics)
    whistlePhrase.addNote(n)
    
    r = Note(REST, QN)
    whistlePhrase.addNote(r)

##### create melody phrases
melodyPhrase = Phrase(0.0)
# Define a C major scale (C, D, E, F, G, A, B)
c_major_scale = [C4, D4, E4, F4, G4, A4, B4, C5]

    
##### create harmony phrases
harmonyPhrase = Phrase(0.0)
# Define chord structure based on the melody
chord_progression = [
    [C4, E4, G4],  # C major
    [F4, A4, C5],  # F major
    [G4, B4, D5],  # G major
    [C4, E4, G4],  # C major
]

for i in range(16 * measures):  
    chord = chord_progression[i % len(chord_progression)]  # Get current chord
    melody_note = choice(chord)  # Choose a note from the current chord
    dynamics = randint(90, 110)
    oddHit = i % 2 == 1
    doItNow = random() < comeAlive
    
    if oddHit and doItNow:
      n = Note(melody_note, QN, dynamics)
    else:
      n = Note(REST, QN, dynamics)
    melodyPhrase.addNote(n)

# Optional: Add rhythmic variation
for i in range(len(melodyPhrase.getNoteList())):
    if i % 4 == 0:  # Change the rhythm for every fourth note
        melodyPhrase.getNote(i).duration = EN * 4  # Hold for longer

# Loop through melody notes to add harmony
for i, note in enumerate(melodyPhrase.getNoteList()):
    chord = chord_progression[i % len(chord_progression)]
    harmony_note = choice(chord)  # Choose a note from the current chord
    dynamics = randint(80, 100)
    oddHit = i % 2 == 1
    doItNow = random() < comeAlive
    if oddHit and doItNow:
      n = Note(harmony_note, HN, dynamics)
    else:
      n = Note(harmony_note, QN, dynamics)
    harmonyPhrase.addNote(n)



# Apply modifications
Mod.elongate(bassDrumPhrase, 1)
Mod.retrograde(percPhrase)
Mod.transpose(hiHatPhrase, 2)
Mod.palindrome(whistlePhrase)
Mod.randomize(whistlePhrase, 2)
Mod.transpose(harmonyPhrase, 3) 

##### combine musical material
drumsPart.addPhrase(bassDrumPhrase)
drumsPart.addPhrase(percPhrase)
drumsPart.addPhrase(hiHatPhrase)
drumsPart.addPhrase(whistlePhrase)
melodyPart.addPhrase(melodyPhrase)
harmonyPart.addPhrase(harmonyPhrase)
score.addPart(drumsPart)
score.addPart(melodyPart)
score.addPart(harmonyPart)


##### view and play
View.sketch(score)
Play.midi(score)




