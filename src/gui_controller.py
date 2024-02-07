import os
from pathlib import Path
import config as C
from tkinter import filedialog, messagebox
from tkinter import *
from json_reader import JsonReader
from utils import cropper
from threading import Thread

class Gui_controller():
    def __init__(self) -> None:
        self.json_file = ""
        self.test_images_folder = ""
        self.out_folder = ""

    def open_folder_in(self, entry):
        self.test_images_folder = filedialog.askdirectory(initialdir=".")
        entry.delete(0,END)
        entry.insert(0,self.test_images_folder)

    def open_folder_out(self, entry):
        self.out_folder = filedialog.askdirectory(initialdir=".")
        entry.delete(0,END)
        entry.insert(0,self.out_folder)

    def open_file(self, entry, extension="json"):
        self.json_file = filedialog.askopenfilename(initialdir=".", filetypes=((f"{extension} files",f"*.{extension}"),("All files","*.*")))
        entry.delete(0,END)
        entry.insert(0,self.json_file)

    def apply_crop(self, button, out_textarea, grayscale=False, resize=False, width=None, height=None):
        
        if self.json_file == "":
            messagebox.showwarning("Warning", "You need to select a JSON file") 
        elif self.test_images_folder == "":
            messagebox.showwarning("Warning", "You need to select an input images folder") 
        elif self.out_folder == "":
            messagebox.showwarning("Warning", "You need to select a output folder")
        elif resize and (width==0 and height==0):
            messagebox.showwarning("Warning", "You need to define the cliplet size")
        else:
            if width==0 or width=="":
                s=None
                h=height
                w=None
            elif height==0 or height=="":
                s=None
                h=None
                w=width
            else:
                s=(width,height)
                h=None
                w=None

            button.configure(state='disabled')

            out_textarea.configure(state='normal')
            out_textarea.delete(1.0,END)
            out_textarea.insert(1.0,"I'm Working...")
            out_textarea.configure(state='disabled')

            def run_cropping():
                j_reader = JsonReader(self.json_file, encoding=C.JSON_ENCODING)

                n_docs = len(os.listdir(self.test_images_folder))

                for ind, image_name in enumerate((os.listdir(self.test_images_folder))):
                    all_cliplets = j_reader.get_cliplets(image_name)

                    out_textarea.configure(state='normal')
                    out_textarea.insert(END,f"\n{int((ind)/n_docs*100)} %\tdoc {ind+1}/{n_docs}  -  {image_name} ... ")
                    out_textarea.yview(END)
                    out_textarea.configure(state='disabled')
                    
                    cropper(os.path.join(self.test_images_folder, image_name), 
                            all_cliplets, self.out_folder, 
                            unknown_tm=0, 
                            len_unknown_tm=C.UNKNOW_TM_LEN, 
                            len_tm=C.TM_LEN, 
                            extension="png",
                            grayscale=grayscale,
                            resize=resize,
                            size=s,
                            size_H=h, 
                            size_W=w,
                            )
                out_textarea.configure(state='normal')
                out_textarea.insert(END,"\n100%\n\nDone!")
                out_textarea.yview(END)
                out_textarea.configure(state='disabled')
                messagebox.showinfo("Cropping", "I'm done...")

                button.configure(state='normal')
                
            t1 = Thread(target=run_cropping)
            t1.start()
                
            
            