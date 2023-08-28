# а) Получить погоду в Астане с статического сайта погоды, используя string.split()
# б) Получить погоду в Астане с статического сайта погоды, используя bs4


# import requests

# city = "Astana,KZ"
# url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
# response = requests.get(url)
# print(response.status_code)
#
# txt = "weather.html"
# with open(txt, 'wb') as f:
#     f.write(response.content)
#     f.close()
#
# data = response.json()
# print("Температура в Астане: {}°C".format(data["main"]["temp"]))




import requests
from bs4 import BeautifulSoup


url = "https://www.bbc.com/weather/1526273"
response = requests.get(url)
text = BeautifulSoup(response.text, "html.parser")
print(response.status_code)

a = "my_file.html"
with open(a, 'wb') as f:
    f.write(response.content)
    f.close()


temp = text.find('span', {'class': 'wr-value--temperature--c'}).text

print(f"Temperature in Astana: {temp}")
