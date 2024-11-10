# Import required modules from tkinter library
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# Initialize the main application window
root = Tk()
root.iconbitmap("Notepad.ico")  # Set icon for the window

# Create a text area widget where the user can write or edit text
TextArea = Text(root, font="lucida 10")
TextArea.pack(fill=BOTH, expand=True)

# Function to create a new file
def newFile():
    """Clears the current text area to start a new file."""
    global file
    root.title("Untitled - Propad")  # Set default window title for new file
    file = None  # Reset file variable
    TextArea.delete(1.0, END)  # Clear the text area

# Function to open an existing file
def openFile():
    """Opens a file and loads its content into the text area."""
    global file
    # Open file dialog to select a file
    file = askopenfilename(filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")], defaultextension=".txt")
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Propad")  # Update window title with file name
        TextArea.delete(1.0, END)  # Clear the text area
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())  # Insert file content into text area

# Function to save the current file
def saveFile():
    """Saves the current text area content to a file."""
    global file
    if file is None:  # If no file has been opened, prompt the user to save as a new file
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            with open(file, "w") as f:
                f.write(TextArea.get(1.0, END))  # Write text area content to the file
            root.title(os.path.basename(file) + " - Propad")  # Update window title with file name
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))  # Save current content to existing file

# Function to exit the application
def quitApp():
    """Closes the application."""
    root.destroy()

# Text editing functions for Cut, Copy, and Paste
def cut():
    """Cuts the selected text in the text area."""
    TextArea.event_generate("<<Cut>>")

def copy():
    """Copies the selected text in the text area."""
    TextArea.event_generate("<<Copy>>")

def paste():
    """Pastes the copied text into the text area."""
    TextArea.event_generate("<<Paste>>")

# Function to display 'About' information
def about():
    """Shows information about the application."""
    showinfo("Propad", "This notepad is created by Shivam Pathak")

# Set initial properties of the main window
root.title("Untitled - Propad")
root.geometry("1000x599")  # Set default window size
file = None  # Variable to store file path

# Create menu bar
Menubar = Menu(root)

# Add File menu
fileMenu = Menu(Menubar, tearoff=0)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=quitApp)
Menubar.add_cascade(label="File", menu=fileMenu)

# Add Edit menu
EditMenu = Menu(Menubar, tearoff=0)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
Menubar.add_cascade(label="Edit", menu=EditMenu)

# Add Help menu
HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="About - Propad", command=about)
Menubar.add_cascade(label="Help", menu=HelpMenu)

# Configure main window to use the menu bar
root.config(menu=Menubar)

# Add scrollbar to the text area
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)  # Pack scrollbar on the right side
Scroll.config(command=TextArea.yview)  # Link scrollbar to text area view
TextArea.config(yscrollcommand=Scroll.set)  # Link text area to scrollbar

# Run the application
root.mainloop()
