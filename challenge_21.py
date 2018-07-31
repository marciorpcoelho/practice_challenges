import requests
from bs4 import BeautifulSoup

# Take the code from the How To Decode A Website exercise and instead of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.

# Extras:
# Ask the user to specify the name of the output file that will be saved.


def main():
    save_name = input('What is the name to save the file under? ')

    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')

    contents = soup.find_all(class_="content-section")
    with open(save_name + '.txt', 'w') as open_file:
        for content in contents:
            open_file.write(content.get_text())


if __name__ == '__main__':
    main()
