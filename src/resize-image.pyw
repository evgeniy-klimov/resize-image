from PIL import Image, UnidentifiedImageError
import tkinter as tk
from tkinter import filedialog, messagebox
import os, sys, getopt

def make_resized_path(path):
    return os.path.dirname(path) + "/resized_" + os.path.basename(path)

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "D:", ['debug='])
        for opt, arg in opts:
            if opt in ['-D', '--debug']:
                if arg == '1': # UnidentifiedImageError
                    file_paths = ('resize.spec',)
                elif arg == '2': # FileNotFoundError
                    file_paths = ('does_not_exist.jpg',)
        if 'file_paths' not in locals():
            file_paths = filedialog.askopenfilenames()

        root = tk.Tk()
        root.withdraw()
        for file_path in file_paths:
            img = Image.open(file_path)
            img = img.resize((400, 400))
            #Saved in the same relative location
            resized_path = make_resized_path(file_path)
            img.save(resized_path)
    except UnidentifiedImageError as e:
        messagebox.showerror(title="UnidentifiedImageError", message=e)
        sys.exit(2)
    except FileNotFoundError as e:
        messagebox.showerror(title="FileNotFoundError", message=e)
        sys.exit(2)
    except getopt.GetoptError:
        print(f"usage: {argv[0]} [-D 1|2]")
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv)