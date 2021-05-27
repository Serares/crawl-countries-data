import json
from warnings import catch_warnings
from selenium import webdriver
import pandas as pd

driver = webdriver.Firefox(executable_path= './geckodriver.exe')

def main():
    # with open('./cScraper/getTableData.js') as scripFile:
    #     script = scripFile.read()
    # dict of tuples
    countriesDict = {} 
    driver.set_window_size(800, 600)
    driver.get('https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita')
  
    driver.implicitly_wait(1)

    gdpPerCapitaTable = driver.find_elements_by_css_selector(".mw-parser-output > table:nth-child(14) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > table:nth-child(1) > tbody:nth-child(2) tr")
    for row in gdpPerCapitaTable:
        # print(row.find_elements_by_css_selector("tr"))
        try:
            countriesDict[row.find_element_by_css_selector("td:nth-child(1) > a").text] = [row.find_element_by_css_selector("td:nth-child(2)").text]
        except:
            print("Can't get country data")


    driver.get('https://www.worldometers.info/demographics/life-expectancy/')

    lifeExpectencyTable = driver.find_elements_by_css_selector("#example2 > tbody:nth-child(2) tr")

    for row in lifeExpectencyTable:
        try:
            countriesDict[row.find_element_by_css_selector("td:nth-child(2) > a").text].append(row.find_element_by_css_selector("td:nth-child(5)").text)
            countriesDict[row.find_element_by_css_selector("td:nth-child(2) > a").text].append(row.find_element_by_css_selector("td:nth-child(4)").text)
        except:
            print("Can't get country data")


    countriesDataFrame = pd.DataFrame.from_dict(countriesDict, orient="index", columns=["gdpPerCapita","maleLifeExpectancy", "femaleLifeExpectancy"])

    print(countriesDataFrame)
    driver.quit()




if __name__ == '__main__':
    main()
