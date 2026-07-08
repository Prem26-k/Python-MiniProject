months = ["January", "February", "March", "April", "May", "June"]
sales = [25000, 32000, 28000, 35000, 40000, 37000]

print("------ Monthly Sales Report ------")

total_sales = 0

for i in range(len(months)):
    print(months[i], ":", sales[i])
    total_sales += sales[i]

print("----------------------------")
print("Total Sales:", total_sales)
print("Average Sales:", total_sales / len(sales))
print("Highest Sales:", max(sales))
print("Lowest Sales:", min(sales))