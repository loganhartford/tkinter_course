#! .\.venv\scripts\python.exe

import customtkinter as ctk
from settings import *
from main_widgets import *
from weather_data import get_weather

# url request
import urllib.request
import json

# Images
from PIL import Image
from os import walk

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


class App(ctk.CTk):
    def __init__(self, current_data, forcast_data, city, country):
        # Data
        self.current_data = current_data
        self.forcast_data = forcast_data
        self.location = {"city": city, "country": country}
        self.color = WEATHER_DATA[self.current_data["weather"]]

        # Images imports
        self.forcast_images = [
            Image.open(f"weather/images/{info['weather']}.png")
            for info in self.forcast_data.values()
        ]
        self.today_animation = self.import_folder("weather/" + self.color["path"])

        super().__init__(fg_color=self.color["main"])
        self.title_bar_color(self.color["title"])
        self.geometry("550x250")
        self.minsize(550, 250)
        self.title("")
        self.iconbitmap("weather/empty.ico")

        # Start widget
        self.widget = SmallWidget(
            self,
            self.current_data,
            self.forcast_data,
            self.location,
            self.color,
            self.today_animation,
        )

        # States
        self.height_break = 600
        self.width_break = 1000
        self.full_height_bool = ctk.BooleanVar(value=False)
        self.full_width_bool = ctk.BooleanVar(value=False)
        self.bind("<Configure>", self.check_size)
        self.full_width_bool.trace("w", self.change_size)
        self.full_height_bool.trace("w", self.change_size)

        self.mainloop()

    def import_folder(self, path):
        for _, __, image_data in walk(path):
            sorted_data = sorted(image_data, key=lambda item: int(item.split(".")[0]))
            image_paths = [path + "/" + item for item in sorted_data]

        images = [Image.open(path) for path in image_paths]
        return images

    def title_bar_color(self, color):
        try:
            HNWD = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            windll.dwmapi.DwmSetWindowAttribute(
                HNWD, DWMWA_ATTRIBUTE, byref(c_int(color)), sizeof(c_int)
            )
        except:
            pass

    def check_size(self, event):
        if event.widget == self:
            # Width
            if self.full_width_bool.get():
                if event.width < self.width_break:
                    self.full_width_bool.set(False)
            else:
                if event.width > self.width_break:
                    self.full_width_bool.set(True)
            # Height
            if self.full_height_bool.get():
                if event.height < self.height_break:
                    self.full_height_bool.set(False)
            else:
                if event.height > self.height_break:
                    self.full_height_bool.set(True)

    def change_size(self, *args):
        self.widget.pack_forget()
        # Max Widget
        if self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = MaxWidget(
                self,
                current_data=self.current_data,
                forcast_data=self.forcast_data,
                location=self.location,
                color=self.color,
                forcast_images=self.forcast_images,
                animation=self.today_animation,
            )

        # Tall Widget
        if self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = TallWidget(
                self,
                current_data=self.current_data,
                forcast_data=self.forcast_data,
                location=self.location,
                color=self.color,
                forcast_images=self.forcast_images,
                animation=self.today_animation,
            )

        # Wide Widget
        if not self.full_height_bool.get() and self.full_width_bool.get():
            self.widget = WideWidget(
                self,
                current_data=self.current_data,
                forcast_data=self.forcast_data,
                location=self.location,
                color=self.color,
                forcast_images=self.forcast_images,
                animation=self.today_animation,
            )

        # Small Widget
        if not self.full_height_bool.get() and not self.full_width_bool.get():
            self.widget = SmallWidget(
                self,
                self.current_data,
                self.forcast_data,
                self.location,
                self.color,
                self.today_animation,
            )


if __name__ == "__main__":
    # Location
    with urllib.request.urlopen("https://ipapi.co/json/") as url:
        data = json.loads(url.read().decode())
        city = data["city"]
        country = data["country_name"]
        latitude = data["latitude"]
        longitude = data["longitude"]

    # Weather information
    current_data = get_weather(latitude, longitude, "metric", "today")
    forcast_data = get_weather(latitude, longitude, "metric", "forcast")

    App(
        current_data=current_data, forcast_data=forcast_data, city=city, country=country
    )
