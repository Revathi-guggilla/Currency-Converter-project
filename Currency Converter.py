from currency_converter import CurrencyConverter
import tkinter as tk

c = CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")    
window.title("Currency Converter")

def clicked():
    try:
        amount = float(entry1.get())
        cur1 = entry2.get().upper()
        cur2 = entry3.get().upper()
        result = c.convert(amount, cur1, cur2)
        label4.config(text=f"Converted Amount: {result:.2f} {cur2}")
    except Exception as e:
        label4.config(text=f"Error: {e}")

# GUI Layout
label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
label.place(x=120, y=50)

label1 = tk.Label(window, text="Enter amount here:", font="Times 16 bold")
label1.place(x=70, y=100)
entry1 = tk.Entry(window)
entry1.place(x=270, y=105)

label2 = tk.Label(window, text="Enter your currency:", font="Times 16 bold")
label2.place(x=30, y=150)
entry2 = tk.Entry(window)
entry2.place(x=270, y=155)

label3 = tk.Label(window, text="Enter desired currency:", font="Times 16 bold")
label3.place(x=10, y=200)
entry3 = tk.Entry(window)
entry3.place(x=270, y=205)

button = tk.Button(window, text="Convert", font="Times 16 bold", command=clicked)
button.place(x=200, y=250)

label4 = tk.Label(window, text="", font="Times 16 bold", fg="blue")
label4.place(x=120, y=300)

window.mainloop()

