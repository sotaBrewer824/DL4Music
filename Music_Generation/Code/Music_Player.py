from pydub import AudioSegment
from pydub.playback import play
import pygame
import time
import numpy as np

# Initialize pygame mixer
pygame.mixer.init()

# Define the notes (simple tones for demo purposes)
notes = {
    'A': 440.0,
    'B': 493.88,
    'C': 523.25,
    'D': 587.33,
    'E': 659.25,
    'F': 698.46,
    'G': 783.99,
}

# Generate a sine wave tone for each note
def generate_tone(frequency, duration=500):
    sample_rate = 44100
    n_samples = int(sample_rate * duration / 1000)
    t = np.linspace(0, duration / 1000, n_samples, False)
    signal = np.sin(frequency * 2 * np.pi * t)
    audio = np.int16(signal * 32767)
    return pygame.sndarray.make_sound(audio)

# Define the song structure (Part A as an example)
song_structure = [
    ('A', 500), ('E', 500), ('A', 500), ('E', 500),
    ('A', 500), ('E', 500), ('A', 500), ('E', 500),
    ('C', 500), ('G', 500), ('E', 500), ('C', 500),
    ('G', 500), ('E', 500), ('C', 500), ('G', 500),
]

# Play the song
for note, duration in song_structure:
    tone = generate_tone(notes[note], duration)
    tone.play()
    time.sleep(duration / 1000)

pygame.quit()