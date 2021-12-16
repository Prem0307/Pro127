from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd 

bright_stars_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page=requests.get(bright_stars_url)
print(page)

soup=bs(page.text,'html.parser')
star_table=soup.find('table')
temp_list_star=[]

table_rows=star_table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list_star.append(row)

Star_names=[]
Distance=[]
Radius=[]
Mass=[]
Lum=[]

for i in range(1,len(temp_list_star)):
    Star_names.append(temp_list_star[i][1])
    Distance.append(temp_list_star[i][3])
    Radius.append(temp_list_star[i][5])
    Mass.append(temp_list_star[i][6])
    Lum.append(temp_list_star[i][7])

df=pd.DataFrame(list(zip(Star_names,Distance,Radius,Mass,Lum)),columns=['Star_names','Distance','Radius','Mass','Lumonsity'])
print(df)

df.to_csv('bright_stars.csv')
