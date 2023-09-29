from geopy.geocoders import Nominatim #Подключаем библиотеку
import requests
from database.kladr_base import *
from math import ceil
import rusyllab
geolocator = Nominatim(user_agent="Tester") #Указываем название приложения (так нужно, да)

def get_coordinates(adress):
    adresses=adress.split()
    # location = geolocator.geocode(adress) #Создаем переменную, которая состоит из нужного нам адреса

    location = geolocator.geocode(adress,language="RU",) #Создаем переменную, которая состоит из нужного нам адреса
    if location==None:
        return({"latitude":0.0,"longitude":0.0})
    return {"latitude":location.latitude,"longitude":location.longitude}

def search(request,type=None):

    parts=[]
    request=request.lower()
    parts=rusyllab.split_words([request])#делим слово на слоги


    session=make_session()
    if type!=None:
        cities=session.query(Settlement).filter(Settlement.Type==type).all()
    else:
        cities=session.query(Settlement).filter().all()

    match_procent=0
    biggest_match_procent=0
    best_option=0
    biggets_amount_of_matches=0
    for city in cities:#перебираем все города
        
        name=city.Name
        name=name.lower()#переводим все в нижний регистр
        number_of_parts=ceil(len(name)/2)#количество слогов в городе из бд

        if city==name:
            return city
        amount_of_matches=0#количество слогов, которое совпало
        word=""
        current_amount_of_matches=0
        for i in range(len(parts)):
            if word+parts[i] in name:
                word=word+parts[i]
                current_amount_of_matches+=1#определеям какое количество слогов совпадает
            else:
                word=""
                if current_amount_of_matches>amount_of_matches:
                    amount_of_matches=current_amount_of_matches
                current_amount_of_matches=0
        # if amount_of_matches==number_of_parts:#если все слоги совпадают, то сразу возвращаем этот город
        #     return city
        
        if amount_of_matches==0:#чтобы не было деления на 0
            continue

        match_procent=amount_of_matches/number_of_parts#число от 0 до 1, которое определяет процент совпадает    

        if amount_of_matches>biggets_amount_of_matches:#определяем наибольший проценнт совпадения и получаем нужный город
            best_option=city
            biggest_match_procent=match_procent
            biggets_amount_of_matches=amount_of_matches
    if biggest_match_procent>0.4:
        return best_option
    else:
        return None
    

def find_best_option(request):
    find_in_cities=search(request,"г")#пробуем с городами
    if find_in_cities!=None:
        return find_in_cities
    
    find_in_all_settlements=search(request=request)#если не вышло с городами- с деревнями
    return find_in_all_settlements
    

city=get_coordinates("Москва")

# print(city.Name)