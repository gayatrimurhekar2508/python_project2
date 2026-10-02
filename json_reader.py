import json

filename = input("Enter JSON file name: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n--- Formatted JSON Data ---")
    print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON file.")
