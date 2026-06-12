import csv

people=[
  {"name":"Ahmed","service":"python","price":150,"status":"active"},
  {"name":"Mohammed","service":"JavaScript","price":200,"status":"inactive"},
  {"name":"yahya","service":"HTML","price":220,"status":"active"},
  {"name":"hussein","service":"C++","price":100,"status":"almost active"}
 ]

with open('people.csv', 'w', newline='',encoding="utf-8") as file:
    fieldnames=['name', 'service', 'price', 'status']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(people)
print("Part 1: CSV file created successfully.")

with open('people.csv', 'r',encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Part 2: All clients: ")
    for row in reader:
        print(f" {row['name']} | {row['service']} | {row['price']} | {row['status']}")

with open('people.csv', 'a',encoding="utf-8") as file:
    fn=["name", "service", "price", "status"]
    writer= csv.DictWriter(file, fieldnames=fn)

    added={"name": "ali", "service": "Python", "price": 120, "status": "active"}
    writer.writerow(added)

print("Part 3: New client added successfully.")

with open('people.csv', 'r',encoding="utf-8") as file:
    reader =csv.DictReader(file)
    rows=list(reader)

total_income = sum(int(row['price']) for row in rows if row['status'] == 'active')
pending_income = sum(int(row["price"]) for row in rows if row['status'] == 'inactive' or row['status'] == 'almost active')
almost_active = sum(1 for row in rows if row['status'] == "almost active")
total_clients= len(rows)

print(f"Part 4: Summary: ")
print(f"Total income: {total_income}")
print(f"Pending income: {pending_income}")
print(f"Almost active projects: {almost_active}")
print(f"All clients: {total_clients}")