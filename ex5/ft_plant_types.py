class Plant:
    """Base class for all vegetation in the garden."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age= age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

class Flower(Plant):
    """
    Represents a flowering plant that extends the base Plant class.

    Attributes:
        color (str): The color of the flower petals.
    """
    def __init__(self, name, height, age, color):
        """
        Initializes a new Flower.

        Args:
            name (str): The common name of the flower.
            height (int): Initial height in cm.
            age (int): Age in days.
            color (str): The specific color (e.g., "Red", "Yellow").
        """
        super().__init__(name, height, age)
        self.color = color

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self):
        """
        Simulates the blooming behavior of the flower.
        """
        print(f"{self.name} is blooming beautifully")

class Tree(Plant):
    """
    Represents a tree, adding diameter and shade functionality.

    Attributes:
        diametre (int): The trunk diameter of the tree.
    """
    def __init__(self, name, height, age, diametre):
        """
        Args:
            name (str): Tree species name.
            height (int): Height in cm.
            age (int): Age in days.
            diametre (int): Trunk diameter in cm.
        """
        super().__init__(name, height, age)
        self.diametre = diametre

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.diametre} diameter")

    def provide_shade(self):
        """Calculates and prints the shade coverage provided by the tree."""
        print(f"{self.name} provides 78 square meters of shade")

class Vegetable(Plant):
    """
    Represents an edible plant.

    Attributes:
        veg_type (str): The type of vegetable (e.g., 'root', 'summer').
    """
    def __init__(self, name, height, age, veg_type):
        super().__init__(name, height, age)
        self.veg_type = veg_type

    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.veg_type} harvest")

    def harvest_info(self):
        """Displays nutritional information about the vegetable."""
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
