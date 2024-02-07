
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, IntVar

from gui_controller import Gui_controller

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

main_w = 1100
main_h = 650
gui_controller = Gui_controller()

ASSETS_PATH = resource_path("assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry(f"{main_w}x{main_h}")
window.title("Cliplets Cropper")
window.iconbitmap(resource_path("assets\icon.ico"))
window.configure(bg = "#F9FBFF")


canvas = Canvas(
    window,
    bg = "#F9FBFF",
    height = 650,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

entry_image_logo = PhotoImage(
    file=relative_to_assets("logo.png"))
entry_bg_1 = canvas.create_image(
    120,
    50,
    image=entry_image_logo
)


#GRAYSCALE Combobox
grayscale = IntVar()
canvas.create_text(
    115.0,
    355.0,
    anchor="nw",
    text="Gray Scale",
    fill="#000000",
    font=("Inter", 24 * -1)
)
ceck_grayscale = Checkbutton(window, variable=grayscale, onvalue=1, offvalue=0)
ceck_grayscale.place(
    x=80.0,
    y=350.0,
    width=30.0,
    height=30.0
)

#RESIZE COMBOBOX
resize = IntVar()
canvas.create_text(
    115.0,
    405.0,
    anchor="nw",
    text="Resize",
    fill="#000000",
    font=("Inter", 24 * -1)
)
ceck_resize = Checkbutton(window, variable=resize, onvalue=1, offvalue=0)
ceck_resize.place(
    x=80.0,
    y=400.0,
    width=30.0,
    height=30.0
)

# width
width = IntVar()
entry_width = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=width,
)
entry_width.place(
    x=212.0,
    y=450.0,
    width=119.0,
    height=35.0
)
canvas.create_text(
    140.0,
    455.0,
    anchor="nw",
    text="Width",
    fill="#000000",
    font=("Inter", 24 * -1)
)

# height
height = IntVar()
entry_height = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=height
)
entry_height.place(
    x=212.0,
    y=500.0,
    width=119.0,
    height=35.0
)
canvas.create_text(
    132.0,
    505.0,
    anchor="nw",
    text="Height",
    fill="#000000",
    font=("Inter", 24 * -1)
)


# out folder text ---------------------------------
canvas.create_text(
    85.0,
    240.0,
    anchor="nw",
    text="Select Output Folder:",
    fill="#000000",
    font=("Inter", 24 * -1)
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
)
entry_3.place(
    x=320.0,
    y=237.0,
    width=587.0,
    height=37.0
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_open.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_controller.open_folder_out(entry_3),
    relief="flat"
)
button_2.place(
    x=907.0,
    y=237.0,
    width=110.0,
    height=37.0
)


# IMAGE FOLDER IN
canvas.create_text(
    93.0,
    188.0,
    anchor="nw",
    text="Select Image Folder:",
    fill="#000000",
    font=("Inter", 24 * -1)
)
# entry_image_4 = PhotoImage(
#     file=relative_to_assets("entry_4.png"))
# entry_bg_4 = canvas.create_image(
#     613.5,
#     202.5,
#     image=entry_image_4
# )
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=320.0,
    y=184.0,
    width=587.0,
    height=37.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_open.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_controller.open_folder_in(entry_4),
    relief="flat"
)
button_3.place(
    x=907.0,
    y=184.0,
    width=110.0,
    height=37.0
)


# JSON FILE SELECTOR
canvas.create_text(
    137.0,
    135.0,
    anchor="nw",
    text="Select Json File:",
    fill="#000000",
    font=("Inter", 24 * -1)
)
# entry_image_5 = PhotoImage(
#     file=relative_to_assets("entry_5.png"))
# entry_bg_5 = canvas.create_image(
#     613.5,
#     149.5,
#     image=entry_image_5
# )
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=320.0,
    y=131.0,
    width=587.0,
    height=37.0
)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_open.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_controller.open_file(entry_5, extension="json"),
    relief="flat"
)
button_4.place(
    x=907.0,
    y=131.0,
    width=109.0,
    height=37.0
)


#apply button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_export.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_controller.apply_crop(button_1, text_area_results, grayscale=grayscale.get(), resize=resize.get(), width=width.get(), height=height.get()),
    relief="flat"
)
button_1.place(
    x=744.0,
    y=528.0,
    width=238.0,
    height=37.0
)


# OUT TEXT FIELD
text_area_results = Text(
    window, 
    height=8,
    background="#d0d0d0",
    state="disabled"
    )
text_area_results.place(
    x=0.0,
    y=580.0,
    width=main_w,
    height=70.0
)

window.resizable(False, False)
window.minsize(width=main_w, height=main_h)
window.maxsize(width=main_w, height=main_h)
window.mainloop()