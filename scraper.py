from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.penguinrandomhouse.com/the-read-down/21-books-youve-been-meaning-to-read').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('book_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline'])

for article in soup.find_all('div', class_='list-meta-wrap'):
    headline = article.div.text
    print(headline)

    csv_writer.writerow([headline])

csv_file.close()
