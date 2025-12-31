import sys

def move_cursor(row, col):
    # \033[ is the Escape sequence
    sys.stdout.write(f"\033[{row};{col}H")
    sys.stdout.flush()

print("Hello!")
move_cursor(5, 10)
print("I moved here! ^w^")
