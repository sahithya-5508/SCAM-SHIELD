import tkinter as tk
from tkinter import Frame, Label, Button, Text, messagebox

BG = "#E0BBE4"  # background same as dashboard
BOX_COLORS = ["#E0BBE4", "#E0BBE4"]  # pleasant colors for two boxes

def open_module(parent):
    win = tk.Toplevel(parent)
    win.title("Message Protection")
    win.attributes("-fullscreen", True)
    win.configure(bg=BG)

    # ---------- TOP BAR: Title + Back ----------
    top = Frame(win, bg=BG)
    top.pack(fill="x", pady=20)
    Label(top, text="Message Protection", font=("Helvetica", 32, "bold"),
          bg=BG, fg="#000000").pack(side="left", padx=40)

    # Back button
    back_btn = Button(top, text="Back", font=("Helvetica", 14, "bold"),
                      bg="#DDDDDD", command=win.destroy)
    back_btn.pack(side="right", padx=40)

    # ---------- CONTAINER ----------
    content = Frame(win, bg=BG)
    content.pack(expand=True)

    CARD_W, CARD_H = 900, 250
    PAD_Y = 40

    # ---------- Clipboard Guardian Box ----------
    cg_frame = Frame(content, width=CARD_W, height=CARD_H, bg=BOX_COLORS[0])
    cg_frame.pack(pady=PAD_Y)
    cg_frame.pack_propagate(False)

    Label(cg_frame, text="Clipboard Guardian", font=("Helvetica", 24, "bold"),
          bg=BOX_COLORS[0]).pack(pady=15)
    info_cg = Text(cg_frame, height=5, width=100)
    info_cg.pack(pady=5)
    result_label = Label(cg_frame, text="", font=("Helvetica", 16, "bold"), bg=BOX_COLORS[0], fg="black")
    result_label.pack(pady=5)

    def analyze_clipboard():
        content_text = info_cg.get("1.0", "end").strip().lower()
        if not content_text:
            messagebox.showinfo("Clipboard Guardian", "Paste some text first!")
            return
        risk = "Safe"
        fg_color = "green"
        if any(x in content_text for x in ["urgent","send the otp","blocked","you have won","prize","congratulations user","last chance","only 24 hours left","free","refund","no hidden fees","click this link to reactivate","kyc update rquired","lottery","exclusive offer"]):
            risk = "Suspicious"; fg_color="dark orange"
        if any(x in content_text for x in ["transfer","password","pin","bank","kill","verify","account","link","action required","free","your account will be closed","make money fast","message from bank/company","guaranteed","no hidden fess","suspicious activity"]):
            risk = "Dangerous"; fg_color="red"
        result_label.config(text=f"Result: {risk}", fg=fg_color)

    Button(cg_frame, text="Analyze", font=("Helvetica", 14), command=analyze_clipboard).pack(pady=5)

    # ---------- Scam Probability Meter Box ----------
    sp_frame = Frame(content, width=CARD_W, height=CARD_H, bg=BOX_COLORS[1])
    sp_frame.pack(pady=PAD_Y)
    sp_frame.pack_propagate(False)

    Label(sp_frame, text="Scam Probability Meter", font=("Helvetica", 24, "bold"),
          bg=BOX_COLORS[1]).pack(pady=15)
    info_sp = Text(sp_frame, height=5, width=100)
    info_sp.pack(pady=5)
    score_label = Label(sp_frame, text="", font=("Helvetica", 16, "bold"), bg=BOX_COLORS[1], fg="black")
    score_label.pack(pady=10)

    def compute_probability():
        s = info_sp.get("1.0", "end").strip().lower()
        if not s:
            score_label.config(text="Please enter text!", fg="black")
            return

        # Define keyword sets
        urgent_words = ["urgent","verify","send the otp","password","action required","free","your account will be closed","make money fast","message from bank/company","guaranteed","no hidden fess","suspicious activity"]
        prize_words = ["you have won","prize","congratulations user","last chance","only 24 hours left","free","refund","no hidden fees","click this link to reactivate","kyc update rquired","lottery","exclusive offer"]
        # Strong/dangerous indicators (including violent/threat words)
        dangerous_keywords = [
            "transfer","password","pin","bank","kill","murder","shoot","attack","harm","die","account","link","verify",
            "your account will be closed","action required","make money fast","message from bank/company","guaranteed",
            "suspicious activity"
        ]

        # Decide only among three fixed scores: 0 (Safe), 65 (Suspicious), 90 (Dangerous)
        if any(x in s for x in dangerous_keywords):
            score = 90
            label = "Dangerous"
        elif any(x in s for x in urgent_words + prize_words) or len(s) > 150:
            # If it contains common scam indicators or is very long, mark Suspicious
            score = 65
            label = "Suspicious"
        else:
            score = 0
            label = "Safe"

        fg_color = "green" if score == 0 else ("orange" if score == 65 else "red")
        score_label.config(text=f"Score: {score}% → {label}", fg=fg_color)

    Button(sp_frame, text="Compute", font=("Helvetica", 14), command=compute_probability).pack(pady=5)

    # ESC closes
    win.bind("<Escape>", lambda e: win.destroy())
