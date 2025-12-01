# 📊 Data Collection Project (Manual Data • API Fetch • Web Scraping)

This project demonstrates **three different methods** of collecting and storing data using Python:

1. **Manual Data Creation (CSV Generation)**
2. **API Data Fetching (Fake Store API)**
3. **Web Scraping (Books to Scrape Website)**

Each method generates a CSV file which can be used for analysis, ML models, dashboards, or further processing.

---

---

## 📝 1. Manual Data Creation

In this method, data is manually created using Python dictionaries and converted into a Pandas DataFrame.  
The dataset is then saved as a CSV file.

### ✔ Output File

`manual_data.csv`

### ✔ Purpose

- Understand DataFrames
- Practice saving data
- Learn basic data processing

---

---

## 🌐 2. API Data Fetching (Fake Store API)

This script fetches product data from the **Fake Store API**, a free public API for testing.

### ✔ Code Summary

- Loop through product API endpoints
- Extract: **title, price, category, rating**
- Store all products in a DataFrame
- Save to `product_data.csv`

### ✔ Output File

`product_data.csv`

### ✔ Concepts Covered

- HTTP GET requests
- JSON data handling
- Converting API data into CSV

---

---

## 🕸️ 3. Web Scraping (Books to Scrape)

This script scrapes book information from the website:  
👉 https://books.toscrape.com/

### ✔ Data Extracted

- **Book Title**
- **Price**
- **Availability Status**

### ✔ Tools Used

- `requests` — Fetch webpage HTML
- `BeautifulSoup` — Parse and extract content
- `pandas` — Build and save dataset

### ✔ Output File

`books_data.csv`

### ✔ scrape_books.py Overview

The script includes:

- `fetch_page()` → Downloads webpage HTML
- `parse_books()` → Extracts book data from HTML
- Saves results into a CSV file
- Displays a preview of the first 10 rows

---

---

# 📂 Final Project Structure
