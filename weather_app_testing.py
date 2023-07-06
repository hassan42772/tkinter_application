import tkinter as tk
import requests
import json
root=tk.Tk()
root.title("WEATHER APP")
root.geometry("1300x1300") 
root.configure(background="black")
root.iconbitmap(r'4.ico') 

def read():
    global current_humidity
    global current_pressure
    global current_temperature
    global label8
    global label5
    global label7
    global label2
    api_key = "ee512e3b141f2b7d550d67dfa50fada9"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "bahawalnagar"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x=response.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    
    label2.configure(text=str(int(current_temperature-273)) +"°C")
    label5.configure(text=str(current_humidity)+" %")
    label7.configure(text=str(current_pressure)+" mb")
    label8.after(2000,read)




master_frame=tk.Frame(root,background="black")
master_frame.pack(fill="both",expand=True)
frame1=tk.Frame(master_frame,background="black")
frame1.grid(column=0,row=0)
label4=tk.Label(frame1,text="WEATHER APPLICATION",bg="black",fg="white",width=40,height=3,font="arial 30 bold")
label4.grid(column=0,row=0,padx=220)
frame2=tk.Frame(master_frame,background="black")
frame2.grid(column=0,row=2)
label1=tk.Label(frame2,text="TEMPERATURE",bg="black",fg="white",width=15,height=2,font="arial 12 bold")
label1.grid(column=0,row=0)
label2=tk.Label(frame2,text="",bg="white",fg="black",width=15,height=2,font="arial 12 bold")
label2.grid(column=1,row=0,pady=10,)
label3=tk.Label(frame2,text="HUMADITY",bg="black",fg="white",width=15,height=2,font="arial 12 bold")
label3.grid(column=0,row=1)
label5=tk.Label(frame2,text="",bg="white",fg="black",width=15,height=2,font="arial 12 bold")
label5.grid(column=1,row=1,pady=10)
label6=tk.Label(frame2,text="PRESSURE",bg="black",fg="white",width=15,height=2,font="arial 12 bold")
label6.grid(column=0,row=2)
label7=tk.Label(frame2,text="",bg="white",fg="black",width=15,height=2,font="arial 12 bold")
label7.grid(column=1,row=2,pady=10)
label8=tk.Label(frame2,text="",bg="black",fg="black",width=15,height=2,font="arial 12 bold")
label8.grid(column=1,row=3,pady=10)
read()
root.mainloop()


