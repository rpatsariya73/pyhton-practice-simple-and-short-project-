store = {}
cart = []

def add_an_item_to_store(name,price):
    store[name] = price

def add_to_cart(item_name,quantity):
    if item_name in store:
        cart.append({"item":item_name,"qty":quantity,"price":store[item_name]})
        return "added to cart"
    else:
        return "item not found"
    
def calculate_bill():
    total = 0

    for item in cart:
        total = total+item["qty"]*item["price"]

        discount = 0
        if total> 1000:
            discount = total*0.10
            total = total - discount

        return total, discount

def print_bill():
    print("\n-------Bill--------")
    for item in cart :
        name = item["item"]
        qty = item["qty"]
        price = item["price"] 
        print(f"{name} ({qty} *Rs {price}) = Rs{qty * price}")

        total,discount = calculate_bill()

        print("---------------------------")
        print(f"discount: Rs{discount}")
        print(f"Final Total: Rs{total}")
        print('----------------------------')   

add_an_item_to_store("milk",50)
add_an_item_to_store("bread",30)
add_an_item_to_store("rice",70)
add_an_item_to_store("oil",150)

print(add_to_cart("milk",2))
print(add_to_cart("rice",5))
print(add_to_cart("oil",1))

print_bill ()