class Enemy:
    def __init__(self, name="Goblin", hit_points=100):
        self.name = name
        self.hit_points = hit_points

    def shout(self):
        print("I will destroy you!")

    def take_damage(self, amount):
        self.hit_points -= amount
        print(f"{self.name} took {amount} damage! Remaining HP: {self.hit_points}")

# Example usage
if __name__ == "__main__":
    # Create an instance of Enemy
    enemy = Enemy(name="Orc", hit_points=150)
    
    # Demonstrate functionality
    print(f"An enemy appeared: {enemy.name} with {enemy.hit_points} HP!")
    enemy.shout()
    enemy.take_damage(30)
