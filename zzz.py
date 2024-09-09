from bs4 import BeautifulSoup
import openpyxl

# Read the daraz.html file
with open('daraz2.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active

# Set the header row in the Excel file
#ws.append(["Product Name", "Product Price", "Product Review"])

# Find all divs with class 'Bm3ON'
product_divs = soup.find_all('div', class_='Bm3ON')

# Loop through each product div
for product in product_divs:
    # Try to find the product name
    try:
        product_name = product.find('div', class_='RfADt').get_text(strip=True)
    except AttributeError:
        product_name = " "

    # Try to find the product price
    try:
        product_price = product.find('span', class_='ooOxS').get_text(strip=True)
    except AttributeError:
        product_price = " "

    # Try to find the product review
    try:
        product_review = product.find('span', class_='qzqFw').get_text(strip=True)
    except AttributeError:
        product_review = " "

    # Write the product data to the Excel sheet
    ws.append([product_name, product_price, product_review])

# Save the workbook as an Excel file
wb.save('darazbd.xlsx')

print("Data has been written to darazbd.xlsx")
