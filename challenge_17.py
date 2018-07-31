import requests
from bs4 import BeautifulSoup
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.


def main():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html5lib')

    titles = soup.find_all(class_='story-heading')
    for title in titles:
        print(title.get_text().strip())


if __name__ == '__main__':
    main()
