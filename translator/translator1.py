# # # from tkinter import *

# # # def play_audio():
# # #     # Your audio playback code goes here
# # #     print("Playing audio...")

# # # root = Tk()
# # # root.title("Audio Button Example")

# # # # Load the audio icon image
# # # audio_icon = PhotoImage(Image.open("C:\PCL\Aditi College\SE\PBL\Audio.jpg"))  # Change this to the path of your audio icon image

# # # # Create the button with the audio icon
# # # audio_btn = Button(root, image=audio_icon, text="Play Audio", compound=LEFT, command=play_audio, font="arial 12 bold", pady=5, bg="orange", activebackground="green")
# # # audio_btn.pack(pady=20)

# # # root.mainloop()

# # from tkinter import *
# # from PIL import Image, ImageTk

# # root = Tk()
# # root.title("Image Insertion")

# # # Load the image using Pillow
# # image_path = "C:\PCL\Aditi College\SE\PBL\Audio.jpg"  # Change this to the path of your image file
# # img = Image.open(image_path)
# # img=img.resize((100,100))
# # img = ImageTk.PhotoImage(img)

# # # Create a label to display the image
# # image_label = Label(root, image=img)
# # image_label.pack()

# # root.mainloop()

# from langcodes import Language

# def language_name_to_code(language_name):
#     # Attempt to parse the language name
#         lang = Language.get(language_name)
#         # Get the language code
#         lang_code = lang.language
#         return lang_code
    
# # Example usage:
# input_language = input("Enter the language name: ")
# language_code = language_name_to_code(input_language)

# if language_code:
#     print(f"The language code for '{input_language}' is '{language_code}'")

import tkinter as tk
import tkinter.simpledialog as simpledialog

def maximize_window(event):
    root.state('normal')  # Restore window to normal (maximize)

def minimize_window(window_title):
    # Find the window with the specified title and minimize it
    for window in tk._default_root.children.values():
        if isinstance(window, tk.Toplevel) and window.wm_title() == window_title:
            window.iconify()
            return
    print(f"Window with title '{window_title}' not found.")

root = tk.Tk()
root.title("Minimize and Maximize Example")

# Get the window title from the user
window_title = simpledialog.askstring("Window Title", "Enter the title of the window to minimize:")

# Minimize the specified window
minimize_window(window_title)

# Create a label with instructions
label = tk.Label(root, text="Click anywhere on the window to maximize it.")
label.pack(pady=20)

# Bind left mouse button click to maximize_window function
root.bind("<Button-1>", maximize_window)

root.mainloop()
