def main():
    qty = None
    cost = None

def fetch_quantity():

    try:
        qty = int(input("Enter quantity: "))
        assert qty > 0
    except:
        print("Quantity cannot be negative or 0. Enter quantity again: ")
        qty = int(input())

    return qty

def fetch_cost():

    try:
        cost = int(input('Enter cost: '))
        assert cost > 0
    except:
        print("Cost cannot be negative. Enter cost again: ")
        cost = int(input())

    return cost

def compute_cost_per_quantity():
    
    qty = fetch_quantity()
    cost = fetch_cost()
    cost_per_quantity = cost/qty
    return cost_per_quantity

cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)