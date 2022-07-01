import tkinter as tk
import requests
from PIL import Image, ImageTk
import login

# API => 5c57a0d34d033f6d3d8501aac37ecc96
# API url => api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

login.main()

root = tk.Tk()
root.title("Weather App")
root.geometry("600x500")


def format_response(x):
        try:
            city = x['name']
            condition = x['weather'][0]['description']
            temp = x['main']['temp']
            humidity = x['main']['humidity']
            final_str = 'City : %s \n\nCondition : %s \n\nTemperature : %s F \n\nHumidity : %s'%(city, condition, temp,humidity)
        except:
            final_str = "There was a problem retrieving the\n weather data for this city"
        return final_str        


def get_weather(city):
    weather_key = '5c57a0d34d033f6d3d8501aac37ecc96'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # dictionary => key:value pair
    params = {'appid':weather_key, 'q':city}
    response = requests.get(url,params)
        
    x = response.json()
    #print(x)
    result['text'] = format_response(x)

    icon = x['weather'][0]['icon']

img = Image.open('./p5.jpg')
img = img.resize((600,500),Image.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

title = tk.Label(bg_lbl,text="Search Available for more than 200,000 citites!", font=("times new roman",13,"bold"))
title.place(x=100,y=18)

frame1 = tk.Frame(bg_lbl, bg="black", bd=5)
frame1.place(x=60,y=60, width=450, height=50)

txt_box = tk.Entry(frame1, font=("times new roman",25), width=17,)
txt_box.grid(row=0,column=0,sticky='w')

btn = tk.Button(frame1,text="Get Weather", font=("times new roman",16,"bold"), command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=12)

frame2 = tk.Frame(bg_lbl, bg="black", bd=5)
frame2.place(x=60,y=130, width=450, height=300)

result = tk.Label(frame2,font=("times new roman",20,"bold"), bg="white", justify="left", anchor="nw")
result.place(relwidth=1,relheight=1)   
    

root.mainloop()
