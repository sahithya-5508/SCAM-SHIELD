import tkinter as tk
from PIL import Image, ImageTk, ImageDraw  # noqa

import dashboard   # ← IMPORTANT

def make_perfect_circle(path, out_size=300):
    img = Image.open(path).convert("RGBA")
    img = img.resize((out_size, out_size), Image.LANCZOS)

    mask = Image.new("L", (out_size, out_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, out_size, out_size), fill=255)

    circle_img = Image.new("RGBA", (out_size, out_size))
    circle_img.paste(img, (0, 0), mask)

    return circle_img


def go_to_dashboard(splash):
    splash.destroy()
    dashboard.show_dashboard()   # ← OPEN DASHBOARD.PY


def show_splash():
    splash = tk.Tk()
    splash.attributes("-fullscreen", True)

    splash.configure(bg="#E0BBE4")  # soft background

    frame = tk.Frame(splash, bg="#E0BBE4")
    frame.pack(expand=True)

    try:
        circ = make_perfect_circle("logo.png", 300)
        logo = ImageTk.PhotoImage(circ)
        lbl = tk.Label(frame, image=logo, bg="#E0BBE4", borderwidth=0)
        lbl.image = logo
        lbl.pack()
    except:
        tk.Label(frame, text="[LOGO]", font=("Arial", 35), bg="#E0BBE4").pack()

    splash.after(3000, lambda: go_to_dashboard(splash))
    splash.mainloop()


show_splash()
