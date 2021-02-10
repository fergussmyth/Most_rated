from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.penguinrandomhouse.com/the-read-down/21-books-youve-been-meaning-to-read').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div', class_='list-meta-wrap'):
    headline = article.div.a.text
    print(headline)

for name in soup.find_all(class_='author'):
    author = name.text
    print(author)

for notes in soup.find_all(class_='desc'):
    description = notes.text
    print(description)
