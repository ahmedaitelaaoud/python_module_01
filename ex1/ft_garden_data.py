class Plant:
    """
    Represents a base plant entity in the garden ecosystem.

    Attributes:
        name (str): The common name of the plant.
        height (int): The current height of the plant in cm.
        age (int): The age of the plant in days.
    """

    def __init__(self, name, height, age):
        """
        Initializes a new Plant instance.

        Args:
            name (str): The name of the plant (e.g., "Rose").
            height (int): Initial height in centimeters.
            age (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")

print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
