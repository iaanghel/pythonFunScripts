import tkinter as tk
from tkinter import ttk
import urllib.request
import json




def get_price(url):
	request = urllib.request.urlopen(url,timeout = 4000)
	x = json.loads(request.read())["data"]["market_data"]["price_usd"]
	request.close()
	return x
def get_timestamp(url):
	request = urllib.request.urlopen(url,timeout = 4000)
	data =json.load(request)	
	request.close()
	return data["status"]["timestamp"]
	
		

def refresh_price():
	global url
	aLable.configure(text="Price:  " + str(round(get_price(url),2) )+ " USD")
	date, hour = get_timestamp(url).split("T")
	hour = hour.split(".")[0]
	bLable.configure(text="Time: " + date + " h: " + hour)
	


if __name__ == "__main__":		
	url = "https://data.messari.io/api/v1/assets/btc/metrics"
	window = tk.Tk()
	window.geometry("250x100")
	window.title("Bitcoin price in USD")
	
	aLable = ttk.Label(window, text="Price: " + str(round(get_price(url),2) )+ " USD")
	aLable.grid(column=0, row=0, padx=60, pady=4)
	
	date, hour = get_timestamp(url).split("T")
	hour = hour.split(".")[0]
	bLable = ttk.Label(text="Time: " + date + " h: " + hour)	
	bLable.grid(column=0, row=1, padx=8, pady=4)

	action = ttk.Button(window, text="Refresh", command=refresh_price)
	action.grid(column=0, row=2, padx=8, pady=4)

	window.mainloop()
