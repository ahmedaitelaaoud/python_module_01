class SecurePlant:
    """
    A plant class that enforces data integrity using setter methods.
    Prevents impossible values (like negative height or age).
    """
    def __init__(self, name):
        self.name = name
        self._age = 0
        self._height = 0

    def get_height(self):
        """Returns the current height."""
        return self._height

    def get_age(self):
        """Returns the current age."""
        return self._age

    def set_height(self, new_height):
        """
        Updates the plant's height after validating the input.

        Security check: Rejects negative values to preserve physics.
        Args:
            new_height (int): The target height in cm.
        """
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {new_height}cm [OK]")
        else:
            print(
                f"Invalid operation attempted: height "
                f"{new_height}cm [REJECTED]"
                )

    def set_age(self, new_age):
        """
        Updates the plant's age after validating the input.

        Args:
            new_age (int): The target age in days. Must be non-negative.
        """
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {new_age} days [OK]")
        else:
            print("Security: Negative height rejected")


print("=== Garden Security System ===")

plant1 = SecurePlant("Rose")
print(f"Plant created: {plant1.name}")
plant1.set_height(25)
plant1.set_age(30)

print()

plant1.set_height(-5)
plant1.set_age(-5)

print(
    f"\nCurrent plant: {plant1.name} "
    f"({plant1.get_height()}cm, {plant1.get_age()} days old)"
    )
