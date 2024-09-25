import os

try:
    path = os.path.join("resources", "just_created.txt")
    os.remove(path)

except FileNotFoundError:
    print("File is already deleted!")
