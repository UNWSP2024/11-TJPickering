#Programmer: Timothy Pickering
#Date: 3/26/2025
#Title: Favorite Phrase Program

#Required module
import tkinter as tk

def create_gui():
    #Create the main window
    root = tk.Tk()
    root.title("Bible Verse Display")
    #Set window size
    root.geometry("500x200")

    #Create a label with the phrase
    verse_text = ("Do not worry about how you will defend yourselves "
                  "or what you will say, for the Holy Spirit will teach you.")
    label = tk.Label(root, text=verse_text, wraplength=400, font=("Arial", 12), padx=10, pady=10, justify="center")

    #Place the label in the window
    label.pack(expand=True)

    #Run the tkinter event loop
    root.mainloop()

#Run the GUI application
create_gui()