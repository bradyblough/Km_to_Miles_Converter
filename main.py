from tkinter import Tk, Label, Button, Entry, Frame, font as tkFont

def calculate_km_to_miles(km):
    try:
        km_value = float(km)
        miles = km_value * 0.621371
        return miles
    except ValueError:
        return None

def convert_km_to_miles():
    km_input = entry.get()
    miles = calculate_km_to_miles(km_input)
    if miles is not None:
        result_label.config(text=f"{miles:.2f}")  
        error_label.config(text="")  # Clear error message when input is valid
    else:
        result_label.config(text="0")  # Reset result label
        error_label.config(text="Provide a number.", fg="red")  # Display error message in red

# GUI setup
window = Tk()
window.title("Km to Miles Converter")
window.config(padx=50, pady=5, bg="white")  # Set background to white

customFont = tkFont.Font(family="Helvetica", size=12)

main_frame = Frame(window, bg="white")
main_frame.grid(padx=1, pady=1)

entry = Entry(main_frame, width=7, font=customFont, borderwidth=1, relief="groove", bg="white")
entry.grid(row=0, column=1, padx=10, pady=(10), sticky="W")
entry.insert(0, "0")  # Default value

# Label for static texts
Label(main_frame, text="Km", font=customFont, bg="white").grid(row=0, column=2, padx=(0, 0), pady=0, sticky="W")
Label(main_frame, text="=", font=customFont, bg="white").grid(row=0, column=3, sticky="E")
Label(main_frame, text="miles", font=customFont, bg="white").grid(row=0, column=5, padx=(0, 0), pady=0, sticky="W")

# Label to display the conversion result, initially set to "0"
result_label = Label(main_frame, text=0, font=customFont, bg="white")
result_label.grid(row=0, column=4, sticky="W")

calculate_button = Button(main_frame, text="Calculate", command=convert_km_to_miles, font=customFont, bg="#4CAF50", fg="white", activebackground="#45a049")
calculate_button.grid(row=2, column=1)

error_label = Label(main_frame, text="", font=customFont, bg="white")
error_label.grid(row=3, column=1) 

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.resizable(width=False, height=False)  # Prevent window resizing

window.mainloop()