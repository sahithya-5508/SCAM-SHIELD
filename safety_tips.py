import tkinter as tk
from tkinter import Frame, Label, Button

# Safety tips with colored icons
TIPS = [
    {"icon": "✅", "text": "Never share your OTP or password with anyone."},
    {"icon": "📞", "text": "Verify unknown callers before responding."},
    {"icon": "⚠️", "text": "Be cautious of suspicious links."},
    {"icon": "💳", "text": "Check payment requests carefully."},
    {"icon": "🔒", "text": "Use strong passwords and enable 2FA."},
    {"icon": "📱", "text": "Keep your apps updated with latest patches."},
    {"icon": "👁️", "text": "Monitor your accounts regularly for unusual activity."},
    {"icon": "🤝", "text": "Trust only known contacts and verify new friends before sharing info."}
]

def open_module(parent):
    window = tk.Toplevel(parent)
    window.title("Safety Tips")
    window.attributes("-fullscreen", True)
    window.configure(bg="#E0BBE4")  # Soft pastel background

    # ---------- TITLE ----------
    Label(
        window,
        text="Safety Tips",
        font=("Helvetica", 32, "bold"),
        bg="#E0BBE4",
        fg="#000000"
    ).pack(pady=30, fill="x")

    # ---------- BACK BUTTON ----------
    back_btn = Button(
        window,
        text="Back",
        font=("Helvetica", 14, "bold"),
        bg="#DDDDDD",
        command=window.destroy
    )
    back_btn.place(relx=0.95, rely=0.02, anchor="ne")

    # ---------- CONTAINER ----------
    container = Frame(window, bg="#E0BBE4")
    container.pack(pady=20)

    CARD_W = 350
    CARD_H = 150
    PADDING_X = 20
    PADDING_Y = 20

    # Row layouts
    row_layouts = [3, 3, 2]  # First row 3, second 3, third 2
    index = 0

    for row_count in row_layouts:
        row_frame = Frame(container, bg="#E0BBE4")
        row_frame.pack(pady=PADDING_Y)

        for col in range(row_count):
            if index >= len(TIPS):
                break
            tip = TIPS[index]

            # Card with default highlight
            card = Frame(
                row_frame,
                width=CARD_W,
                height=CARD_H,
                bg="#FFFFFF",
                bd=0,
                relief="raised",
                highlightthickness=4,
                highlightbackground="#61E861"  # default green outline
            )
            card.pack(side="left", padx=PADDING_X)
            card.pack_propagate(False)

            # Tip label with icon
            label = Label(
                card,
                text=f"{tip['icon']}\n{tip['text']}",
                font=("Helvetica", 16),
                bg="#FFFFFF",
                fg="#000000",
                justify="center",
                wraplength=CARD_W - 20
            )
            label.place(relx=0.5, rely=0.5, anchor="center")

            # Hover effect (optional subtle)
            def on_enter(e, c=card):
                c.config(bg="#F7F7F7")
            def on_leave(e, c=card):
                c.config(bg="#FFFFFF")
            card.bind("<Enter>", on_enter)
            card.bind("<Leave>", on_leave)

            index += 1

    # ESC → close window
    window.bind("<Escape>", lambda e: window.destroy())
