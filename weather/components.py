import customtkinter as ctk
import datetime, calendar
from image_widgets import *


class SimplePanel(ctk.CTkFrame):
    def __init__(self, parent, weather, col, row, color, animation):
        super().__init__(master=parent, fg_color=color["main"], corner_radius=0)
        self.grid(column=col, row=row, sticky="nsew")

        # Layout
        self.rowconfigure(0, weight=1, uniform="a")
        self.columnconfigure((0, 1), weight=1, uniform="a")

        # Widgets
        temp_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(
            temp_frame,
            text=f"{weather['temp']}\N{DEGREE SIGN}",
            font=ctk.CTkFont(family="calibri", size=50),
            text_color=color["text"],
        ).pack()
        ctk.CTkLabel(
            temp_frame,
            text=f"feels like: {weather['feels_like']}\N{DEGREE SIGN}",
            font=ctk.CTkFont(family="calibri", size=16),
            text_color=color["text"],
        ).pack()
        temp_frame.grid(row=0, column=0)

        AnimatedImage(self, animation, 0, 1, color["main"])


class DatePanel(ctk.CTkFrame):
    def __init__(self, parent, location, col, row, color):
        super().__init__(master=parent, fg_color=color["main"], corner_radius=0)
        self.grid(column=col, row=row, sticky="nsew")

        # Location
        location_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(
            location_frame,
            text=f"{location['city']}, ",
            font=ctk.CTkFont(family="calibri", size=20, weight="bold"),
            text_color=color["text"],
        ).pack(side="left")
        ctk.CTkLabel(
            location_frame,
            text=f"{location['country']}",
            font=ctk.CTkFont(
                family="calibri",
                size=20,
            ),
            text_color=color["text"],
        ).pack(side="left")
        location_frame.pack(side="left", padx=10)

        # Date
        day, weekday, suffix, month = get_time_info()
        ctk.CTkLabel(
            self,
            text=f"{weekday[:3]}, {day}{suffix} {calendar.month_name[month]}",
            font=ctk.CTkFont(family="calibri", size=20, weight="bold"),
            text_color=color["text"],
        ).pack(side="right", padx=10)


class HorizontalForcastPanel(ctk.CTkFrame):
    def __init__(
        self, parent, forcast_data, col, row, rowspan, divider_color, forcast_images
    ):
        super().__init__(master=parent, fg_color="#FFF")
        self.grid(column=col, row=row, rowspan=rowspan, sticky="nsew", padx=6, pady=6)

        # Widgets
        for i, info in enumerate(forcast_data.items()):
            frame = ctk.CTkFrame(self, fg_color="transparent")

            # Data
            year, month, day = info[0].split("-")
            weekday = list(calendar.day_name)[
                datetime.date(int(year), int(month), int(day)).weekday()
            ][:3]

            # Layout
            frame.columnconfigure(0, weight=1, uniform="a")
            frame.rowconfigure(0, weight=5, uniform="a")
            frame.rowconfigure(1, weight=2, uniform="a")
            frame.rowconfigure(2, weight=1, uniform="a")

            # Widgets
            StaticImage(frame, forcast_images[i], 0, 0)
            ctk.CTkLabel(
                frame,
                text=f"{info[1]['temp']}\N{DEGREE SIGN}",
                text_color="#444",
                font=("Calibri", 22),
            ).grid(row=1, column=0, sticky="n")
            ctk.CTkLabel(frame, text=weekday, text_color="#444").grid(row=2, column=0)
            frame.pack(side="left", expand=True, fill="both", padx=5, pady=5)

            if i < len(forcast_data) - 1:
                ctk.CTkFrame(self, fg_color=divider_color, width=2).pack(
                    side="left", fill="both"
                )


