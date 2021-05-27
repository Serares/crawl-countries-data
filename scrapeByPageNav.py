from os import times
import requests
from selenium import webdriver
import time

def main():
    with open('getMovieDetails.js') as f:
         script = f.read()
    baseUrl = 'https://www.themoviedb.org/'
    driver = webdriver.Firefox(executable_path = './geckodriver.exe')
    driver.set_window_size(800, 600)
    driver.get(baseUrl)
    moviesDetails = [];
    container = driver.find_elements_by_css_selector('a[class="image"]')
    
    for image in container:
        image.click()
        movieDetails = driver.execute_script(script)
        moviesDetails.append(movieDetails)
        driver.back()
    
    print(moviesDetails)
    driver.quit()

if __name__ == "__main__":
    main()