class Order():

    def __init__(self, customer_name, order_date, quantity, product_name, brand, warranty) -> None:
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.product_name = product_name
        self.brand = brand
        self.warranty = warranty