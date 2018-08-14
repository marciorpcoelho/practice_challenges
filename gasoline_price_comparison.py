import requests
import time
import sys
import pandas as pd
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(executable_path='C:\\Users\\mrpc\\AppData\\Roaming\\JetBrains\\PyCharm Community Edition 2018.1.2\\plugins\\chromedriver.exe')
pd.set_option('display.expand_frame_repr', False)
# driver.close()


# Possible configuration to make chrome window not open at all - https://stackoverflow.com/questions/16180428/can-selenium-webdriver-open-browser-windows-silently-in-background
# CHROME_PATH = '/usr/bin/google-chrome'
# CHROME_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application'
# CHROMEDRIVER_PATH = 'C:\\Users\\mrpc\\AppData\\Roaming\\JetBrains\\PyCharm Community Edition 2018.1.2\\plugins\\chromedriver.exe'
# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

# get list of stations in gaia
# get prices of each station
# show the lowest?

def main():
    start = time.time()
    postos_dict = gaia_stations_list()
    postos_price_gasoline_95_dict = price_retrieval(postos_dict)

    # print(postos_price_gasoline_95_dict)

    print('\nRunning time: %.2f' % (time.time() - start), 'seconds')


def gaia_stations_list():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    postos_link_list = []
    postos_name_list = []
    postos_dict = {}

    for i in range(1, 6):
        if i == 1:
            url = 'https://www.maisgasolina.com/lista-de-postos/porto/vila-nova-de-gaia/'
        else:
            url = 'https://www.maisgasolina.com/lista-de-postos/porto/vila-nova-de-gaia/' + str(i) + '/'

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html5lib')

        for link in soup.find_all('a'):
            link = link.get('href')
            if '/posto/' in link:
                postos_link_list.append(link)

        for name in soup.find_all(class_='name'):
            name = name.text.split('Actualizado a ')[0]
            postos_name_list.append(name.replace(',', '.'))

    for (names, links) in zip(postos_name_list, postos_link_list):
        postos_dict[names] = links

    postos_dict_new = station_removal(postos_dict)

    return postos_dict_new


def station_removal(postos_dict):
    # Station w/o Gasoline: 'BP - Mastergás'
    # Stations that exists on both sides of the road (which have the same prices): 'Galp Vasco da Gama -...Galp Vasco da Gama - Pedroso (N/S)', 'Galp Feiteira (N/S)', 'Galp - Gaia Arrábida N/S', 'Repsol A.S. Vilar Paraíso...Repsol A.S. Vilar Paraíso A (N/S)', 'Repsol - Vilar de...Repsol - Vilar de Andorinho (N/S)', 'BP - Valadares N/S', 'Repsol E.S. Gaia I (N/S)'

    stations_to_remove = ['BP - Mastergás', 'Galp Vasco da Gama -...Galp Vasco da Gama - Pedroso (N/S)', 'Galp Feiteira (N/S)', 'Galp - Gaia Arrábida N/S', 'Repsol A.S. Vilar Paraíso...Repsol A.S. Vilar Paraíso A (N/S)', 'Repsol - Vilar de...Repsol - Vilar de Andorinho (N/S)', 'BP - Valadares N/S', 'Repsol E.S. Gaia I (N/S)']
    for station in stations_to_remove:
        try:
            del postos_dict[station]
        except KeyError:
            continue

    # Station w/o Gasoline:
    # del postos_dict['BP - Mastergás']
    # Stations that exists on both sides of the road (which have the same prices):
    # del postos_dict['Galp Vasco da Gama -...Galp Vasco da Gama - Pedroso (N/S)']
    # del postos_dict['Galp Feiteira (N/S)']
    # del postos_dict['Galp - Gaia Arrábida N/S']
    # del postos_dict['Repsol A.S. Vilar Paraíso...Repsol A.S. Vilar Paraíso A (N/S)']
    # del postos_dict['Repsol - Vilar de...Repsol - Vilar de Andorinho (N/S)']
    # del postos_dict['BP - Valadares N/S']
    # del postos_dict['Repsol E.S. Gaia I (N/S)']

    return postos_dict


def price_retrieval(postos_dict):

    postos_price_gasoline_95_dict = {}

    for key in postos_dict:
        url = postos_dict[key]
        driver.get(url)

        elem = driver.find_elements_by_class_name("encoded")
        for element in [elem[0]]:
            postos_price_gasoline_95_dict[key] = float(element.text)
    driver.close()

    df = pd.DataFrame.from_dict(postos_price_gasoline_95_dict, orient='index')
    df.index.names = ['Stations']
    df.rename({0: 'Gasoline Price'}, axis=1, inplace=True)
    df.sort_values(by='Gasoline Price', inplace=True)
    df.to_csv('gasoline_prices_week_' + str(datetime.datetime.now().strftime('%W')) + '.csv')
    return postos_price_gasoline_95_dict


if __name__ == '__main__':
    main()
