import time
import random
import string
import sys

print("Введите строку или paragraph (вставьте через Ctrl+V, затем нажмите Ctrl+Z + Enter)")
input_str = sys.stdin.read().strip()

current_str = list(input_str)
# Only target non-whitespace, non-newline characters for replacement
positions = [i for i in range(len(current_str)) if current_str[i] not in (' ', '\n')]
random.shuffle(positions)

for pos in positions:
    last_char = current_str[pos]  # init with original
    for _ in range(5):  # flicker effect
        flicker_char = random.choice(string.printable.strip())
        current_str[pos] = flicker_char
        print('\033[2J\033[H', end='')  # clear screen and move cursor to top-left
        print(''.join(current_str), end='', flush=True)
        time.sleep(0.0005)
        last_char = flicker_char  # update to last flicker
    current_str[pos] = last_char  # leave as last random char instead of '0'
    print('\033[2J\033[H', end='')  # clear screen and move cursor to top-left
    print(''.join(current_str), end='', flush=True)
    time.sleep(0.01)

print("\nDone!")
