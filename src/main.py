import os
import json
import time
import sys
from math import sin, pi

import simpleaudio as sa


def english_to_morse_code(text):
    morse_code = ""
    with open(os.path.join(os.path.dirname(__file__), 'morse.json'), 'r') as f:
        MORSE_CODE_DICT = json.load(f)
    
    for char in text:
        char = char.upper()
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += char

    return morse_code.strip()


def play_tone(frequency, duration):
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    tone = []

    for i in range(num_samples):
        t = i / float(sample_rate)
        tone.append(0.5 * sin(frequency * t * 2 * pi))

    audio = bytearray()
    for sample in tone:
        audio.extend(int(sample * 32767).to_bytes(2, 'little', signed=True))

    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def play_morse_code(morse_code, unit_duration=100):
    for symbol in morse_code:
        if symbol == '.':
            duration = unit_duration
        elif symbol == '-':
            duration = unit_duration * 3
        elif symbol == ' ':
            time.sleep(unit_duration * 2 / 1000)
            continue
        else:
            continue

        play_tone(1000, duration / 1000)
        time.sleep(unit_duration / 1000)
                       
                       
                       
def main():
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        morse_code = english_to_morse_code(input_text)
        print(morse_code)
        play_morse_code(morse_code)
    else:
        print("Usage: python morse_code_translator.py <text to translate>")



if __name__ == "__main__":
    main()
