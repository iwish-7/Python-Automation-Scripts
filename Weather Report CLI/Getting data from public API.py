import requests

base_url = "https://wttr.in"

def getW(city):
    url = f"{base_url}/{city}?format=j1"
    req = requests.get(url)

    if req.status_code == 200:
        WD = req.json()
        return WD
    else:
        print("Error")


city = input("Enter the city name: ")
Weather_info = getW(city)

print(Weather_info.keys())

info = input("Enter any one info from above: ")
if Weather_info:
    print(f'{Weather_info[f'{info}']}')