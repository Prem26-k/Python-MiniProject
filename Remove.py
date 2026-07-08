customer_ids = [101, 102, 103, 101, 104, 102]
print("Customer IDs:", customer_ids)

unique_customers = []

for customer in customer_ids:
    if customer not in unique_customers:
        unique_customers.append(customer)

print("After Removing Duplicates:", unique_customers)