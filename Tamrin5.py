class Vehicle:
    def init(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"برند: {self.brand}")
        print(f"سال ساخت: {self.year}")


class Car(Vehicle):
    def init(self, brand, year, num_doors):
        super().init(brand, year) 
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()  
        print(f"تعداد درها: {self.num_doors}")


class Motorcycle(Vehicle):
    def init(self, brand, year, has_sidecar):
        super().init(brand, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"دارای سایدکار: {'بله' if self.has_sidecar else 'خیر'}")


v1 = Vehicle("Toyota", 2020)
c1 = Car("BMW", 2022, 4)
m1 = Motorcycle("Yamaha", 2021, False)

print("---- Vehicle ----")
v1.display_info()

print("\n---- Car ----")
c1.display_info()

print("\n---- Motorcycle ----")
m1.display_info()
