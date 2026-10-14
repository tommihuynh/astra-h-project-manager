car_brand = "Opel"
car_model = "Astra H GTC"
car_year = 2008
engine = "Z16XER"
horsepower = 115


mileage = 182371
car_colour = "Black"
project_budget = 1000
project_cost = 250
remaining_budget = project_budget - project_cost

part_prices = [250, 180, 300]

parts = [ 
  {
    "name": "Suspension components",
    "price": 250,
    "category": "Suspension",
    "status": "Planned"
  },
  {
    "name": "Tyres",
    "price": 180,
    "category": "Tyres",
    "status": "Planned"
  },
  {
    "name": "Exhaust components",
    "price": 300,
    "category": "Exhaust",
    "status": "Researching"
  },
  {
    "name": "Brake components",
    "price": 120,
    "category": "Brake",
    "status": "Planned"
  }
]


print("Car:", car_brand, car_model)
print("Year:", car_year)
print("Engine:", engine)
print("Power:", horsepower, "HP")
print()

current_year = 2026
car_age = current_year - car_year

print("Car age:", car_age, "years")
print("Mileage:", mileage, "km")
print("Colour:", car_colour)
print("Project budget:", project_budget, "EUR")
print("Project cost:", project_cost, "EUR")
print("Remaining budget:", remaining_budget, "EUR")

print()
print("\n--- Stage 1 Parts ---")
print(part_prices)
print("First part price:", part_prices[0], "EUR")
print("Second part prices:", part_prices[1], "EUR")
print("Third part prices:", part_prices[2], "EUR")

part_prices.append(70)
print("Updated prices:", part_prices)

print("\n--- Part Suspension Details ---")
print("Name:", parts[0]["name"])
print("Price:", parts[0]["price"], "EUR")
print("Category:", parts[0]["category"])
print("Status:", parts[0]["status"])

print("\n--- Parts Inventory ---")
print(parts[0]["name"])
print(parts[1]["name"])
print(parts[2]["name"])

total_cost = (
    parts[0]["price"]
    + parts[1]["price"]
    + parts[2]["price"]
    + parts[3]["price"]
)
print("Total planned cost:", total_cost, "EUR")
