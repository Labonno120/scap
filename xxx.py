import requests
from bs4 import BeautifulSoup
import csv

# Define the URL for the Daraz Bangladesh search page
url = 'https://www.daraz.com.bd/catalog/?_keyori=ss&clickTrackInfo=textId--8604400042594750176__abId--None__pvid--5a93ca2f-5295-4cd5-905e-8205f3683d87__matchType--1__abGroup--None__srcQuery--laptop__spellQuery--laptop__ntType--nt-common&from=suggest_normal&page=2&q=laptop&spm=a2a0e.tm80335401.search.2.7352xE8PxE8Pok&sugg=laptop_0_1'

headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', 
          'accept-language' : 'en-US,en;q=0.9',
          'Accept-Encoding':'gzip, deflate, br, zstd',
           'Accept':'*/*',
             'Referer': 'https://www.daraz.com.bd/' ,
               'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                'content-type': 'text/plain;charset=UTF-8',
'cookie':
'cna=TdthH/r4xj8CAWdyYLB39P69; sca=605914c5; atpsida=f4d0f15163cf9528c9999a66_1725648045_1',
'origin':
'https://www.daraz.com.bd',
'pragma':
'no-cache',
'priority':
'u=4, i' }
# Send an HTTP GET request to the URL
response = requests.get(url ,headers=headers)
print(response.text)
# Create/append to the CSV file
with open('product.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header row in CSV
    writer.writerow(["Product Name", "Price"])

    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Optional: Print the HTML for debugging
        # print(soup.prettify())

        # Find all product containers (update based on Daraz BD HTML structure)
        products = soup.find_all('div', class_='Bm3ON')  # Update based on inspection

        # Loop through product containers and extract name and price
        for item in products:
            # Extract product name (adjust class based on Daraz HTML structure)
            product_name = item.select_one('.RfADt')
            product_name = product_name.get_text() if product_name else "No name"

            # Extract product price (adjust class based on Daraz HTML structure)
            product_price = item.select_one('.ooOxS')
            product_price = product_price.get_text() if product_price else "No price"

            # Print the product name and price for debugging
            print(f"Product Name: {product_name}, Price: {product_price}")

            # Write data to CSV file
            writer.writerow([product_name, product_price])

        print("Data successfully written to product.csv")
    else:
        print(f"Failed to retrieve data from {url}, Status Code: {response.status_code}")
