import time
import random
import string

input_str = input("Enter string: ")
current_str = list(input_str)
positions = list(range(len(current_str)))
random.shuffle(positions)

for pos in positions:
    last_char = current_str[pos]  # init with original
    for _ in range(5):  # flicker effect
        flicker_char = random.choice(string.printable.strip())
        current_str[pos] = flicker_char
        print(f"\r{''.join(current_str)}", end='', flush=True)
        time.sleep(0.05)
        last_char = flicker_char  # update to last flicker
    current_str[pos] = last_char  # leave as last random char instead of '0'
    print(f"\r{''.join(current_str)}", end='', flush=True)
    time.sleep(0.01)

print("\nDone!")
