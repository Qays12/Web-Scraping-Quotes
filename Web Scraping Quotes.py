import requests
from bs4 import BeautifulSoup

number = 1
term = "No quotes found!"
live_link = True

while live_link:
    response = requests.get(f"https://quotes.toscrape.com/page/{number}/")
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select(".text")

    authors = soup.select(".author")
    number += 1

    for quote, author in zip(quotes, authors):
        quote_text = quote.get_text()
        author_text = author.get_text(strip=True)
        print(f"Quote: {quote_text} By, {author_text}")

    if term in response.text:
        live_link = False
