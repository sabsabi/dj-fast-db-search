import os
from people import people_data

def remove_duplicates(people_data):
    unique_data = []
    seen = set()

    for person, description in people_data:
        if person not in seen:
            unique_data.append((person, description))
            seen.add(person)

    return unique_data

unique_people_data = remove_duplicates(people_data)

# Check if people_unique.py exists and delete it
if os.path.exists("people_unique.py"):
    os.remove("people_unique.py")

# Write the unique data to people_unique.py
with open("people_unique.py", "w") as file:
    file.write("people_data = [\n")
    for person, description in unique_people_data:
        file.write(f"    (\"{person}\", \"{description}\"),\n")
    file.write("]\n")

print("Unique data has been written to people_unique.py")