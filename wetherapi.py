#!/usr/bin/python3
#******************************************************************************************************
# .This is the script to grab the Weather Information using open wethermap api
# .This mainly contains 3 modules
# .First module checks that wether internet connection is active or not
# .Second module gets the latitude and longitude of your location
# .Third module which grabs the weather information based on our latitude and longitude and some printing stuff
# .GUI version for this is comming soon.......
# .****Guru Bhat****
#******************************************************************************************************
import geocoder
import requests
#******************Colors********************************************
headers = '\033[95m'
okblue = '\033[94m'
okgreen = '\033[92m'
warning = '\033[93m'
fail = '\033[91m'
endc = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'

#********************checks for internet connection****************************************************
def CheckInet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        # print("internet_is_"+okgreen+"active"+endc)
        return 1
    except requests.ConnectionError:
        # print(fail+"No internet connection available."+endc)
        return 0

#**********************wil get lattitude and langitude if internet is active***************************
def get_latlng():
    myloc = geocoder.ip('me')
    lat,lng = myloc.latlng
    return lat, lng
#***********************grabs the weather Information from wether API**********************************
#******replace "xxxx" with your open weathermap api key at line 44 below*******************************
def get_weatherdata():
    internet = CheckInet()
    if internet == 1:
        cur_lat, cur_lon = get_latlng()
        url = "http://samples.openweathermap.org/data/2.5/weather?lat="+str(cur_lat)+"&lon="+str(cur_lon)+"&appid=xxxxxxxxxxxxxxxxxxxxxxx"
        req = requests.get(url)
        weather_data = req.json()
        temp = weather_data['main']['temp']
        temprature = temp/10
        wind_speed = weather_data['wind']['speed']
        latitude = weather_data['coord']['lat']
        longitude = weather_data['coord']['lon']
        description = weather_data['weather'][0]['description']
        print(headers+"*******************Weather Information*******************"+endc)
        print()
        print(okblue+"Tempature\t:"+"\t"+endc+okgreen+str(temprature)+endc+"\t"+fail+"degree celcius"+endc)
        print(okblue+"Wind Speed\t:"+"\t"+endc+okgreen+str(wind_speed)+endc+"\t"+fail+"m/s"+endc)
        print(okblue+"Latitude\t:"+"\t"+endc+okgreen+str(latitude)+endc)
        print(okblue+"Longitude\t:"+"\t"+endc+okgreen+str(longitude)+endc)
        print(okblue+"Description\t:"+"\t"+endc+okgreen+str(description)+endc)
        print()
        print(headers+ "************************"+endc+okgreen+"Guru Bhat"+endc+headers+"***********************" + endc)
    else:
        print(fail + "Check Your Internet Connection" + endc)

def main():
    get_weatherdata()
if __name__ == '__main__':
    main()
