#Import
import selenium, bs4, time, requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

#Define URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

#List to store data
star_data = []

#Define function to scrape data
def scrape_data():
  page = requests.get(START_URL)
  soup = BeautifulSoup(page.text,'html.parser')
  star_table = soup.find_all("table")
  tbody = star_table[7].find_all("tbody")[0]
  i = 0
  for tr_tag in tbody:
    i += 1
    temp_list = []
    if i > 1:
      for index,td_tag in enumerate(tr_tag):
        try:
          if i == 5 and index == 1:
            text = td_tag.find_all("span")[0]
            text = text.text.strip()
            temp_list.append(text)
          else:
            text = td_tag.contents[0].text.strip()
            temp_list.append(text)
        except:
          print(end='\r')

      if temp_list != []:
        star_data.append(temp_list)
        
      time.sleep(0.01)
      print("scraping ....",end= '\r')



#call function
scrape_data()

#Feedback
print("Data scrapped.")

#Define headers
headers = ["Brown Dwarf", "Constellation", "Right ascension", "Declination",
            "App. Mag", "Distance(ly)", "Spectral Type", "Mass", "Radius", 
          "Discovery Year"]

#Define pandas DataFrame
data_frame = pd.DataFrame(star_data,columns=headers)

#Save as csv
data_frame.to_csv('data.csv',index=True,index_label=id)