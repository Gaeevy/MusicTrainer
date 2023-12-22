import random
from mingus.core.notes import int_to_note
from time import sleep
from mingus.core.progressions import to_chords

# prog = to_chords(["I", "IV", "V"], "C")
# print(prog)

progressions = [
    ("major", ["I", "III", "VI", "IV"]),
    ("major", ["I", "III", "vi", "IV"]),
    ("major", ["I", "I", "vi", "IV"]),
    ("major", ["I", "II", "vi", "IV"]),
    ("major", ["I", "IV", "vi", "IV"]),
    ("major", ["IV", "I", "V", "vi"]),
    ("major", ["V", "vi", "IV", "I"]),
    ("major", ["I", "vi", "IV", "V"]),
    ("major", ["I", "IV", "V", "I"]),
    ("major", ["VI", "VII", "I", "I"]),
    ("major", ["I", "VI", "II", "V"]),
]


def return_note_and_string() -> tuple[str, int]:
    random_note_int = random.randint(0, 11)
    accidental = ("#", "b")[random.randint(0, 1)]
    note = int_to_note(random_note_int, accidentals=accidental)
    string = random.randint(1, 6)
    return note, string


def return_key_and_progression() -> str:
    random_note_int = random.randint(0, 11)
    accidental = ("#", "b")[random.randint(0, 1)]
    key = int_to_note(random_note_int, accidentals=accidental)
    random_prog_int = random.randint(0, len(progressions) - 1)
    color, progression = progressions[random_prog_int]
    return key + f" {color}: " + str(progression)
