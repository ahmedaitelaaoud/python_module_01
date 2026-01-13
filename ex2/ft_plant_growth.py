class Plant:
    """
    Represents a plant that can grow over time.
    """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """
        Simulates one cycle of growth for the plant.

        Increments the height by 1cm and age by 1 day.
        """
        self.height += 1
        self.age += 1

    def get_info(self):
        """Prints current status."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)

print("=== Day 1 ===")
rose.get_info()
for i in range(1, 7):
    rose.grow()
print("=== Day 7 ===")
rose.get_info()
print(f"Growth this week: +6cm")
