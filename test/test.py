from datetime import date


class Get_Data:
    def __init__(self):
        self.date = date.today()
        self.year = date.today().year
        self.get_holiday_instance = Get_Holiday()
        self.get_weather_instance = Get_Weather()

    def get_holiday(self):
        self.get_holiday_instance.get_holiday()

    def get_weather(self):
        self.get_weather_instance.get_weather()


class Get_Holiday(Get_Data):
    def __init__(self) -> None:
        super().__init__()

    def get_holiday(self):
        print("Mengakses metode get_holiday dari Get_Holiday", self.date)


class Get_Weather:
    def get_weather(self):
        print("Mengakses metode get_weather dari Get_Weather")


data = Get_Data()
data.get_holiday()  # Mengakses metode get_holiday dari Get_Holiday
data.get_weather()  # Mengakses metode get_weather dari Get_Weather

