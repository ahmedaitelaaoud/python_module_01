class Plant:
    """
    Represents a plant in the garden with basic attributes.

    Attributes:
        name: The plant's name
        height: Current height in centimeters
        age: Age in days
    """

    def __init__(self, name, height, age):
        """
        Initialize a new plant.

        Args:
            name: The plant's name
            height: Starting height in cm
            age: Starting age in days
        """
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """
        Shown info about plant

        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")



rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
# remove get.info
rose.get_info()
sunflower.get_info()
cactus.get_info()
