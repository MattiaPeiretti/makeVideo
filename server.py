import eel
from makevideo import fileSelector


from tkinter import messagebox



eel.init('GUI')


file_selector = fileSelector()

path = ""

@eel.expose
def ask_folder():
    path = file_selector.ask_folder()

@eel.expose
def ask_multiple_files():
    path = file_selector.ask_multiple_files()
    
@eel.expose
def submit():
    if path == "":
        messagebox.showerror("Error", "No images have been selected!!")



eel.start('pages/loadFile.html', mode='custom', cmdline_args=['electron/node_modules/electron/dist/electron.exe', '.'])

