"""
Pornsawan Khareram
683040156-9
"""
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  
import re

class RegistrationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Registration")
        self.root.geometry("500x650")
        
        # Variables to store form data
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Prefer not to say")
        self.program_var = tk.StringVar(value="Computer Science")
        self.understand_var = tk.BooleanVar(value=False)
        self.dob_var = tk.StringVar()
        self.story_var = ""

        # Start with registration page
        self.current_frame = None
        self.show_registration_page()
        
    def clear_window(self):
        if self.current_frame:
            self.current_frame.destroy()
    
    def show_registration_page(self):
        # Clear all variables
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.gender_var.set("Prefer not to say")
        self.program_var.set("Computer Science")
        self.understand_var.set(False)
        self.dob_var.set("")
        self.comment_content = ""  # Clear saved comment content
        
        self.clear_window()
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Title
        ttk.Label(
            self.current_frame,
            text="Student Registration Form",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)
        
        # Create form fields
        self.create_form_fields()

        # Clear the Text widget after it's created (in case of coming back from confirmation)
        self.story_text.delete("1.0", "end")
    
    def create_form_fields(self):
        
        form_frame = ttk.Frame(self.current_frame)
        form_frame.pack(fill='x', pady=5)
        
  
        # Name
        ttk.Label(form_frame, text="Name:").pack(anchor='w', pady=(5,0))
        ttk.Entry(form_frame, textvariable=self.name_var).pack(fill='x', pady=2)

        # Email
        ttk.Label(form_frame, text="Email:").pack(anchor='w', pady=(5,0))
        ttk.Entry(form_frame, textvariable=self.email_var).pack(fill='x', pady=2)

        #  Phone
        ttk.Label(form_frame, text="Phone:").pack(anchor='w', pady=(5,0))
        ttk.Entry(form_frame, textvariable=self.phone_var).pack(fill='x', pady=2)
        
        # Date of Birth
        ttk.Label(form_frame, text="Birth Date:").pack(anchor='w', pady=(5,0))
        self.dob_entry = DateEntry(
            form_frame,
            width=20,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            year=2000,
            textvariable=self.dob_var
        )
        self.dob_entry.pack(anchor='w', pady=2)
        
        # 5. Gender
        ttk.Label(form_frame, text="Gender:").pack(anchor='w', pady=(5,0))
        gender_frame = ttk.Frame(form_frame)
        gender_frame.pack(anchor='w', pady=2)
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male").pack(side='left')
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female").pack(side='left')
        ttk.Radiobutton(gender_frame, text="Non-binary", variable=self.gender_var, value="Non-binary").pack(side='left')
        ttk.Radiobutton(gender_frame, text="Prefer not to say", variable=self.gender_var, value="Prefer not to say").pack(side='left')
        

        # Program
        ttk.Label(form_frame, text="Program:").pack(anchor='w', pady=(5,0))
        program_cb = ttk.Combobox(form_frame, textvariable=self.program_var, state="readonly")
        program_cb['values'] = ("Computer Science", "Engineering", "Business", "Arts", "Sciences")
        program_cb.pack(fill='x', pady=2)

    
        # Tell us about yourself
        ttk.Label(form_frame, text="Tell us a little bit about yourself:").pack(anchor='w', pady=(5,0))
        self.story_text = tk.Text(form_frame, height=4, width=30)
        self.story_text.pack(fill='x', pady=2)
                
        
        # Accept Checkbox & Submit Button
        ttk.Checkbutton(
            form_frame, 
            text="I accept the terms and conditions.", 
            variable=self.understand_var
        ).pack(anchor='w', pady=10)
        
        ttk.Button(form_frame, text="Submit Registration", command=self.validate_and_submit).pack(pady=10)
    
    def validate_and_submit(self):
        # Basic validation
        if not self.name_var.get().strip():
            messagebox.showerror("Error", "Please enter your name")
            return
        
        if not self.validate_email(self.email_var.get()):
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        if not self.validate_phone(self.phone_var.get()):
            messagebox.showerror("Error", "Please enter a valid phone number")
            return
        
        if not self.understand_var.get():
            messagebox.showerror("Error", "Please accept the terms and conditions.")
            return

        # save text in the comment box
        self.story_var = self.story_text.get("1.0", "end-1c")

        # If validation passes, show confirmation page
        self.show_confirmation_page()
    
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone):
        pattern = r'^\d{9,10}$'
        return re.match(pattern, phone) is not None
    
    def show_confirmation_page(self):

        self.clear_window()
        self.current_frame = ttk.Frame(self.root)
        self.current_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        
        # Title
        ttk.Label(
            self.current_frame,
            text="Registration Confirmed!",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)

        # Info Frame
        info_frame = ttk.Frame(self.current_frame)
        info_frame.pack(fill='x', pady=10)

        # Display details matching the confirmation screenshot order
        ttk.Label(info_frame, text=f"Name: {self.name_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Email: {self.email_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Phone: {self.phone_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Birth Date: {self.dob_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Gender: {self.gender_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Program: {self.program_var.get()}").pack(anchor='w', pady=2)
        ttk.Label(info_frame, text=f"Story: {self.story_var}").pack(anchor='w', pady=2)

        # New Registration Button
        ttk.Button(
            self.current_frame, 
            text="New Registration", 
            command=self.show_registration_page
        ).pack(pady=20)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RegistrationApp()
    app.run()