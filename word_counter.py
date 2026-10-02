def count_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    words = len(text.split())
    lines = len(text.splitlines())
    characters = len(text)
    return words, lines, characters

filename = input("Enter text file name: ")
try:
    words, lines, characters = count_file(filename)
    print("Words:", words)
    print("Lines:", lines)
    print("Characters:", characters)
except FileNotFoundError:
    print("File not found.")
