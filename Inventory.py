class Product:
    def __init__(self, product_id, name, category, current_stock, reorder_point, reorder_quantity, lead_time):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.current_stock = current_stock
        self.reorder_point = reorder_point
        self.reorder_quantity = reorder_quantity
        self.lead_time = lead_time
        self.historical_sales = []

    def add_sales_data(self, sales):
        self.historical_sales.append(sales)
        self.current_stock -= sales  # Update current stock after sale


class Warehouse:
    def __init__(self, warehouse_id, location):
        self.warehouse_id = warehouse_id
        self.location = location
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def track_inventory(self):
        print("\n--- Inventory Tracking ---")
        for product in self.products.values():
            if product.current_stock < product.reorder_point:
                print(f"Reorder Alert for: {product.name}")
                print(f"Current Stock: {product.current_stock}")
                print(f"Recommended Order Quantity: {product.reorder_quantity}")
            else:
                print(f"{product.name} is sufficiently stocked.")

    def generate_report(self):
        print("\n--- Inventory Report ---")
        for product in self.products.values():
            print(f"Product: {product.name}")
            print(f"Current Stock: {product.current_stock}")
            print(f"Turnover Rate: {self.calculate_turnover_rate(product)}")

    def calculate_turnover_rate(self, product):
        total_sales = sum(product.historical_sales)
        average_stock = (product.current_stock + product.current_stock) / 2
        turnover_rate = total_sales / average_stock if average_stock > 0 else 0
        return turnover_rate


def calculate_eoq(annual_demand, ordering_cost, holding_cost):
    if holding_cost > 0:
        return (2 * annual_demand * ordering_cost / holding_cost) ** 0.5
    return 0


def main():
    warehouse = Warehouse(1, "Main Warehouse")

    # Example products
    product1 = Product(101, "Laptop", "Electronics", 15, 5, 20, 2)
    product1.add_sales_data(3)
    product1.add_sales_data(4)

    product2 = Product(102, "Smartphone", "Electronics", 30, 10, 15, 3)
    product2.add_sales_data(5)
    product2.add_sales_data(6)

    warehouse.add_product(product1)
    warehouse.add_product(product2)

    while True:
        print("\nOptions:")
        print("1. Track Inventory")
        print("2. Generate Report")
        print("3. Add Sales Data")
        print("4. Calculate EOQ")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            warehouse.track_inventory()
        elif choice == '2':
            warehouse.generate_report()
        elif choice == '3':
            product_id = int(input("Enter Product ID: "))
            sales = int(input("Enter sales data: "))
            if product_id in warehouse.products:
                warehouse.products[product_id].add_sales_data(sales)
                print("Sales data updated.")
            else:
                print("Product not found.")
        elif choice == '4':
            product_id = int(input("Enter Product ID: "))
            if product_id in warehouse.products:
                annual_demand = sum(warehouse.products[product_id].historical_sales)
                ordering_cost = 50  # Example ordering cost
                holding_cost = 2    # Example holding cost per unit
                eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)
                print(f"Optimal Order Quantity (EOQ) for {warehouse.products[product_id].name}: {eoq:.2f}")
            else:
                print("Product not found.")
        elif choice == '5':
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
