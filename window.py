from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("Meme Generator")
window.geometry("400x600")
window.configure(bg = "#81d1e2")
canvas = Canvas(
    window,
    bg = "#81d1e2",
    height = 600,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    200.0, 312.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 130, y = 89,
    width = 140,
    height = 41)

window.resizable(False, False)
window.mainloop()
