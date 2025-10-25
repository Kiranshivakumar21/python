quantity = int(input("Enter the quantity purchased: "))
cost_per_item = float(input("Enter cost per item: "))

total_cost = quantity * cost_per_item

if total_cost > 1000:
    discount = 0.10 * total_cost
    total_cost -= discount

print("Total cost for user:", total_cost)
