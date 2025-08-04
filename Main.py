import random
import math

# Define the temperature thresholds (distance in grid units)
TEMPERATURE_LEVELS = [
    (0, "already there"),
    (1, "scorching"),
    (3, "hot"),
    (4, "warm"),
    (7, "cold"),
    (8, "very cold"),
    (15, "freezing")
]

# Player and goal positions
Lifeline = 2;
player = [0, 0]
goal = [random.randint(-10, 10), random.randint(-10, 10)]

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def get_temperature(dist):
    for threshold, label in TEMPERATURE_LEVELS:
        if dist <= threshold:
            return label
    return "???"

def move_player(direction):
    if direction == 'w':
        player[1] += 1
    elif direction == 's':
        player[1] -= 1
    elif direction == 'a':
        player[0] -= 1
    elif direction == 'd':
        player[0] += 1
    else:
        print("Invalid input. Use only w/a/s/d.")

print("Find the hidden point using w/a/s/d. Type 'quit' to give up.")
while True:
    dist = distance(player, goal)
    temp = get_temperature(dist)
    print(f"You're feeling: {temp.upper()}")

    if temp == "already there":
        print("You found it! Nice.")
        break

    if temp == "freezing":
        Lifeline -=1

    if Lifeline == 1:
        print("You feel a chill in your bones");

    if Lifeline == 0:
        print("You have ventured too far");
        break

    move = input("Move (w/a/s/d): ").strip().lower()
    if move == "quit":
        print(f"You gave up. The goal was at {goal}")
        break
    move_player(move)
