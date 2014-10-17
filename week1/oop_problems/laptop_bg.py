class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        print(self.final_price - self.stock_price)


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.deskspace = diskspace
        self.ram = ram


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        if product in self.products:
            self.products[product] += count
        else:
            self.products[product] = count

    def list_products(self, product_class):
        for product in self.products:
            if isinstance(product, product_class):
                print("{} - {}".format(product, self.products[product]))


new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
new_store = Store('Laptop.bg')
new_store.load_new_products(new_smarthphone, 20)

#!!!! predefine __str__
