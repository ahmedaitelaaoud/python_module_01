class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age= age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beatifully")

class Tree(Plant):
    def __init__(self, name, height, age, diametre):
        super().__init__(name, height, age)
        self.diametre = diametre

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.diametre} diameter")

    def provide_shade(self):
        print(f"{self.name} provides 78 square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, veg_type):
        super().__init__(name, height, age)
        self.veg_type = veg_type

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.veg_type} harvest")

    def harvest_info(self):
        print(f"{self.name} is rich in vitamin C")

print("=== Garden Plant Types ===\n")

rose = Flower("Rose", 25, 30, "red")
rose.get_info()
rose.bloom()
print()

oak = Tree("Oak", 500, 1825, 50)
oak.get_info()
oak.provide_shade()
print()

tomato = Vegetable("Tomato", 80, 90, "summer")
tomato.get_info()
tomato.harvest_info()
