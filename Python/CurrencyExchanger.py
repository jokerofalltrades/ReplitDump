from tkinter import Tk, Button, Entry

e1 = None
e2 = None

CurrencyConverter = Tk()
CurrencyConverter.title("Best Exchange Rate Ltd.")
CurrencyConverter.geometry("400x400")
CurrencyConverter.config(bg="#00240a")

def GBPtoUSD():
    global e1
    global e2
    GBP = int(e1.get())
    Result = round(GBP * 1.31, 2)
    e2.insert(0, str(Result) + " USD")

def USDtoGBP():
    global e1
    global e2
    USD = int(e1.get())
    Result = round(USD * 0.76, 2)
    e2.insert(0, str(Result) + " GBP")

Button(CurrencyConverter, text="£ to $", height=int(0.4), width=2, bg="#064c00", fg="white", font="Oxygen", command=GBPtoUSD).grid(row=2)

e1 = Entry(CurrencyConverter)
e1.grid(row=1, column=1)

e2 = Entry(CurrencyConverter)
e2.grid(row=3, column=1)