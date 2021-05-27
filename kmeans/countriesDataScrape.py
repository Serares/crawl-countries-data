import json
from selenium import webdriver
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

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
            countryGdp = float(row.find_element_by_css_selector("td:nth-child(2)").text.replace(',',''))
            countryName = row.find_element_by_css_selector("td:nth-child(1) > a").text
            countriesDict[row.find_element_by_css_selector("td:nth-child(1) > a").text] = [countryName, countryGdp]
        except:
            print("Can't get country data")


    driver.get('https://www.worldometers.info/demographics/life-expectancy/')

    lifeExpectencyTable = driver.find_elements_by_css_selector("#example2 > tbody:nth-child(2) tr")

    for row in lifeExpectencyTable:
        try:
            femaleLifeExpectancy = float(row.find_element_by_css_selector("td:nth-child(4)").text.replace(',',''))
            maleLifeExpectancy = float(row.find_element_by_css_selector("td:nth-child(5)").text.replace(',',''))
            countriesDict[row.find_element_by_css_selector("td:nth-child(2) > a").text].append(maleLifeExpectancy)
            countriesDict[row.find_element_by_css_selector("td:nth-child(2) > a").text].append(femaleLifeExpectancy)
        except:
            print("Can't get country data")


    for country in list(countriesDict):
        if(len(countriesDict[country]) < 3):
            countriesDict.pop(country, None)

    countriesDataFrame = pd.DataFrame.from_dict(countriesDict, orient="index", columns=["country","gdpPerCapita","maleLifeExpectancy", "femaleLifeExpectancy"])

    print(countriesDataFrame)
    clusterData(countriesDataFrame)
    driver.quit()

def clusterData(dataFrame):
    x = dataFrame.iloc[:, [1,2]].values

    # gasirea numarului de clustere
    list = []
    for i in range(1, 11):
        km = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
        km.fit(x)
        list.append(km.inertia_)

    plt.plot(range(1, 11), list)
    plt.title('Metoda Elbow')
    plt.xlabel('Număr de clustere')
    plt.ylabel('within cluster sum of squares')
    plt.show()
    
    # antrenam modelul K-means pe setul de date folosind 3 clustere
    coeficienti = []
    km = KMeans(n_clusters= 3, init = 'k-means++', random_state = 42)
    y_kmeans = km.fit_predict(x)
    score = silhouette_score(x, km.labels_)
    coeficienti.append(score)
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = 'sub dezvoltate')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'mediu-dezvoltate')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = 'dezvoltate')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroizi')
    plt.title('Clustere pentru tari')
    plt.xlabel('PIB PER CAP DE LOCUITOR')
    plt.ylabel('SPERANTA DE VIATA')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
