import time
import sys

def type_line_timed(text, typing_duration, after_delay):
    if len(text) == 0:
        return
    typing_speed = typing_duration / len(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(after_delay)

naiilang_lyrics = [
    ("Alam ko naman", 1, 1.5),
    ("Kaibigan tayo", 2, 2),
    ("Kasalanan bang mahulog sayo???", 3, 2),
    ("Tumingin ka saakin", 3, 2),
    ("Gusto kong linawin", 1.8, 2),
    ("Naiilang kaba", 2, 1),
    ("Pag tayo lang dalawa??", 2, 1.5),
    ("Sinasabi ko nga na", 1.5, 1.5),
    ("Atin ang mundo", 1.5, 2.5),
    ("Walang ibang tulad mooooo", 3, 2)
]

print("\n")
time.sleep(1)

for line, typing_duration, after_delay in naiilang_lyrics:
    type_line_timed(line, typing_duration, after_delay)
