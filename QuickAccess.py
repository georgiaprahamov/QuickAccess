import keyboard
import subprocess
import tkinter as tk
from tkinter import messagebox

def open_calculator():
    try:
        subprocess.Popen('calc.exe')
    except FileNotFoundError:
        messagebox.showerror("Error", "Calculator not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    root.withdraw()

    try:
        keyboard.add_hotkey('f12', open_calculator)
        messagebox.showinfo("Info", "Press F12 to open Calculator. Press 'q' to quit.")
        while True:
            if keyboard.is_pressed('q'):
                messagebox.showinfo("Info", "Exiting...")
                break
    except KeyboardInterrupt:
        messagebox.showinfo("Info", "Exiting...")

if __name__ == "__main__":
    main()
