import tkinter as tk
from tkinter import Frame, Label
import message_protection     # Message Protection module
import trusted_senders       # Trusted Sender Score module
import emergency_actions     # Emergency Actions module
import safety_tips           # Safety Tips module (new module)

def show_dashboard():
    dash = tk.Tk()
    dash.title("Dashboard")
    dash.attributes("-fullscreen", True)
    dash.configure(bg="#E0BBE4")  # Soft purple background

    # ---------- TITLE ----------
    Label(
        dash,
        text="Dashboard",
        font=("Helvetica", 35, "bold"),
        bg="#E0BBE4",
        fg="#000000"
    ).pack(pady=40)

    # ---------- CARD CONTAINER ----------
    container = Frame(dash, bg="#E0BBE4")
    container.pack(pady=10)

    # Card dimensions
    CARD_W = 380
    CARD_H = 260

    # Card colors
    colors = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]

    # Card texts
    texts = [
        "Message\nProtection Module",
        "Trusted Sender\nScore",
        "Emergency\nActions",
        "Safety\nTips"
    ]

    # ---------- CLICK ACTIONS ----------
    def on_click(i):
        if i == 0:
            message_protection.open_module(dash)
        elif i == 1:
            trusted_senders.open_module(dash)
        elif i == 2:
            emergency_actions.open_module(dash)
        elif i == 3:
            safety_tips.open_module(dash)
        else:
            print(f"{texts[i]} page not implemented yet.")

    # ---------- CREATE TOP ROW (2 CARDS) ----------
    top_row = Frame(container, bg="#E0BBE4")
    top_row.pack(pady=20)

    for index in range(2):
        frame = Frame(
            top_row,
            width=CARD_W,
            height=CARD_H,
            bg=colors[index],
            highlightbackground="black",  # Black outline
            highlightthickness=2,         # Thickness of outline
            bd=0
        )
        frame.pack(side="left", padx=50)
        frame.pack_propagate(False)

        # Clickable
        frame.bind("<Button-1>", lambda e, i=index: on_click(i))

        label = Label(
            frame,
            text=texts[index],
            font=("Helvetica", 22, "bold"),
            bg=colors[index],
            fg="black",
            justify="center",
            wraplength=CARD_W - 20
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        label.bind("<Button-1>", lambda e, i=index: on_click(i))

    # ---------- CREATE BOTTOM ROW (2 CARDS) ----------
    bottom_row = Frame(container, bg="#E0BBE4")
    bottom_row.pack(pady=20)

    for index in range(2, 4):
        frame = Frame(
            bottom_row,
            width=CARD_W,
            height=CARD_H,
            bg=colors[index],
            highlightbackground="black",  # Black outline
            highlightthickness=2,
            bd=0
        )
        frame.pack(side="left", padx=50)
        frame.pack_propagate(False)

        # Clickable
        frame.bind("<Button-1>", lambda e, i=index: on_click(i))

        label = Label(
            frame,
            text=texts[index],
            font=("Helvetica", 22, "bold"),
            bg=colors[index],
            fg="black",
            justify="center",
            wraplength=CARD_W - 20
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        label.bind("<Button-1>", lambda e, i=index: on_click(i))

    # ESC → exit app
    dash.bind("<Escape>", lambda e: dash.destroy())

    dash.mainloop()
