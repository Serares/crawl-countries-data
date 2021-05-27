import requests
from selenium import webdriver
import time
from sklearn.preprocessing import LabelEncoder
import json

def main():
    with open('getMovieDetails.js') as f:
         script = f.read()
    baseUrl = 'https://www.worldometers.info/coronavirus/'
    driver = webdriver.Firefox(executable_path = './geckodriver.exe')
    driver.set_window_size(800, 600)
    driver.get(baseUrl)
    rows_numbers = 0

    for 
    container = driver.find_elements_by_css_selector('#main_table_countries_today > tbody:nth-child(2) > tr:nth-child(7) > td:nth-child(5)')
    
    for image in container:
        image.click()
        movieDetails = driver.execute_script(script)
        moviesDetails.append(movieDetails)
        driver.back()
    
    print(moviesDetails)
    driver.quit()
    

if __name__ == "__main__":
    main()