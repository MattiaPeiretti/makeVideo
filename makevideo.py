import cv2
import numpy as np
import glob

import tkinter as tk
from tkinter import filedialog


class fileSelector():
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def ask_multiple_files(self):
        return filedialog.askopenfilenames(parent=self.root, title='Choose a file', filetypes=[("Bitmap image", ".bmp"), ("Tiff images", ".tif .tiff"), ("Jpeg image", ".jpg")])

    def ask_folder(self):
        return filedialog.askdirectory(parent=self.root, title='Choose a file')



class makeVideo():
    def __init__(self, path, fps, filename, specific_files=False):

        if not specific_files:
            all_images = glob.glob(path)
        else:
            all_images = path

        self.total_images = len(all_images)
        self.out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'DIVX'), int(fps), (int(width), int(height)))
    
    def start_convertion(self):
        y = 0
        for filename in glob.glob(path):
            img = cv2.imread(filename)
            out.write(img)
            y += 1
            self.progress = (y / self.total_images) * 100
        out.release()
           