class SimpleTallPanel(ctk.CTkFrame):
    def __init__(self, parent, weather, location, col, row, color, animation):
        super().__init__(master=parent, fg_color=color["main"], corner_radius=0)
        self.grid(column=col, row=row, sticky="nsew")

        # Layout
        self.columnconfigure(0, weight=1, uniform="a")
        self.rowconfigure((0, 2, 4), weight=1, uniform="a")
        self.rowconfigure(1, weight=2, uniform="a")
        self.rowconfigure((3, 5), weight=6, uniform="a")

        # Data
        day, weekday, suffix, month = get_time_info()

        # Temperature
        temp_frame = ctk.CTkFrame(self, fg_color="transparent")
        ctk.CTkLabel(
            temp_frame,
            text=f"{weather['temp']}\N{DEGREE SIGN}",
            font=ctk.CTkFont(family="calibri", size=50),
            text_color=color["text"],
        ).pack()
        ctk.CTkLabel(
            temp_frame,
            text=f"feels like: {weather['feels_like']}\N{DEGREE SIGN}",
            font=ctk.CTkFont(family="calibri", size=16),
            text_color=color["text"],
        ).pack()
        temp_frame.grid(row=5, column=0)

        # Date
        info_frame = ctk.CTkFrame(self, fg_color="transparent")
        info_frame.columnconfigure(0, weight=1, uniform="a")
        info_frame.rowconfigure((0, 1), weight=1, uniform="a")
        info_frame.grid(row=1, column=0)

        ctk.CTkLabel(
            info_frame,
            text=f"{weekday[:3]}, {day}{suffix} {calendar.month_name[month]}",
            text_color=color["text"],
            font=("Calibri", 18),
        ).grid(column=0, row=1)

        # Location
        location_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        ctk.CTkLabel(
            location_frame,
            text=f"{location['city']}, ",
            font=ctk.CTkFont(family="calibri", size=20, weight="bold"),
            text_color=color["text"],
        ).pack(side="left")
        ctk.CTkLabel(
            location_frame,
            text=f"{location['country']}",
            font=ctk.CTkFont(
                family="calibri",
                size=20,
            ),
            text_color=color["text"],
        ).pack(side="left")
        location_frame.grid(column=0, row=0)

        # Animated imgage
        AnimatedImage(self, animation, 3, 0, color["main"])


class VerticalForcastPanel(ctk.CTkFrame):
    def __init__(self, parent, forcast_data, col, row, divider_color, forcast_images):
        super().__init__(master=parent, fg_color="#FFF")
        self.grid(column=col, row=row, sticky="nsew", padx=6, pady=6)

        # Widgets
        for i, info in enumerate(forcast_data.items()):
            frame = ctk.CTkFrame(self, fg_color="transparent")

            # Data
            year, month, day = info[0].split("-")
            weekday = list(calendar.day_name)[
                datetime.date(int(year), int(month), int(day)).weekday()
            ]

            # Layout
            frame.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
            frame.rowconfigure(0, weight=1, uniform="a")

            # Widgets
            StaticImage(frame, forcast_images[i], 0, 3)

            ctk.CTkLabel(
                frame,
                text=f"{info[1]['temp']}\N{DEGREE SIGN}",
                text_color="#444",
                font=("Calibri", 22),
            ).grid(row=0, column=2, sticky="e")
            ctk.CTkLabel(frame, text=weekday, text_color="#444").grid(
                row=0, column=0, sticky="e"
            )
            frame.pack(expand=True, fill="both", padx=5, pady=5)

            # Divider Line
            if i < len(forcast_data) - 1:
                ctk.CTkFrame(self, fg_color=divider_color, height=2).pack(fill="x")


def get_time_info():
    month = datetime.datetime.today().month
    day = datetime.datetime.today().day
    weekday = list(calendar.day_name)[datetime.datetime.today().weekday()]

    match day % 10:
        case 1:
            suffix = "st"
        case 2:
            suffix = "nd"
        case 3:
            suffix = "rd"
        case _:
            suffix = "th"

    return day, weekday, suffix, month
