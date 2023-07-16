# author: ononemli

from requests import get
import json
import tkinter as gui

url1 = 'http://ipinfo.io/json'
response = get(url1)
data = json.loads(response.text)

ip = data['ip']
city = data['city']
provider = data['provider']
region = data['region']
country = data['country']
postal = data['postal']
timezone = data['timezone']

form=gui.Tk()

windowWidth = form.winfo_reqwidth()
windowHeight = form.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
positionRight = int(form.winfo_screenwidth()/2 - windowWidth/1)
positionDown = int(form.winfo_screenheight()/2 - windowHeight/1)
form.geometry("350x240")
form.geometry("+{}+{}".format(positionRight, positionDown))

form.config(background = "silver")
form.title("IP Info - ononemli")
form.state("normal")
form.resizable(False,False)

label0=gui.Label(text="*")
label0.pack()

label1=gui.Label(text="my first coding")
label1.configure(font=("Courier", 10, "italic"))
label1.pack()

label2=gui.Label(form,text="in python")
label2.configure(font=("Helvetica", 10, "normal"))
label2.pack()

label3=gui.Label(form,text="--------------------------")
label3.pack()

label4=gui.Label(form,text="IP Address: "+ip)
label4.configure(font=("Terminal", 12, "normal"))
label4.pack()

label5=gui.Label(form,text="Provider: " + provider)
label5.configure(font=("Verdana", 11, "noraml"))
label5.pack()

label6=gui.Label(form,text="City: "+city)
label6.configure(font=("Verdana", 11, "normal"))
label6.pack()

label7=gui.Label(form,text="Region: "+region)
label7.configure(font=("Verdana", 11, "normal"))
label7.pack()

label8=gui.Label(form,text="Country: "+country)
label8.configure(font=("Verdana", 11, "normal"))
label8.pack()

label9=gui.Label(form,text="Postal: "+postal)
label9.configure(font=("Verdana", 11, "normal"))
label9.pack()

label10=gui.Label(form,text="Time Zone: "+timezone)
label10.configure(font=("Verdana", 11, "normal"))
label10.pack()

form.mainloop()
