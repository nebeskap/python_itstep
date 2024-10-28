class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна за одиницю: {self.price}")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.calculate_total_price()}")



product = Product(name="Книжка", price = 500, quantity = 3)
product.display_info()