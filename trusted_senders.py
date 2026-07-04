import tkinter as tk

# Sample sender messages / scores
MESSAGES = [
    {"sender": "Alice (Known person)", "message": "Hey, how are you?", "score": "0%(Safe)", "status": "green"},
    {"sender": "Bob (Unknown person)", "message": "Check this link!", "score": "60%(Suspicious)", "status": "yellow"},
    {"sender": "Scam Caller", "message": "Send me your bank info!", "score": "90%(Danger)", "status": "red"},
    {"sender": "Unknown Number", "message": "You won a prize!", "score": "75%(Risk)", "status": "red"},
]

# Status colors for borders
STATUS_COLOR = {
    "green": "#61E861",   # High score
    "yellow": "#EAEA19",  # Medium score
    "red": "#F24303"      # Low score
}

def open_module(parent):
    window = tk.Toplevel(parent)
    window.title("Trusted Sender Score")
    window.attributes("-fullscreen", True)
    window.configure(bg="#E0BBE4")

    # ---------- Title ----------
    title = tk.Label(
        window,
        text="Trusted Sender Score",
        font=("Helvetica", 32, "bold"),
        bg="#E0BBE4",
        fg="black"
    )
    title.pack(pady=20, fill="x")

    # ---------- Back Button ----------
    back_btn = tk.Button(
        window,
        text="Back",
        font=("Helvetica", 14, "bold"),
        bg="#DDDDDD",
        command=window.destroy
    )
    back_btn.place(relx=0.95, rely=0.02, anchor="ne")

    # ---------- Container for messages ----------
    container = tk.Frame(window, bg="#E0BBE4")
    container.pack(expand=True, fill="both", padx=30, pady=20)

    # Keep reference to last selected card
    last_selected_card = {"frame": None}

    def set_score_color(card_frame, status):
        """Highlight selected card and reset previous"""
        if last_selected_card["frame"] and last_selected_card["frame"] != card_frame:
            last_selected_card["frame"].config(highlightbackground="#DDD")
        card_frame.config(highlightbackground=STATUS_COLOR.get(status, "#DDD"))
        last_selected_card["frame"] = card_frame

    for msg in MESSAGES:
        card_frame = tk.Frame(
            container,
            bg="white",
            bd=0,
            relief="raised",
            highlightthickness=4,
            highlightbackground="#DDD",
            padx=20,
            pady=15
        )
        card_frame.pack(pady=15, fill="x")

        # Sender
        sender_label = tk.Label(
            card_frame,
            text=f"Sender: {msg['sender']}",
            font=("Helvetica", 18, "bold"),
            bg="white",
            anchor="w"
        )
        sender_label.pack(fill="x")

        # Message
        message_label = tk.Label(
            card_frame,
            text=f"Message: {msg['message']}",
            font=("Helvetica", 16),
            bg="white",
            wraplength=900,
            justify="left"
        )
        message_label.pack(fill="x", pady=5)

        # Score
        score_label = tk.Label(
            card_frame,
            text=f"Score: {msg['score']}",
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg=STATUS_COLOR[msg['status']]
        )
        score_label.pack(anchor="e")

        # Click → highlight selected card and reset previous
        for widget in [card_frame, sender_label, message_label, score_label]:
            widget.bind(
                "<Button-1>",
                lambda e, f=card_frame, st=msg['status']: set_score_color(f, st)
            )

        # Hover effect
        def on_enter(e, f=card_frame):
            f.config(bg="#F7F7F7")
        def on_leave(e, f=card_frame):
            f.config(bg="white")
        card_frame.bind("<Enter>", on_enter)
        card_frame.bind("<Leave>", on_leave)

    # ESC → close window
    window.bind("<Escape>", lambda e: window.destroy())

