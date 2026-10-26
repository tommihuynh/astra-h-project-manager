import json

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


def calculate_total_cost(parts):
    return  sum(part["price"] for part in parts )

def calculate_remaining_budget(budget, total_cost):
    return budget- total_cost

def display_parts(parts):
    for part in parts:
        print(
            f'{ part["name"] } |'
            f'{ part["price"] } EUR |'
            f'{ part["category"] } |'
            f'{ part["status"] }'
        )

def add_part(parts, part):
    return parts.append(part)


def save_parts(parts):
    with open("parts.json", "w") as file:
        json.dump(parts, file)


def load_parts():
    with open("parts.json", "r") as file:
        parts = json.load(file)
    return parts


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

new_part= {
    "name": "Sport steering wheel ",
    "price": 40,
    "category": "Body",
    "status": "Planned"

}

parts = load_parts()

add_part(parts, new_part)

save_parts(parts)

new_lists = load_parts()

print()
print("\n--- Stage 1 Parts ---")
display_parts(new_lists)


total_cost = calculate_total_cost(new_lists)
remaining = calculate_remaining_budget(project_budget,total_cost)
print("Total planned cost:", total_cost, "EUR")
print("Remaining cost:", remaining, "EUR")
