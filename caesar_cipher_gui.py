# caesar_cipher_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from caesar_cipher import enkripsi, dekripsi

def process_text():
    try:
        shift = int(shift_value.get())
        text = input_text.get("1.0", "end-1c")
        if mode.get() == "encrypt":
            result = enkripsi(text, shift)
        else:
            result = dekripsi(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid shift value.")

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Machine")
root.geometry("550x500")
root.config(bg="#F5E6CC")  # Background warna pastel krem

# Styling
title_font = ("Helvetica", 18, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Title Label
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=title_font, bg="#FFB6C1", fg="#4B4B4B", pady=10)
title_label.pack(fill="x", pady=(10, 0))

# Frame untuk shift value
shift_frame = tk.Frame(root, bg="#F5E6CC")
shift_frame.pack(pady=10)
tk.Label(shift_frame, text="Shift Value:", font=label_font, bg="#F5E6CC", fg="#4B4B4B").grid(row=0, column=0, padx=10, pady=5)
shift_value = tk.Entry(shift_frame, width=5, font=label_font, bg="#FFF1E6", fg="#4B4B4B", relief="solid", bd=1)
shift_value.grid(row=0, column=1, padx=5, pady=5)

# Frame untuk Input Text
input_frame = tk.Frame(root, bg="#F5E6CC")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Input Text to Encrypt/Decrypt:", font=label_font, bg="#F5E6CC", fg="#4B4B4B").grid(row=0, column=0, padx=10, pady=5)
input_text = tk.Text(input_frame, height=5, width=50, font=("Helvetica", 10), bg="#FFF1E6", fg="#4B4B4B", wrap="word", relief="solid", bd=1)
input_text.grid(row=1, column=0, padx=10, pady=5)

# Frame untuk mode pilihan
mode_frame = tk.Frame(root, bg="#F5E6CC")
mode_frame.pack(pady=10)
mode = tk.StringVar(value="encrypt")
ttk.Style().configure("TRadiobutton", background="#F5E6CC", foreground="#4B4B4B", font=label_font)
ttk.Radiobutton(mode_frame, text="Encrypt", variable=mode, value="encrypt", style="TRadiobutton").grid(row=0, column=0, padx=20)
ttk.Radiobutton(mode_frame, text="Decrypt", variable=mode, value="decrypt", style="TRadiobutton").grid(row=0, column=1, padx=20)

# Tombol Process
process_button = tk.Button(root, text="Process Text", command=process_text, font=button_font, bg="#B5EAD7", fg="#4B4B4B", activebackground="#A4D4AE", activeforeground="#4B4B4B", relief="flat")
process_button.pack(pady=15)

# Frame untuk Output Text
output_frame = tk.Frame(root, bg="#F5E6CC")
output_frame.pack(pady=10)
tk.Label(output_frame, text="Output:", font=label_font, bg="#F5E6CC", fg="#4B4B4B").grid(row=0, column=0, padx=10, pady=5)
output_text = tk.Text(output_frame, height=5, width=50, font=("Helvetica", 10), bg="#FFF1E6", fg="#4B4B4B", wrap="word", relief="solid", bd=1)
output_text.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()
