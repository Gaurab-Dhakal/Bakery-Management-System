import datetime
import os
import qrcode

# Define product class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Function to display available products
def display_inventory(inventory):
    print("-" * 50)
    print("Available Bakery Items:")
    print("-" * 50)
    print("{:<20s}{:>10s}{:>10s}".format("Name", "Price", "Stock"))
    print("-" * 50)
    for product in inventory:
        print("{:<20s}{:>10.2f}{:>10d}".format(product.name, product.price, product.stock))
    print("-" * 50)

# Function to take order
def take_order(inventory):
    order = {}
    comments = ""
    while True:
        display_inventory(inventory)
        product_name = input("Enter product name (or 'q' to quit): ").lower()
        if product_name == 'q':
            break
        found = False
        for product in inventory:
            if product.name.lower() == product_name:
                quantity = int(input(f"Enter quantity for {product.name}: "))
                if quantity <= product.stock:
                    order[product.name] = quantity
                    product.stock -= quantity
                    found = True
                    break
                else:
                    print(f"Insufficient stock for {product.name}. Available stock: {product.stock}")
                    found = True
                    break
        if not found:
            print("Product not found.")

    comments = input("Add any comments to your order (optional): ")
    return order, comments

# Function to calculate bill
def calculate_bill(order, inventory):
    total = 0
    print("\nYour Order:")
    print("-" * 50)
    print("{:<20s}{:>10s}{:>10s}".format("Name", "Price", "Quantity"))
    print("-" * 50)
    for product_name, quantity in order.items():
        for product in inventory:
            if product.name == product_name:
                item_price = product.price
                total += item_price * quantity
                print("{:<20s}{:>10.2f}{:>10d}".format(product_name, item_price, quantity))
    print("-" * 50)
    print(f"Total: {total:.2f}")
    return total

# Function to generate QR code with safe filename
def generate_qr(data, filename):
    filename = filename.replace(" ", "_").strip("_")
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")
    img.save(f"qr_codes/{filename}.png")
    print(f"QR code saved to qr_codes/{filename}.png")

# Main program
def main():
    # Sample inventory (replace with your actual data)
    inventory = [
        Product("Bread", 2.50, 10),
        Product("Cupcakes", 1.00, 15),
        Product("Cookies", 3.00, 8),
    ]

    # Prompt customer for name
    customer_name = input("Enter customer name: ")

    # Take order
    print("\nWelcome to the Bakery!")
    order, comments = take_order(inventory)

    if order:
        # Calculate bill
        bill_amount = calculate_bill(order, inventory)
        print("\nThank you for your order!")

        # Generate order data for QR code
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        order_data = f"Customer: {customer_name}\nDate & Time: {current_time}\nOrder: {order}\nComments: {comments}\nTotal: {bill_amount}"

        # Generate and save QR code
        generate_qr(order_data, f"{customer_name}_{current_time}")

if __name__ == "__main__":
    main()