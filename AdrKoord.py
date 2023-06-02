from geopy.geocoders import Nominatim #Подключаем библиотеку

geolocator = Nominatim(user_agent="Tester") #Указываем название приложения (так нужно, да)
# adress = str(input('Введите адрес: \n')) #Получаем интересующий нас адрес
# location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса


def get_coordinates(adress):
    adresses=adress.split()
    # location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса

    location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса
    if location==None:
        return({"latitude":0.0,"longitude":0.0})
    return {"latitude":location.latitude,"longitude":location.longitude}
# print(location) #Выводим результат: адрес в полном виде
# print(location.latitude, location.longitude) #И теперь выводим GPS-координаты нужного нам адреса
