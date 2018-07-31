import requests
from bs4 import BeautifulSoup

# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
# The article is long, so it is split up between 4 pages.
# Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.


def main():
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    contents = soup.find_all(class_="content-section")
    for content in contents:
        print(content.get_text())


if __name__ == '__main__':
    main()
