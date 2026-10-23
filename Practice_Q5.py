# Q5
distance = float(input("Enter distance(km): "))
mileage = float(input("Enter mileage(km/litre):"))
price = float(input("Enter fuel price per litre: "))
cost = (distance / mileage) * price
print(f"Fuel Cost: Rs. {cost}")
