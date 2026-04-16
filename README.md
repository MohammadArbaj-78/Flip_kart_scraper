# 📊 Flipkart Web Scraper (iPhone Data)

## 🚀 Project Overview

This project is a web scraper built using Python and Selenium to extract iPhone product data from Flipkart.

The scraper collects product details such as:

* Product Name
* Product Price

The extracted data is first saved as HTML files and then parsed into a structured CSV file.

---

## 🛠️ Technologies Used

* Python
* Selenium
* Undetected ChromeDriver
* BeautifulSoup
* Pandas

---

## ⚙️ How It Works

### Step 1: Scraping Data

* The script opens Flipkart search pages.
* It simulates human behavior (scrolling and mouse movement).
* It extracts product HTML blocks.
* Each product is saved as a separate `.html` file inside the `Scrape_Data` folder.

### Step 2: Parsing Data

* The parser reads all saved HTML files.
* Extracts product name and price using BeautifulSoup.
* Converts data into a structured format.
* Saves final output into a CSV file (`output.csv`).

---

## 📁 Project Structure

```
project-folder/
│
├── scraper.py
├── parser.py
├── Scrape_Data/
│   ├── 1.html
│   ├── 2.html
│   └── ...
├── output.csv
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install selenium undetected-chromedriver beautifulsoup4 pandas
```

### 2. Run Scraper

```bash
python scraper.py
```

### 3. Run Parser

```bash
python parser.py
```

---

## 📌 Features

* Anti-detection using Undetected ChromeDriver
* Random user-agents
* Human-like scrolling behavior
* Multi-page scraping
* Structured CSV output

---

## 📊 Output Example

| Name      | Price   |
| --------- | ------- |
| iPhone 14 | ₹70,000 |
| iPhone 13 | ₹60,000 |

---

## ⚠️ Notes

* Website structure may change, so selectors may need updates.
* Use responsibly and follow website terms.

---

## 💼 Use Case

This project demonstrates:

* Web scraping automation
* Data extraction from e-commerce websites
* Data cleaning and structuring

---

## 📬 Contact

If you need any web scraping or data extraction project, feel free to reach out.

---
