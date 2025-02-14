class Basket:
    def __init__(self):
        self.products = []
        self.products2 = []

    def add(self, product, price, quantity):
        self.products.append({"product": product, "price": price, "quantity": quantity})
        return f"{product} ({quantity} savatga qo'shildi"

    def show(self): 
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']}: {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def calc(self):
        summa = 0
        for i in self.products:
            summa += i["price"] * i["quantity"]
        return f"Umumiy narx: {summa} USD"

    def remove(self, product, quantity=1):
        for i in self.products:
            if i["product"] == product:
                if i["quantity"] > quantity:
                    i["quantity"] -= quantity
                else:
                    self.products.remove(i)
                return f"{product} ({quantity} dona) savatdan olib tashlandi"
        return f"{product} savatda topilmadi"
    
    def append_to_second_basket(self):
        self.products2 = self.products.copy()  
        return f"Mahsulotlar 2chi savatga qo'shildi: {self.products2}"
    
    def revome_second_basket(self):
        self.products2.clear()  
        print("2chi savat butunlay o'chirildi")

    def delete_basket(self):
        self.products.clear() 
        return "Savat butunlay bo'shatildi!"

b = Basket()
print(b.add("qulpinay", 2, 3))
print(b.add("Banan", 1, 2))
print(b.show())
print(b.calc())
print(b.remove("qulpinay", 2))
print(b.show())
b.append_to_second_basket()
print(b.append_to_second_basket())
b.revome_second_basket()

