import random

data = {
    "Iron Fist": "Punching attacks do more damage to your opponent. (5 Ranks Max)",
    "Big Leagues": "Do more melee weapon damage. (5 Ranks Max)",
    "Armorer": "Craft better upgrades for your armour. (4 Ranks Max)",
    "Blacksmith": "Craft better melee weapon mods. (3 Ranks Max)",
    "Heavy Gunner": "Heavy guns do more damage. (5 Ranks Max)",
    "Strong Back": "Gain a bonus to your maximum carry weight. (5 Ranks Max)",
    "Steady Aim": "Hip-fire accuracy is improved when firing any gun. (3 Ranks Max)",
    "Basher": "Gun bashing does more damage. (4 Ranks Max)",
    "Rooted": "While standing still, you gain a bonus to damage resistance, melee and unarmed attacks. (3 Ranks Max)",
    "Pain Train": "While in power armor, sprinting into enemies hurts & staggers them. (Robots & oversized enemies are immune.) (3 Ranks Max)",
    "Pickpocket": "Makes picking pockets easier. (4 Ranks Max)",
    "Rifleman": "Attacks with non-automatic rifles does more damage. (5 Ranks Max)",
    "Awareness": "You can view a targets specific damage resistances in V.A.T.S. (2 Ranks Max)",
    "Locksmith": "Makes picking locks easier. (4 Ranks Max)",
    "Demolition Expert": "Your explosives do more damage, and you can craft explosives at any chemistry station. (4 Ranks Max)",
    "Night Person": "Gain a bonus to intelligence and perception between the hours of 6:00 p.m. and 6:00 a.m. (3 Ranks Max)",
    "Refractor": "Instantly gain a bonus to energy resistance. (5 Ranks Max)",
    "Sniper": "You can hold your breath longer whilst aiming with scopes. (3 Ranks Max)",
    "Penetrator": "In V.A.T.S. you can target an enemy's body parts that are blocked by cover, with a decrease in accuracy. (2 Ranks Max)",
    "Concentrated Fire": "In V.A.T.S. every attack on the same body part gains a bonus to accuracy. (3 Ranks Max)",
    "Toughness": "You now have extra damage resistance (5 Ranks Max)",
    "Lead Belly": "Take less radiation from eating or drinking. (3 Ranks Max)",
    "Lifegiver": "You instantly gain a bonus to your maximum health. (3 Ranks Max)",
    "Chem Resistant": "You're less likely to get addicted when consuming chems. (2 Ranks Max)",
    "Aquagirl": "You no longer take radiation damage from swimming, and can breath underwater (2 Ranks Max)",
    "Rad Resistant": "Instantly grants radiation resistance. (4 Ranks Max)",
    "Adamantium Sleleton": "Reduces limb damage (3 Ranks Max)",
    "Cannibal": "Eating human corpses restores health. (3 Ranks Max)",
    "Ghoulish": "Radiation now regenerates your lost health. (4 Ranks Max)",
    "Solar Powered": "Gain a boost to strength and endurance between the hours of 6:00 a.m. and 6:00 p.m. (3 Ranks Max)",
    "Cap Collector": "Buying and selling prices at vendors are now much better. (3 Ranks Max)",
    "Black Widow": "The opposite sex suffer more damage in combat, and are easier to persuade in dialogue. (3 Ranks Max)",
    "Lone Wanderer": "When adventuring without a companion, you take less damage and carry weight increases. (4 Ranks Max)",
    "Attack Dog": "Your faithful canine companion can hold an enemy, giving you a greater chance to hit them in V.A.T.S. (4 Ranks Max)",
    "Animal Friend": "With your gun, aim at any animal below your level and gain a chance to pacify it. (3 Ranks Max)",
    "Local Leader": "You are able to establish supply lines between your workshop settlements. (2 Ranks Max)",
    "Party Girl": "You no longer get addicted to alcohol / Effects are doubled / Luck +3 whilst drunk. (3 Ranks Max)",
    "Inspirational": "Because you lead by example, your companion does more damage in combat, and cannot hurt you. (3 Ranks Max)",
    "Wasteland Whisperer": "Aim at any wasteland creature below your level and gain a chance to pacify/incite to attack/command them (3 Ranks Max)",
    "Intimidation": "Aim at any human opponent below your level and gain a chance to pacify/incite to attack/command them. (3 Ranks Max)",
    "V.A.N.S.": "The path to your closest quest target is displayed in V.A.T.S. (2 Ranks Max)",
    "Medic": "Stimpaks now restore more lost health, and RadAway removes more radiation. (4 Ranks Max)",
    "Gun Nut": "Craft better gun mods. (4 Ranks Max)",
    "Hacker": "Makes hacking easier. (4 Ranks Max)",
    "Scrapper": "You can salvage uncommon components when scrapping weapons and armor. (3 Ranks Max)",
    "Science!": "Craft high-tech mods for weapons and armour. (4 Ranks Max)",
    "Chemist": "Any chems you take last longer. (4 Ranks Max)",
    "Robotics Expert": "Hack a robot, and gain a chance to power it on or off, or initiate a self-destruct. (3 Ranks Max)",
    "Nuclear Physicist": "Radiation weapons do more damage and fusion cores last longer. (3 Ranks Max)",
    "Nerd Rage": "When health is below 20%, time slows and you gain a bonus to damage resistance and do more damage. (3 Ranks Max)",
    "Gunslinger": "Non-automatic pistols do more damage. (5 Ranks Max)",
    "Commando": "Your automatic weapons now do more damage, and have improved hip fire accuracy. (5 Ranks Max)",
    "Sneak": "You are harder to detect while sneaking. (5 Ranks Max)",
    "Mister Sandman": "You can instantly kill a sleeping person. Your silenced weapons do additional sneak damage. (3 Ranks Max)",
    "Action Girl": "Your action points regenerate faster. (3 Ranks Max)",
    "Moving Target": "Get a bonus to damage resistance and energy resistance whilst sprinting. (3 Ranks Max)",
    "Ninja": "Ranged and melee sneak attacks get a bonus to normal damage. (3 Ranks Max)",
    "Quick Hands": "You can reload all guns faster. (3 Ranks Max)",
    "Blitz": "V.A.T.S. melee distance is increased significantly. (2 Ranks Max)",
    "Gun Fu": "Do more damage to your second V.A.T.S. target and beyond. (3 Ranks Max)",
    "Fortune Finder": "You find even more bottle caps in containers (3 Ranks Max)",
    "Scrounger": "You find even more ammunition in containers. (4 Ranks Max)",
    "Bloody Mess": "You now inflict bonus damage in combat. (4 Ranks Max)",
    "Mysterious Stranger": "Mysterious Stranger will appear occasionally in V.A.T.S. (4 Ranks Max)",
    "Idiot Savant": "Randomly receive bonus XP from any action, the lower your intelligence, the greater the chance. (3 Ranks Max)",
    "Better Criticals": "Criticals have a bonus to damage. (3 Ranks Max)",
    "Critical Banker": "Save critical hits, to be used in V.A.T.S. later. (4 Ranks Max)",
    "Grim Reaper's Sprint": "Any kill in V.A.T.S. has an increased chance to restore all action points. (2 Ranks Max)",
    "Four Leaf Clover": "Each hit in V.A.T.S. has a chance of filling your Critical meter. (5 Ranks Max)",
    "Ricochet": "Enemy's ranged attacks randomly ricochet back and kill them. The closer to death, the higher the chance. (3 Ranks Max)"
}

def select_male_perks():
    return random.sample(list(data.keys()), 7)

if __name__ == "__main__":
    chosen_perks = select_male_perks()
    for perk in chosen_perks:
        print(f"{perk}: {data[perk]}")
