import tkinter as tk
from tkinter import Frame, Label, Button

# ----------------------------
# In-memory storage
# ----------------------------
GUARDIAN_CONTACT = "mom"
REPORTS = []

# ----------------------------
# Functions
# ----------------------------
def select_guardian(guardian_var):
    global GUARDIAN_CONTACT
    GUARDIAN_CONTACT = guardian_var.get().lower()
    status_label.config(text=f"Guardian set to: {GUARDIAN_CONTACT.capitalize()}", fg="black")

def manual_sos():
    sos_box.config(bg="#FF4C4C")
    status_label.config(
        text=f"SOS sent to {GUARDIAN_CONTACT}!",
        fg="black"
    )

def report_scam():
    REPORTS.append("User reported a scam/fraud")
    report_box.config(bg="#FFA500")
    status_label.config(
        text=f"Scam reported to {GUARDIAN_CONTACT}",
        fg="black"
    )

# ----------------------------
# Open Emergency Actions Module
# ----------------------------
def open_module(parent):
    global status_label, sos_box, report_box

    window = tk.Toplevel(parent)
    window.title("Emergency Actions")
    window.attributes("-fullscreen", True)
    window.configure(bg="#E0BBE4")  # Background color

    # ---------- TITLE ----------
    Label(
        window,
        text="Emergency Actions",
        font=("Helvetica", 36, "bold"),
        bg="#E0BBE4",
        fg="black"
    ).pack(pady=30)

    # ---------- BACK BUTTON ----------
    back_btn = Button(
        window,
        text="Back",
        font=("Helvetica", 14, "bold"),
        bg="#DDDDDD",
        command=window.destroy
    )
    back_btn.place(relx=0.95, rely=0.02, anchor="ne")

    # ---------- STATUS LABEL ----------
    status_label = Label(
        window,
        text="Select an action below",
        font=("Helvetica", 18),
        bg="#E0BBE4",
        fg="black",
        justify="center",
        wraplength=1000
    )
    status_label.pack(pady=10)

    # ---------- CARD CONTAINER ----------
    container = Frame(window, bg="#E0BBE4")
    container.pack(pady=50)

    CARD_W, CARD_H = 350, 400
    PADDING_X = 30

    # ---------- CARD DEFINITIONS ----------
    cards = [
        {"title": "Select Guardian", "bg": "#FFFFFF", "fg": "black", "action": "guardian"},
        {"title": "Emergency SOS", "bg": "#FF4C4C", "fg": "black", "action": "sos"},
        {"title": "Report Scam / Fraud", "bg": "#FFA500", "fg": "black", "action": "report"}
    ]

    guardian_var = tk.StringVar(value=GUARDIAN_CONTACT)

    for idx, card in enumerate(cards):
        frame = Frame(container, width=CARD_W, height=CARD_H, bg=card["bg"], bd=0, relief="raised")
        frame.grid(row=0, column=idx, padx=PADDING_X)
        frame.pack_propagate(False)

        # Card title label
        lbl = Label(
            frame,
            text=card["title"],
            font=("Helvetica", 22, "bold"),
            bg=card["bg"],
            fg=card["fg"],
            wraplength=CARD_W - 20,
            justify="center"
        )
        lbl.pack(expand=True, pady=10)

        # Hover effect
        def on_enter(e, f=frame):
            f.config(bd=4, relief="groove")
        def on_leave(e, f=frame):
            f.config(bd=0, relief="raised")
        frame.bind("<Enter>", on_enter)
        frame.bind("<Leave>", on_leave)

        # ---------- CLICK ACTIONS ----------
        if card["action"] == "guardian":
            options = ["Mom", "Dad", "Sister", "Brother", "Cousin", "Friend"]
            btn_frame = Frame(frame, bg=card["bg"])
            btn_frame.pack(pady=10)
            for opt in options:
                def make_command(opt=opt):
                    return lambda: (guardian_var.set(opt), select_guardian(guardian_var))
                b = Button(btn_frame, text=opt, font=("Helvetica", 14), bg="#DDDDDD", command=make_command())
                b.pack(pady=3, fill="x", padx=10)
        elif card["action"] == "sos":
            frame.bind("<Button-1>", lambda e: manual_sos())
            lbl.bind("<Button-1>", lambda e: manual_sos())
        elif card["action"] == "report":
            frame.bind("<Button-1>", lambda e: report_scam())
            lbl.bind("<Button-1>", lambda e: report_scam())

        # Save references to global frames for color updates
        if card["action"] == "sos":
            global sos_box
            sos_box = frame
        elif card["action"] == "report":
            global report_box
            report_box = frame

    # ESC → close window
    window.bind("<Escape>", lambda e: window.destroy())
