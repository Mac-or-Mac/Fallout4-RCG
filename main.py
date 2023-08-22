import random
import re
import subprocess

def read_data_from_file(filename):
    with open(filename, "r") as file:
        data = file.read().strip()
    return data

def extract_value(data_string, data_type="list"):
    match = re.search(r'data = (\{.*\}|\[.*\])', data_string)
    if match:
        values_str = match.group(1)
        if data_type == "list":
            values = values_str.replace('"', '').strip('[]').split(", ")
        elif data_type == "dict":
            values = [value.strip('"') for key, value in eval(values_str).items()]
        return values
    return []

def run_external_script(script_name):
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout.strip()

def generate_perks(sex):
    if sex == "Male":
        perks_output = run_external_script("male_perks.py")
    else:
        perks_output = run_external_script("female_perks.py")
    return perks_output

def main():
    categories = {
        "Sex": "sex_data.py",
        "Follower": "follower_data.py",
        "Commonwealth Faction": "commonwealth_faction_data.py",
        "Commonwealth Settlement": "commonwealth_settlement_data.py",
        "Far Harbor Faction": "far_harbor_faction_data.py",
        "Far Harbor Settlement": "far_harbor_settlement_data.py",
        "Name": "names_data.py",
        "Nuka World Faction": "nuka_world_faction_data.py",
        "Romance": "romance_data.py"
    }

    selections = {}

    for category, filename in categories.items():
        data = read_data_from_file(filename)
        values = extract_value(data)
        selections[category] = random.choice(values) if values else "Unknown"

    display_order = [
        "Name",
        "Sex",
        "Follower",
        "Romance",
        "Commonwealth Faction",
        "Commonwealth Settlement",
        "Far Harbor Faction",
        "Far Harbor Settlement",
        "Nuka World Faction"
    ]

    for category in display_order:
        print(f"{category}: {selections.get(category, 'Unknown')}")

    # Get and print the selected perks based on the chosen sex
    selected_sex = selections["Sex"]
    chosen_perks = generate_perks(selected_sex)
    print("\nSelected Perks:")
    print(chosen_perks)

    # Run special_generator.py and capture its output
    special_output = run_external_script("special_generator.py")
    print(f"\n{special_output}")

if __name__ == "__main__":
    main()
