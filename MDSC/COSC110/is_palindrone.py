import os

head = '/Users/benmurarotto/Desktop/UniNotes/University/MDSC/'

def recurse_dir(xpath: str) -> None:
        for item in os.listdir(xpath):
            full_path = os.path.join(xpath, item)
            if full_path.endswith('.py'):  # Correctly check if the file ends with .py
                print(os.path.realpath(full_path))
        for item in os.listdir(xpath):
            full_path = os.path.join(xpath, item)
            if os.path.isdir(full_path):
                recurse_dir(full_path)

recurse_dir(head)