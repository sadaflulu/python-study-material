cart=[]
while True:
    print(".........shopping cart.........")
    print("1.Add items")
    print("2.view cart")
    print("3.Rename items")
    print("4.sort cart")
    print("5.Exit")
    choice=input("enter your choice:-")
    if choice == "1":
        item=input ("enter your item name:-")
        cart.append(item)
        print(cart,"added to the cart")
    elif choice == "2":
        for i in cart:
            print(i)
        
    
