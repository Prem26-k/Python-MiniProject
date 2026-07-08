employee = ["John", "Alice", "John", "Bob", "Alice"]
print("Employee:", employee)

duplicate = []

for i in employee:
    if employee.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print("Duplicate Employees:", duplicate)