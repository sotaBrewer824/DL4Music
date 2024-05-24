import os

import mido
import pygame

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
def play_midi(file):
   freq = 44100
   bitsize = -16
   channels = 2
   buffer = 1024
   pygame.mixer.init(freq, bitsize, channels, buffer)
   pygame.mixer.music.set_volume(1)
   clock = pygame.time.Clock()
   try:
       pygame.mixer.music.load(file)
   except:
       import traceback
       print(traceback.format_exc())
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
       clock.tick(30)


# bpm = \frac{60000000}{tempo}
'''
def music(note, base_num, base_time):
    # mid = mido.MidiFile()
    # track = mido.MidiTrack()
    # mid.tracks.append(track)
    # meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(mido.Message('note_on', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=96, time=0,
                              channel=1))
    track.append(mido.Message('note_off', note=base_note + base_num * 12 + sum(major_notes[0:note]), velocity=96,
                              time=int(480 * base_time), channel=1))
    # print('正在合成(',note, base_num, base_time,')音')
    # track.append(mido.Message('note_on', note=base_note, velocity=96, time=0))
    # track.append(mido.Message('note_off', note=base_note, velocity=96, time=480*base_time))
    # mid.save('1.mid')
    # play_midi('1.mid')

major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
base_note = 60

def music(note, octave, duration):
    track.append(mido.Message('note_on', note=base_note + note + (octave * 12), velocity=100, time=0))
    track.append(mido.Message('note_off', note=base_note + note + (octave * 12), velocity=100, time=int(480 * duration)))

def mozart_music():
    # Intro
    music(5, 1, 0.5)
    music(6, 1, 0.5)
    music(0, 2, 1)
    music(7, 1, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 0.5)
    music(7, 1, 0.5)
    music(5, 1, 0.5)
    music(3, 2, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)

    music(0, 2, 1)
    music(7, 1, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 0.5)
    music(7, 1, 0.5)
    music(5, 1, 0.5)
    music(3, 2, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(7, 1, 0.5)
    music(6, 1, 0.5)
    music(5, 1, 1)

    music(5, 1, 0.5)
    music(6, 1, 0.5)
    music(0, 2, 1)
    music(7, 1, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 0.5)
    music(7, 1, 0.5)
    music(5, 1, 0.5)
    music(3, 2, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)

    music(0, 2, 1)
    music(7, 1, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 0.5)
    music(7, 1, 0.5)
    music(5, 1, 0.5)
    music(3, 2, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(7, 1, 0.5)
    music(6, 1, 0.5)
    music(5, 1, 1)

    # Variation 1
    for i in range(4):
        for note in major_notes:
            music(note, 2, 0.25)
        music(7, 1, 0.5)
        music(6, 1, 0.5)
        music(5, 1, 1)

    # Variation 2
    for i in range(4):
        for note in major_notes:
            music(note, 2, 0.25)
        music(5, 1, 0.5)
        music(6, 1, 0.5)
        music(7, 1, 1)

    # Outro
    music(5, 1, 0.5)
    music(6, 1, 0.5)
    music(0, 2, 1)
    music(7, 1, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 0.5)
    music(7, 1, 0.5)
    music(5, 1, 0.5)
    music(3, 2, 0.5)
    music(2, 2, 0.5)
    music(1, 2, 0.5)
    music(0, 2, 1)

mozart_music()


mid.save('mozart_part3_Gemini.mid')
play_midi('mozart_part3_Gemini.mid')
print('Enjoy the song')
'''
from mido import MidiFile, MidiTrack

# Set base note and major scale intervals
base_note = 60
major_notes = [0, 2, 2, 1, 2, 2, 2, 1]

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

base_note = 60

def music(note, octave, duration):
    track.append(mido.Message('note_on', note=base_note + note + (octave * 12), velocity=100, time=0))
    track.append(mido.Message('note_off', note=base_note + note + (octave * 12), velocity=100, time=int(480 * duration)))

def turkish_march():
    # Part A
    music(9, 0, 2)  # A
    music(4, 0, 2)  # E
    music(9, 0, 2)  # A
    music(4, 0, 2)  # E
    music(9, 0, 2)  # A
    music(4, 0, 2)  # E
    music(9, 0, 2)  # A
    music(4, 0, 2)  # E
    music(0, 1, 2)  # C
    music(7, 0, 2)  # G
    music(4, 0, 2)  # E
    music(0, 1, 2)  # C
    music(7, 0, 2)  # G
    music(4, 0, 2)  # E
    music(0, 1, 2)  # C
    music(7, 0, 2)  # G

# Call the function to create the Turkish March
turkish_march()

# Save the MIDI file
mid.save('turkish_march_gpt.mid')

print("MIDI file has been saved as 'turkish_march_gpt.mid'")
