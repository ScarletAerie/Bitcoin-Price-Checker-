from tkinter import *
from bs4 import BeautifulSoup
import bs4
import urllib
import requests
from urllib import request
from datetime import datetime


root = Tk()
root.title('Bitcoin Price Grabber')
root.geometry("550x210")
root.config(bg="black")

global previous
previous = False

# Get Current Time
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")


# Create a Frame
my_frame = Frame(root, bg="black")
my_frame.pack(pady=20)

# Add bitcoin price label
bit_label = Label(my_frame, text='TEST', 
	font=("Helvetica", 45),
	bg="black",
	fg="green",
	bd=0)
bit_label.grid(row=0, column=1, padx=20, sticky="s")

# Latest Price Up/Down
latest_price = Label(my_frame, text="move test",
	font=("Helvetica", 8),
	bg="black",
	fg="grey")
latest_price.grid(row=1, column=1, sticky="n" )

#Grab the bitcoin price
def Update():
	global previous

	# Grab Bitcoin Price
	r=requests.get('https://ca.finance.yahoo.com/quote/BTC-CAD/')
	soup=bs4.BeautifulSoup(r.text,"html.parser")
	price_large2=soup.find_all('div',{'class':"D(ib) Mend(20px)"})[0].find('span').text
	

	# Update our bitcoin label
	bit_label.config(text=f'${price_large2}')
	# Set timer to 30 seconds
	# 1 second = 1000
	root.after(30000, Update)

	# Get Current Time
	now = datetime.now()
	current_time = now.strftime("%I:%M:%S %p")

	# Update the status bar
	status_bar.config(text=f'Last Updated: {current_time}   ')

	# Determine Price Change
	# grab current Price
	current = price_large2

	# remove the comma
	current = current.replace(',', '')

	if previous:
		if float(previous) > float(current):
			latest_price.config(
				text=f'Price Down {round(float(previous)-float(current), 2)}', fg="red")

		elif float(previous) == float(current):
			latest_price.config(text="Price Unchanged", fg="grey")	

		else:
			latest_price.config(
				text=f'Price Up {round(float(current)-float(previous), 2)}', fg="green")			


	else:
		previous = current
		latest_price.config(text="Price Unchanged", fg="grey")

# Create status bar
status_bar = Label(root, text=f'Last Updated {current_time}   ',
	bd=0,
	anchor=E,
	bg="black",
	fg="grey")

status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# On program start, run update function
Update()
root.mainloop()