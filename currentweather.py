from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image
import requests
import pytz

root = Tk()
root.title("Climate Modal Using Tkinter")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city=textfiled.get()

    geolocator = Nominatim(user_agent="geopiExercises")
    Location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result= obj.timezone_at(lng=Location.longitude,lat=Location.latitude)
    
    home= pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT CLIMATE")

    api="key"+city+"key"
    json_data=requests.get(api).json()
    condition= json_data['weather'][0]['main']
    description= json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=(wind))
    h.config(text=(humidity))
    d.config(text=(description))
    p.config(text=(pressure))


search_image=PhotoImage(file="search image")
myimage= Label(image=search_image)
myimage.place(x=20,y=20)

textfiled=tk.Entry(root,justify="center", width= 17,font=("poppins",25,"bold"),bg="#FFFFFF",border=0,fg="blue")
textfiled.place(x=50,y=40)
textfiled.focus()

search_icon = PhotoImage(file="search_icon")
myimage_icon = Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

Logo_image=PhotoImage(file="logo")
logo = Label(image=Logo_image)
logo.place(x=17,y=100)

frame_image = PhotoImage(file="frame_box")
frame_myimage= Label(image=frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=230,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)


w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=230,y=430)

d=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=430)

p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=650,y=430)

#above are just simple designs and font color of personal choice along with font style






root.mainloop()
