class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, nb):
        self.height += nb

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    rose.get_info()
    print("=== Day 7 ===")
    rose.grow(6)
    rose.get_info()
    print(f"Growth this week: +6cm")
