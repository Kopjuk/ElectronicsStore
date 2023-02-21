class Item:
    DiscountPriceLevel = 0.8
    InstancesCreated = []

    def __init__(self, product_name: str, unit_price: int, quantity_store: int):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity_store = quantity_store
        self.InstancesCreated.append(self.product_name)

    def AmountPerItem(self):
        self.amaunt = self.unit_price * self.quantity_store
        return self.amaunt

    def DiscountPrice(self):
        self.discount_price = self.unit_price * self.DiscountPriceLevel
        return self.discount_price


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.AmountPerItem())
print(item2.AmountPerItem())

item1.DiscountPriceLevel = 0.9
item1.DiscountPrice()
print(item1.DiscountPrice())
print(item2.DiscountPrice())

print(Item.InstancesCreated)

