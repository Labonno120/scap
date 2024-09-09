from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import openpyxl

# Path to ChromeDriver (Update this to your actual ChromeDriver path)
chrome_driver_path = "C:/Users/Gs/chromedriver-win32/chromedriver.exe"

# Initialize ChromeDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Create an Excel workbook to store the scraped data
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Product Name", "Product Price", "Product Review"])

# Function to scrape product data from the current page
def scrape_page():
    # Find product containers (Adjust this based on actual class names)
    product_divs = driver.find_elements(By.CLASS_NAME, "Bm3ON")

    # Loop through each product
    for product in product_divs:
        try:
            product_name = product.find_element(By.CLASS_NAME, "RfADt").text
        except:
            product_name = "No name"

        try:
            product_price = product.find_element(By.CLASS_NAME, "ooOxS").text
        except:
            product_price = "No price"

        try:
            product_review = product.find_element(By.CLASS_NAME, "qzqFw").text
        except:
            product_review = "No review"

        # Append the data to the Excel file
        ws.append([product_name, product_price, product_review])

# Loop through multiple pages
for page in range(1, 4):  # Adjust the range based on the number of pages you want to scrape
    page_url = f"https://www.daraz.com.bd/catalog/?page={page}&q=laptop"
    driver.get(page_url)

    # Wait for the page to load
    time.sleep(2)

    # Scrape the current page
    scrape_page()

# Save the Excel file
wb.save("darazbd_scraped.xlsx")

# Close the browser
driver.quit()

print("Scraping completed. Data saved to darazbd_scraped.xlsx")
