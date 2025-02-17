from uuid import uuid4 as id
from uuid import uuid4 as idd
import time

class Product:
    def __init__(self, name, price, quantity):
        self.__id = id()
        self.name = name  
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot nomi: {self.name}, Narxi: {self.price}, Miqdori: {self.quantity}, id raqami: {self.__id}"

    def sell(self, amount):
        if amount > self.quantity:
            return f"Siz {amount}ta mahsulot so'radingiz, lekin omborda {self.quantity}ta bor."
        else:
            self.quantity -= amount
            return f"{amount}ta mahsulot sotildi. Omborda {self.quantity}ta qoldi."

    def restock(self, amount):
        self.quantity += amount
        return f"Omborga {amount}ta mahsulot qo'shildi. Yangi miqdor: {self.quantity}"

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f", garantiya: {self.warranty}yil"
        return data

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date  

    def info(self):
        data = super().info()
        data += f", Yaroqlilik muddati: {self.expiration_date}"
        return data
    
    def sell(self, amount):
        if self.expiration_date < "2025-02-11":  
            return "Xatolik: mahsulot muddati o'tgan!"
        return super().sell(amount)

# Savat klassi
class Basket:
    def __init__(self):
        self.__id = idd()
        self.products = []

    def add(self, product, price, quantity):
        self.products.append({"product": product, "price": price, "quantity": quantity})
        return f"{product} ({quantity} dona) savatga qo'shildi!"

    def show(self): 
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']}: {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def calc(self):
        summa = sum(i["price"] * i["quantity"] for i in self.products)
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

    def delete_basket(self):
        self.products.clear() 
        return "Savat butunlay bo'shatildi!" 

# Dastur boshlanishi
products = []
basket = Basket()

while True:
    print("\n1 - Omborni boshqarish")
    print("2 - Ombordagi mahsulotlarni ko'rish")
    print("3 - Mahsulot sotish")
    print("4 - Mahsulot qayta yuklash")
    print("5 - Savatga solish")
    print("6 - Chiqish")
    
    choice = input("Tanlov kiriting: ")

    if choice == "1":
        print("\nMahsulot turini tanlang:")
        print("1 - Oddiy mahsulot")
        print("2 - Elektronika")
        print("3 - Oziq-ovqat")
        
        time.sleep(1)
        prod_type = input("Tanlang 1, 2, 3: ")
        name = input("Mahsulot nomi: ")
        price = int(input("Narxi: "))
        quantity = int(input("Miqdori: "))

        if prod_type == "1":
            product = Product(name, price, quantity)
        elif prod_type == "2":
            warranty = int(input("Garantiya muddati (yil): "))
            product = Electronics(name, price, quantity, warranty)
        elif prod_type == "3":
            expiration_date = input("Yaroqlilik muddati (YYYY-MM-DD): ")
            product = Food(name, price, quantity, expiration_date)
        else:
            print("Xato tanlov!")
            continue

        products.append(product)
        print("Mahsulot qo'shildi!")

    elif choice == "2":
        if not products:
            print("Omborda hech narsa yo'q!")
        else:
            for i, p in enumerate(products, 1):
                print(f"{i}. {p.info()}")

    elif choice == "3":
        if not products:
            print("Sotish uchun mahsulot yo'q!")
            continue
        
        for i, p in enumerate(products, 1):
            print(f"{i}. {p.info()}")

        prod_index = int(input("Qaysi mahsulotni sotmoqchisiz? (raqam): ")) - 1
        if 0 <= prod_index < len(products):
            amount = int(input("Nechta sotmoqchisiz? "))
            print(products[prod_index].sell(amount))
        else:
            print("Xato tanlov!")

    elif choice == "4":
        if not products:
            print("Omborda hech narsa yo'q!")
            continue
        
        for i, p in enumerate(products, 1):
            print(f"{i}. {p.info()}")
        
        prod_index = int(input("Qaysi mahsulotga qo'shmoqchisiz? (raqam): ")) - 1
        if 0 <= prod_index < len(products):
            amount = int(input("Nechta qo'shmoqchisiz? "))
            print(products[prod_index].restock(amount))
        else:
            print("Xato tanlov!")

    elif choice == "5":
        if not products:
            print("Savatga qo'shish uchun mahsulot yo'q!")
            continue

        for i, p in enumerate(products, 1):
            print(f"{i}. {p.info()}")

        prod_index = int(input("Qaysi mahsulotni savatga qo'shmoqchisiz? (raqam): ")) - 1
        if 0 <= prod_index < len(products):
            amount = int(input("Nechta qo'shmoqchisiz? "))
            if amount <= products[prod_index].quantity:
                basket.add(products[prod_index].name, products[prod_index].price, amount)
                print("Mahsulot savatga qo'shildi!")
            else:
                print("Savatga qo'shish uchun yetarli mahsulot yo'q!")
        else:
            print("Xato tanlov!")

        print("\nSavatni ko'rish uchun 1 ni bosing, bo'shatish uchun 2 ni bosing, orqaga qaytish uchun istalgan tugmani bosing.")
        sub_choice = input("Tanlov: ")
        if sub_choice == "1":
            print(basket.show())
            print(basket.calc())
        elif sub_choice == "2":
            print(basket.delete_basket())

    elif choice == "6":
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov!")
