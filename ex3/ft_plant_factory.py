class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days old)")


plant_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
    ]
print("=== Plant Factory Output ===")
for name, height, age in plant_data:
    new_plant = Plant(name, height, age)
    new_plant.get_info()
print(f"Total plants created: {len(plant_data)}")
