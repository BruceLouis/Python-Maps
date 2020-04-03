from tkinter import *

window = Tk()

def kg_conversion():
    grams = float(entry_1_value.get()) * 1000
    pounds = float(entry_1_value.get()) * 2.20462
    ounces = float(entry_1_value.get()) * 35.274
    
    grams_text.delete("1.0", END)
    grams_text.insert(END, grams)
    
    pounds_text.delete("1.0", END)
    pounds_text.insert(END, pounds)
    
    ounces_text.delete("1.0", END)
    ounces_text.insert(END, ounces)

label_1 = Label(window, text = "kilograms")
label_1.grid(row = 0, column = 0)

button_1 = Button(window, text = "convert", command = kg_conversion)
button_1.grid(row = 0, column = 2)

entry_1_value = StringVar()
entry_1 = Entry(window, width = 20, textvariable = entry_1_value)
entry_1.grid(row = 0, column = 1)

grams_label = Label(window, text = "grams")
grams_label.grid(row = 1, column = 0)
grams_text = Text(window, height = 1, width = 20)
grams_text.grid(row = 2, column = 0)

pounds_label = Label(window, text = "pounds")
pounds_label.grid(row = 1, column = 1)
pounds_text = Text(window, height = 1, width = 20)
pounds_text.grid(row = 2, column = 1)

ounces_label = Label(window, text = "ounces")
ounces_label.grid(row = 1, column = 2)
ounces_text = Text(window, height = 1, width = 20)
ounces_text.grid(row = 2, column = 2)

window.mainloop()
