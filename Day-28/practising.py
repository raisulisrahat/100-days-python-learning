# Here is am showing Practising Day 23 in python

# JSON Built-In Modules
import json

filename = "example.json"

with open(filename, 'r') as file_object:
    json_str = file_object.read()
    data = json.loads(json_str)

print("My Name:", data["myName"])
print("My Last Name:", data["myLastName"])
print("Hobbies:", ", ".join(data["hobbies"]))
print("Age:", data["age"])

print("\nLanguages:")
for lang in data["languages"]:
    print(f"Name: {lang['name']}, Years of Experience: {lang['years']}")


