class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)

print("=== Day 1 ===")
rose.get_info()
for i in range(1, 7):
    rose.grow()
print("=== Day 7 ===")
rose.get_info()
print(f"Growth this week: +6cm")
