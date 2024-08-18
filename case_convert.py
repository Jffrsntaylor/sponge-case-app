import customtkinter as ctk
import random
import pyperclip

def convert_to_sponge_case(text):
    def sponge_case(text, start_with_upper):
        result = []
        use_upper = start_with_upper

        for char in text:
            if char.isalpha():
                result.append(char.upper() if use_upper else char.lower())
                use_upper = not use_upper
            else:
                result.append(char)
        
        return ''.join(result)

    # Determine the case for the first letter
    if text:
        first_char = text[0]
        start_with_upper = random.choice([True, False]) if first_char.isalpha() else random.choice([True, False])

        # Apply Sponge Case conversion
        return sponge_case(text, start_with_upper)
    else:
        return text

def on_convert_button_click():
    input_text = text_input.get("1.0", "end").strip()
    if input_text:
        sponge_case_text = convert_to_sponge_case(input_text)
        text_output.configure(state="normal")
        text_output.delete("1.0", "end")
        text_output.insert("end", sponge_case_text)
        text_output.configure(state="disabled")
        status_label.configure(text="Text converted!", text_color="#28a745")
    else:
        status_label.configure(text="No text to convert!", text_color="#dc3545")

def on_clear_button_click():
    text_input.delete("1.0", "end")
    text_output.configure(state="normal")
    text_output.delete("1.0", "end")
    text_output.configure(state="disabled")
    status_label.configure(text="Text cleared.", text_color="#ffc107")

def on_copy_button_click():
    text_output_content = text_output.get("1.0", "end").strip()
    if text_output_content:
        pyperclip.copy(text_output_content)
        status_label.configure(text="Converted text copied to clipboard!", text_color="#28a745")
    else:
        status_label.configure(text="No text to copy!", text_color="#dc3545")

def on_exit():
    window.destroy()

# Set up the modern UI using customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create the main window
window = ctk.CTk()
window.title("EnTeR YoUr TeXt")
window.geometry("800x450")
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", on_exit)

# Instruction label (in Sponge Case)
instruction_label = ctk.CTkLabel(window, text="EnTeR YoUr TeXt", font=ctk.CTkFont(size=24, weight="bold"))
instruction_label.pack(pady=20)

# Text input box
text_input = ctk.CTkTextbox(window, height=100, font=("Arial", 14))
text_input.pack(pady=10, padx=20, fill="x")

# Frame to hold the buttons horizontally
button_frame = ctk.CTkFrame(window)
button_frame.pack(pady=15)

# Convert button
convert_button = ctk.CTkButton(button_frame, text="Convert", command=on_convert_button_click, width=120, height=40)
convert_button.grid(row=0, column=0, padx=15)

# Clear button
clear_button = ctk.CTkButton(button_frame, text="Clear", command=on_clear_button_click, width=120, height=40)
clear_button.grid(row=0, column=1, padx=15)

# Copy button
copy_button = ctk.CTkButton(button_frame, text="Copy", command=on_copy_button_click, width=120, height=40)
copy_button.grid(row=0, column=2, padx=15)

# Output label
output_label = ctk.CTkLabel(window, text="Converted text:", font=("Arial", 16))
output_label.pack(pady=10)

# Text output box, disabled for editing
text_output = ctk.CTkTextbox(window, height=100, font=("Arial", 14), state="disabled")
text_output.pack(pady=5, padx=20, fill="x")

# Status bar
status_label = ctk.CTkLabel(window, text="", font=("Arial", 12))
status_label.pack(side="bottom", fill="x", pady=10)

# Run the Tkinter event loop
window.mainloop()
