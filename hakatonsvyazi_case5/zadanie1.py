from dadata import Dadata
import geocoder
from geopy.geocoders import Nominatim
from config import *
import random

dadata = Dadata(TOKEN_DADATA)


# Функция получения текущих координат пользователя
def your_coordinates() -> list:
    return geocoder.ip('me').latlng


# Функция получения ближайших почтовых отделений
def get_post_offices(latitude: float, longitude: float, radius_meters: int) -> list:
    post_offices = []
    results = dadata.geolocate("address", latitude, longitude, radius_meters)
    for result in results:
        post_offices.append(result['data']['postal_code'])
    return post_offices


# Из индекса в адрес почтового отделения
def decode_index(index: int | str) -> str:
    return dadata.find_by_id("postal_unit", index)[0]['data']['address_str']


# Получение данных от пользователя
userKey: int = random.randint(0, 10000)
my_file = open("posts/postOffice" + str(userKey) + ".txt", "w+")
print("Здравствуйте! Эта программа находит ближайшие отделения Почты России по координатам и радиусу.")
print("Пожалуйста, введите координаты через запятую или введите 1, чтобы ввести ваши текущие координаты (yчтите, что текущие координаты получаются из вашего IP-адреса, поэтому они не самые точные):")
input_data: str = input()
coordinates: list = []
if input_data != "1":
    coordinates = input_data.split(",")
else:
    coordinates = your_coordinates()
print("Пожалуйста, введите радиус, вокруг которого вы хотите получить ближайшие почтовые отделения. Если радиус не "
          "имеет значения, введите 0:")
radius: int = int(input())
dates: list = get_post_offices(coordinates[0], coordinates[1], radius)
dates = list(set(dates))
for data in dates:
    print("Найдено отделение с индексом " + data + " по следующему адресу: " + decode_index(data))
    my_file.write("Найдено отделение с индексом " + data + " по следующему адресу: " + decode_index(data))
print("Поиск отделений завершен. Вы можете также посмотреть найденные отделения в папке posts в файле postOffice" + str(userKey) + ".txt")

