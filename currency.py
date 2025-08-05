from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk

# Currency Converter object
c = CurrencyConverter()

# Available currencies from the converter
currency_list = list(c.currencies)

# GUI setup
window = tk.Tk()
window.geometry("550x400")
window.title("Currency Converter")

def clicked():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get().upper()
        to_currency = combo_to.get().upper()
        
        # Conversion
        converted_amount = c.convert(amount, from_currency, to_currency)
        rate = c.convert(1, from_currency, to_currency)
        
        result_label.config(
            text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}\n(1 {from_currency} = {rate:.4f} {to_currency})"
        )
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Title Label
title_label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
title_label.pack(pady=20)

# Amount Entry
tk.Label(window, text="Amount:", font="Times 14").pack()
entry_amount = tk.Entry(window, font="Times 14")
entry_amount.pack(pady=5)

# From Currency
tk.Label(window, text="From Currency:", font="Times 14").pack()
combo_from = ttk.Combobox(window, values=currency_list, font="Times 12")
combo_from.set("USD")  # Default value
combo_from.pack(pady=5)

# To Currency
tk.Label(window, text="To Currency:", font="Times 14").pack()
combo_to = ttk.Combobox(window, values=currency_list, font="Times 12")
combo_to.set("INR")  # Default value
combo_to.pack(pady=5)

# Convert Button
convert_button = tk.Button(window, text="Convert", font="Times 14 bold", command=clicked)
convert_button.pack(pady=15)

# Result Label
result_label = tk.Label(window, text="", font="Times 14", fg="blue")
result_label.pack(pady=10)

# Run the GUI loop
window.mainloop()
