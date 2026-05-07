#  Price Scraper + Currency Converter

##  Project Overview

This project is a Python-based web scraping and data analysis tool that:

* Scrapes product (book) data from an e-commerce website
* Extracts product titles and prices
* Converts prices from one currency to another using a live exchange rate API
* Displays results in a clean table format
* Saves the data to a CSV file
* Visualizes prices using a bar chart

---

##  Data Source

This project scrapes data from:

* [https://books.toscrape.com/]

---

##  Features

* Web scraping using `requests` and `BeautifulSoup` 
* Extracts at least 10 products (books)
* Cleans product titles and prices
* Converts currency using a free exchange rate API
* Displays data using `pandas`
* Saves results to CSV file
* Adds timestamp for conversion time
* Visualizes original prices using `matplotlib`
* Handles connection and API errors

---

## Requirements

Install dependencies before running the project:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

>  Note: `tabulate` is optional and not required for this project.

---

##  How to Run

1. Clone or download the project
2. Navigate to the project folder
3. Run the script:

```bash
python currencies.py
```

---

##  Currency Conversion API

This project uses a free API:

[https://open.er-api.com/](https://open.er-api.com/)

Example endpoint:

```
https://open.er-api.com/v6/latest/GBP
```

✔ No API key required
✔ Supports major world currencies

---

##  Example Output

```
Book Title               Price (GBP)   Price (KES)
A Light in the Attic     51.77         8720.45
Tipping the Velvet       53.74         9051.23
```

---

##  Output Files

The program generates:

* `converted_book_prices.csv` → stored dataset

---

##  Visualization

A bar chart is generated using matplotlib showing:

* Book titles
* Original prices

---

##  Common Issues

### 1. Matplotlib lock error

Fix:

```
Delete file:
C:\Users\USER\.matplotlib\fontlist-v390.json.matplotlib-lock
```

---

### 2. Currency not found error

Cause:
Using invalid currency names like "dollar"

✔ Use correct codes:

* USD
* GBP
* KES
* EUR

---

##  Key Learnings

* Web scraping basics
* Data cleaning
* Working with APIs
* Currency conversion logic
* Using pandas DataFrames
* Data visualization

---

##  Author

Student Project – Python Web Scraping Assignment

---

##  License

For educational use only.
