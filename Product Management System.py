products = {
    101: {"pname": "laptop", "category": "electronics", "price": 50000, "stock": 20},
    102: {"pname": "mouse", "category": "electronics", "price": 10000, "stock": 30},
    103: {"pname": "keyboard", "category": "electronics", "price": 20000, "stock": 10}
}


def add_product():

    pid = int(input("Enter the product id: "))
    if pid in products:
        print("ID already exists")
    else:
        pname = input("Enter the product name: ")
        category = input("Enter the category: ")
        price = int(input("Enter the price: "))
        stock = int(input("Enter the stock: "))
        products[pid] = {
            "pname": pname,
            "category": category,
            "price": price,
            "stock": stock
        }
        print("Product added successfully")


def update_stock():

    pid = int(input("Enter the product id: "))
    if pid in products:
        new_stock = int(input("Enter the new stock: "))
        products[pid]["stock"] = products[pid]["stock"] + new_stock
        print("Stock updated successfully")
    else:
        print("Product not found")


def change_price():

    pid = int(input("Enter the product id: "))
    if pid in products:
        new_price = int(input("Enter the new price: "))
        products[pid]["price"] = new_price
        print("Price updated successfully")
    else:
        print("ID does not exist")


def search_product():

    pid = int(input("Enter the product id: "))
    if pid in products:
        pname = products[pid]["pname"]
        category = products[pid]["category"]
        price = products[pid]["price"]
        stock = products[pid]["stock"]
        print(f"""
        Product ID   : {pid}
        Product Name : {pname}
        Category     : {category}
        Price        : {price}
        Stock        : {stock}
        """)
    else:
        print("Product not found")


def display_all_products():

    print("-" * 105)
    print(
        f"|{'pid':^20}|{'pname':^20}|{'category':^20}|{'price':^20}|{'stock':^20}|"
    )
    print("-" * 105)
    for pid, product in products.items():
        print(
            f"|{pid:^20}|"
            f"{product['pname']:^20}|"
            f"{product['category']:^20}|"
            f"{product['price']:^20}|"
            f"{product['stock']:^20}|"
        )
        print("-" * 105)


# ---------------- ORDERS ----------------

orders = { 1001: {
              "cname": "bhumika",
              "product": {101: 2, 102: 3}}}

def add_order():

    if len(orders) > 0:
        order_id = max(orders) + 1
    else:
        order_id = 1001
    cname = input("Enter customer name: ")
    display_all_products()
    product = {}
    while True:
        pid = int(input("Enter product id: "))
        if pid not in products:
            print("Product ID not found")
            continue
        qn = int(input("Enter quantity: "))
        if qn <= 0:
            print("Quantity must be greater than 0")
            continue
        if products[pid]["stock"] >= qn:
            product[pid] = qn
            products[pid]["stock"] -= qn
            print("Product added to order")
        else:
            print("Not enough stock")
            continue
        ch = input("Do you want to add another product? (yes/no): ")
        if ch.lower() == "no":
            break
    orders[order_id] = {
        "cname": cname,
        "product": product
    }
    print("Order added successfully")
    print("Order ID:", order_id)


def cancel_order():
    order_id = int(input("Enter the order id: "))
    if order_id in orders:
        order_product = orders[order_id]["product"]
        for pid in order_product:
            qn = order_product[pid]
            products[pid]["stock"] += qn
        del orders[order_id]
        print("Order cancelled successfully")
    else:
        print("Order ID not found")


def bill():

    order_id = int(input("Enter the order id: "))
    if order_id in orders:
        customer_name = orders[order_id]["cname"]
        total = 0
        print("""
================================
          CUSTOMER BILL
================================
""")

        print("Order ID      :", order_id)
        print("Customer Name :", customer_name)
        print("--------------------------------")
        print("Product       Quantity    Price")
        print("--------------------------------")
        for pid, qn in orders[order_id]["product"].items():

            pname = products[pid]["pname"]
            price = products[pid]["price"]
            amount = qn * price
            total += amount
            print(f"{pname:<15}{qn:<12}{price}")
        print("--------------------------------")
        print("Total Amount :", total)
        print("================================")
    else:
        print("Order ID not found")


# ---------------- MENU ----------------

def menu():

    while True:
        print("""
==============================================
          PRODUCT MANAGEMENT SYSTEM
==============================================

1. Add Product
2. Update Stock
3. Change Price
4. Search Product
5. Display All Products
6. Add Order
7. Cancel Order
8. Generate Bill
9. Exit

==============================================
""")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_product()

        elif choice == 2:
            update_stock()

        elif choice == 3:
            change_price()

        elif choice == 4:
            search_product()

        elif choice == 5:
            display_all_products()

        elif choice == 6:
            add_order()

        elif choice == 7:
            cancel_order()

        elif choice == 8:
            bill()

        elif choice == 9:
            print("Thank you!")
            break

        else:
            print("Invalid choice")
menu()