from tkinter import *
import requests


window = Tk()
window.title("Wymiana walut")
window.geometry("400x200")

def multiplication(ask):
    inserted_amout = entry.get()
    if inserted_amout == "":
        v.set("Please insert data.")
    else:
        result = float(inserted_amout)*ask
        rounded_value = round(result,2)
        v.set(rounded_value)

def download_data(data):
    result = data.json()
    #print(result)
    exchange_rate = result["rates"][0]["ask"]
    #print(exchange_rate)
    if exchange_rate >= 0:
        multiplication(exchange_rate)
    else:
        print("Error, exchange rate cannot be below 0")

def get_url():
    selected_currency = clicked.get()
    url = "http://api.nbp.pl/api/exchangerates/rates/c/{}/2016-04-04/?format=json".format(selected_currency)
    data = requests.get(url)
    print(url)
    if data.status_code == 200:
        download_data(data)
    else:
        print("błąd")
        return -1

options = [
    "USD",
    "AUD",
    "CAD",
    "EUR",
    "HUF",
    "CHF",
    "GBP",
    "JPY",
    "CZK",
    "NOK",
    "SEK",
    "XDR"
]

clicked = StringVar()
clicked.set(options[0])
#print(clicked.get())

execute_button=Button(window,text="Execute", command=get_url)
execute_button.grid(row=0, column=1)

entry_value = StringVar()
entry = Entry(window, textvariable = entry_value)
entry.grid(row=0,column=2)

v = StringVar()
text_place = Label(window,textvariable=v ,height=1,width=20)
text_place.grid(row=3,column =2)

drop = OptionMenu(window, clicked, *options)
drop.grid(row=0, column=3)


window.mainloop()