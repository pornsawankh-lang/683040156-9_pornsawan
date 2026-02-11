"""
Pornsawan Khareram
683040156-9
"""

import tkinter as tk

def create_circle_icon(parent, text, color):
    canvas = tk.Canvas(parent, width=40, height=40, bg="white", highlightthickness=0)
    canvas.pack(side="left", padx=10)
    
    canvas.create_oval(2, 2, 38, 38, outline=color, width=2)
    

    canvas.create_text(20, 20, text=text, fill=color, font=("Arial", 12, "bold"))
    
    return canvas

def create_login_ui():
    root = tk.Tk()
    root.title("Lab 5-1: Login UI")
    root.geometry("350x600")
    root.configure(bg="white")

    main_frame = tk.Frame(root, bg="white", padx=40, pady=30)
    main_frame.pack(expand=True, fill="both")

    tk.Label(main_frame, text="LOGIN", font=("Arial", 16, "bold"), bg="white", fg="#555").pack(anchor="w", pady=(0, 20))

    tk.Label(main_frame, text="Email", bg="white", fg="#888").pack(anchor="w")
    tk.Entry(main_frame, font=("Arial", 12), bd=1, relief="solid").pack(fill="x", pady=(5, 15), ipady=5)

    tk.Label(main_frame, text="Password", bg="white", fg="#888").pack(anchor="w")
    tk.Entry(main_frame, font=("Arial", 12), bd=1, relief="solid", show="*").pack(fill="x", pady=(5, 10), ipady=5)

    tk.Checkbutton(main_frame, text="Remember me?", bg="white", activebackground="white").pack(anchor="w")

    tk.Button(main_frame, text="LOGIN", bg="#e95d8b", fg="white", font=("Arial", 11, "bold"), bd=0).pack(fill="x", pady=(15, 5), ipady=8)
    
    tk.Label(main_frame, text="Forgot Password?", bg="white", fg="#888", font=("Arial", 9)).pack(anchor="e")

    divider_frame = tk.Frame(main_frame, bg="white")
    divider_frame.pack(fill="x", pady=20)
    tk.Frame(divider_frame, bg="#ddd", height=1).pack(side="left", fill="x", expand=True)
    tk.Label(divider_frame, text="OR", bg="white", fg="#bbb", font=("Arial", 8)).pack(side="left", padx=10)
    tk.Frame(divider_frame, bg="#ddd", height=1).pack(side="left", fill="x", expand=True)

    social_frame = tk.Frame(main_frame, bg="white")
    social_frame.pack(pady=10)

    create_circle_icon(social_frame, "G", "#db4437")
    create_circle_icon(social_frame, "f", "#4267B2")
    create_circle_icon(social_frame, "in", "#0077b5")

    signup_frame = tk.Frame(main_frame, bg="white")
    signup_frame.pack(side="bottom", pady=20)
    tk.Label(signup_frame, text="Need an account?", bg="white", fg="#555").pack(side="left")
    tk.Label(signup_frame, text="SIGN UP", bg="white", fg="#555", font=("Arial", 9, "bold")).pack(side="left", padx=5)

    root.mainloop()

if __name__ == "__main__":
    create_login_ui()

