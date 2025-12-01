from pathlib import Path

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / 'puzzle-1-input.txt'

Start = 50
current = Start
Count_number = 0
Counter = 0

# Open the file in read mode
with open(TEXT_FILE, 'r') as file:
    lines = file.read().splitlines()

    for line in lines:
        direction = line[0]
        num = int(line[1:])

        # L = Subtract, R = Add
        move = -num if direction == 'L' else num

        # Wrap around
        current = (current + move) % 100

        if current == Count_number:
            Counter = Counter + 1


print(Counter)