cart = []

while True:
    print("===== SHOPPING CART SYSTEM =====")
    print("1. Add items")
    print("2. View cart")
    print("3. Remove from cart")
    print("4. Sort cart")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. Add items
    if choice == "1":
        item = input("Enter item name: ")
        cart.append(item)
        print(item, "added to cart successfully!")

    # 2. View cart
    elif choice == "2":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("Your shopping cart:")

            for index, item in enumerate(cart):
                print(index, ":", item)

            print("First item:", cart[0])
            print("Last item:", cart[-1])
            print("First two items:", cart[:2])

    # 3. Remove from cart
        

    # 4. Sort cart
    

    # 5. Exit

       
    
        
