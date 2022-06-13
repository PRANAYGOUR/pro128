from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests 

BrightStar_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(BrightStar_URL)
soup = bs(page.text , "html.parser")
star_table = soup.find_all("table")

temp_list = []

tableRows = star_table[7].find_all("tr")
for tr in tableRows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]

    temp_list.append(row)

star_name = []
star_distance = []
star_radius = []
star_mass = []

for i in range(1 , len(temp_list)):
    star_name.append(temp_list[i][0])
    star_distance.append(temp_list[i][5])
    star_mass.append(temp_list[i][7])
    star_radius.append(temp_list[i][8])
    

df2 = pd.DataFrame(list(zip(star_name,star_distance,star_mass,star_radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv("dwarf_Star.csv")