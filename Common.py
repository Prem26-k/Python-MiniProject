customer1 = ["Laptop", "Mouse", "Keyboard"]
customer2 = ["Mouse", "Monitor", "Keyboard"]

common_products = []

for product in customer1:
    if product in customer2:
        common_products.append(product)

print("Common Products:", common_products)