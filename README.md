# Bakery-Management-System
Here Is The Bakery Management System(BMS) that I made using Python.
I have added only few inventories list. You can add as many as you want.

## Explanation:

* Product Class (Product):
  Represents a bakery product with name, price, and stock.
* display_inventory:
Displays available bakery items with their prices and stock levels.
* take_order:
Allows the customer to select items and quantities from the inventory.
Reduces the stock of selected items accordingly.
Optionally allows adding comments to the order.
* calculate_bill:
Calculates the total bill based on the selected items and quantities.
Displays the order details and the total amount.
* generate_qr:
Generates a QR code containing order details and saves it as a PNG file in a qr_codes folder.
* main:  
  The main program flow:  
  Prompts the user for their name.  
   Takes the order using take_order.  
   If an order is placed (if order:), calculates the bill using calculate_bill.  
   Generates a QR code summarizing the order details using generate_qr.  


## To run this program:

```
Ensure you have the required libraries (qrcode) installed (pip install qrcode).
Replace the sample inventory with your actual bakery products.
Run the script, and it will guide you through the ordering process. After placing the order, a QR code will be generated containing the order details.




