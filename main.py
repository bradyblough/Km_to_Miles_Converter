from tkinter import *
import math


# function to generate km to miles
def miles_to_km():
    km_input = entry.get()
    result = float(km_input) * 0.621
    # updates empty label with function result
    empty_label.config(text=result)
    return math.ceil(result)


# window creation
window = Tk()
window.minsize(width=300, height=120)
window.configure(padx=40, pady=30)
window.title("Km to Miles Converter")
# entry box
entry = Entry(width=6)
entry.grid(row=0, column=1)
# miles label
miles_label = Label(text="Km")
miles_label.grid(row=0, column=2)
# = to label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)
# empty label
empty_label = Label(text="")
empty_label.grid(row=1, column=1)
# km label
km_label = Label(text="Miles")
km_label.grid(row=1, column=2)
# calculate button
# calls miles_to_km function
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
