import requests
from pyquery import PyQuery as pq

def main():
    headers = {
    'User-Agent': 'Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90',
    'From': 'jianurares14@stud.ase.ro'
    }
    baseUrl = 'https://www.themoviedb.org/'
    response = requests.get(baseUrl, headers=headers)
    html = response.text
    dom = pq(html)
    images = dom("img")
    for element in images:
        print(pq(element))


if __name__ == '__main__':
	main()
