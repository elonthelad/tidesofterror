import os
import math
import tkinter as tk
from tkinter import filedialog

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r+') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    if 'manpower=' in line:
                        try:
                            manpower = int(line.split('manpower=')[1].strip())
                            multiplied_manpower = manpower * 3
                            new_line = f"\tmanpower={multiplied_manpower}\n"
                            lines[i] = new_line
                            file.seek(0)
                            file.writelines(lines)
                        except ValueError:
                            print(f"Error: Invalid 'manpower=' value in file '{filename}'")
                        break
                else:
                    print(f"Warning: 'manpower=' not found in file '{filename}'")

def select_folder():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_path = filedialog.askdirectory()
    if folder_path:
        process_files_in_folder(folder_path)
    else:
        print("No folder selected.")

if __name__ == "__main__":
    select_folder()
