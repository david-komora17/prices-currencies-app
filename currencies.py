import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def scrape_books():
    url = "https://books.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    product_data = []

    for book in books[:10]:
        title = book.h3.a["title"]

        price_text = book.find("p", class_="price_color").text

        # Remove currency symbol (£)
        price_gbp = float(price_text.replace("£", ""))

        product_data.append({
            "title": title,
            "price_gbp": price_gbp
        })
    return product_data


def get_exchange_rate(base_currency="GBP", target_currency="KES"):

    api_url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()

        data = response.json()

        rate = data["rates"][target_currency]

        return rate
    except requests.exceptions.RequestException as e:
        print(f"API Connection Error: {e}")
        return None

    except KeyError:
        print("Currency not found.")
        return None


def main():

    print("Scraping products...")

    products = scrape_books()

    if not products:
        print("No products found.")
        return

