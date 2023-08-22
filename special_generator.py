import random

MAX_HISTORY = 10  # The number of past rolls to remember
roll_history = []  # Store the past rolls

def generate_special_points(total_points=28):
    stats = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
    special = {stat: 1 for stat in stats}  
    total_points -= len(stats)

    while total_points > 0:
        stat = random.choice(stats) 
        if special[stat] < 10:
            special[stat] += 1
            total_points -= 1

    return special

def is_roll_similar(roll):
    for past_roll in roll_history:
        if roll == past_roll:
            return True
    return False

def main():
    global roll_history

    special_stats = generate_special_points()
    
    while is_roll_similar(special_stats):
        special_stats = generate_special_points()

    # If our history is too long, remove the oldest item
    if len(roll_history) >= MAX_HISTORY:
        roll_history.pop(0)
    roll_history.append(special_stats)

    print("Generated SPECIAL Stats:")
    for stat, points in special_stats.items():
        print(f"{stat}: {points}")

if __name__ == "__main__":
    main()