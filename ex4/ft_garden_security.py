class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._age = 0
        self._height = 0


    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, new_height):
        if new_height >=0:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print("Security: Negative height rejected")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose")
    plant1.set_age(25)
    plant1.set_height(30)
    print()
    plant1.set_height(-5)
    plant1.set_age(-5)
    print(f"\nCurrent plant: {plant1.name} ({plant1.get_age()} days ols, {plant1.get_height()}cm)")
