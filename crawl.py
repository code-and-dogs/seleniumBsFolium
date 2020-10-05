from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from time import sleep
import csv

#Create a Chrome driver and crawl the URL
driver = webdriver.Chrome() 
driver.get('https://www.mcdonalds.com/de/de-de/restaurant-suche.html/l/berlin');

sleep(10) #give time for all javascripts to be finished running
page = driver.page_source
soup = BS(page, "lxml")

#Find restaurant list
content = soup.find('div', class_='uberfinder')
restaurantList = content.find_all('div', class_='ubsf_sitemap-location-address')

#Create dataset
with open('Restaurants.csv', mode='w', newline='') as outputFile:
    restaurantCSV = csv.writer(outputFile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    restaurantCSV.writerow(['restaurant', 'street', 'zip', 'city', 'country'])

    restaurantName = 'McDonalds'
    country = 'Germany'
    city = 'Berlin'
    for restaurant in restaurantList:
        street = restaurant.text.split(",")[0]
        zipCode = restaurant.text.split(",")[1][1:6]
        restaurantCSV.writerow([restaurantName, street, zipCode, city, country])
        
driver.close()
