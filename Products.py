products = [
        {"Product name": "Gaming Console", "Price": 2500, "Discount": "5%", "Category": "Video Games", "Stock": 10},
        {"Product name": "Shampoo", "Price": 6, "Discount": "0%", "Category": "Personal Care", "Stock": 7},
        {"Product name": "Smartphone", "Price": 7600, "Discount": "20%", "Category": "Electronics", "Stock": 50},
        {"Product name": "Laptop", "Price": 65000, "Discount": "20%", "Category": "Electronics", "Stock": 99},
        {"Product name": "Book", "Price": 750, "Discount": "5%", "Category": "Books", "Stock": 20},
]

for product in products:
    print(f"Product: {product['Product name']} | Price:{product['Price']} | Discount:{product['Discount']} | Catergory:{product['Category']} | Stock:{product['Stock']}")