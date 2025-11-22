from tkinter import*
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()

    data = requests.get( "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3daf7fb98ac4f7b004cdd1a86118ca5e" ).json()

    W_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])

    temp_celsius = data["main"]["temp"] - 273.15
    temp_label1.config(text=f"{temp_celsius:.2f} °C")

    pressure_label1.config(text=str(data["main"]["pressure"]))


win = Tk()
win.title("Parth Gaur Solutions")
win.config(bg="orange")
win.geometry("500x570")

name_label = Label(win, text="Weatherbash Weather App",
                   font=("Arial Black", 20, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry") 

com = ttk.Combobox(win, values=list_name,
                   font=("Times New Roman", 15),
                   textvariable=city_name)
com.place(x=25, y=120, height=40, width=450)

W_label = Label(win, text="Weather Climate",
                font=("Times New Roman", 17, "bold"))
W_label.place(x=25, y=260, height=50, width=210)

W_label1 = Label(win, text="", font=("Times New Roman", 17, "bold"))
W_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description",
                 font=("Times New Roman", 17, "bold"))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Times New Roman", 17, "bold"))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature",
                   font=("Times New Roman", 17, "bold"))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 17, "bold"))
temp_label1.place(x=250, y=400, height=50, width=210)

pressure_label = Label(win, text="Pressure",
                       font=("Times New Roman", 17, "bold"))
pressure_label.place(x=25, y=470, height=50, width=210)

pressure_label1 = Label(win, text="", font=("Times New Roman", 17, "bold"))
pressure_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done",
                     font=("Arial Black", 20, "bold"),
                     command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop()
