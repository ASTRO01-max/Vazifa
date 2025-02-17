import uuid

# class Car:
#     def __init__(self, name , yaer, km=0):
#         self.name = name
#         self.yaer = yaer
#         self.__km = km

    # def get_km(self):
    #     return self.__km
    
# car = Car("Colabt", 2025, 1000)
# car2 = car
# car2.name = "gnnbfvbgh"
# print(car.name)

""""""

# from uuid import uuid4 as id

# class Avto:
#     def __init__(self, name, year):
#         self.__id = id()
#         self.name = name
#         self.year = year
#         self.__km = 100

#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
# a = Avto("Cobalt", 2025)
# print(a.get_id())

class Sinf:
    def __init__(self,ism , familiya , yil):
        self.__id = uuid.uuid4()
        self.ism = ism 
        self.yil = yil 
        self.familiya = familiya
    
    def info(self):
        print(f"{self.ism}, {self.familiya}, {self.yil}. {self.__id}")

a = Sinf("Saloh", "2008", "Abdullayev")
a.info()




