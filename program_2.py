#Programmer: Timothy Pickering
#Date: 3/26/2025
#Title: Funny address program

#Required module
import tkinter as tk
from tkinter import messagebox

#Function to display name and address in a popup
def show_info():
    info_text = "Name: Tim Pickering\nAddress: 300 W Main St Anoka, MN 55303"
    messagebox.showinfo("Info", info_text)

#Quit function to confirm exit with a fun message
def confirm_quit():
    confirm = tk.Toplevel(root)
    confirm.title("Confirmation")
    confirm.geometry("250x100")

    tk.Label(confirm, text="Are you sure?").pack(pady=5)
    tk.Button(confirm, text="Send me to the void", command=root.quit).pack()

#Create the main application window
def main():
    global root
    root = tk.Tk()
    root.title("Info Display")
    root.geometry("300x150")

    #Create the show info button
    tk.Button(root, text="Show Info", command=show_info).pack(pady=10)
    tk.Button(root, text="Quit", command=confirm_quit).pack(pady=10)

    #Start the tkinter event loop
    root.mainloop()

#Run the program
if __name__ == "__main__":
    main()