class CoffeeMachine:

    def __init__(self, water, coffee_beans, milk):
        self.water = water
        self.coffee_beans = coffee_beans
        self.milk = milk

    def check_resources(self, required_water, required_coffee_beans, required_milk):
        if self.water >= required_water and self.coffee_beans >= required_coffee_beans and self.milk >= required_milk:
            return True
        else:
            print("Insufficient resources. Please check the ingredient levels.")
            return False
            
    def add_resources(self, add_water, add_coffee_beans, add_milk):
        self.water += add_water
        self.coffee_beans += add_coffee_beans
        self.milk += add_milk
        print(f"Added {add_water}ml of water. Current water level: {self.water}ml")
        print(f"Added {add_coffee_beans}g of coffee beans. Current coffee beans level: {self.coffee_beans}g")
        print(f"Added {add_milk}ml of milk. Current milk level: {self.milk}ml")
    
    def make_espresso(self):
        if self.check_resources(50, 20, 0):
            print("Making Espresso...")
            self.water -= 50
            self.coffee_beans -= 20
            print("Espresso is ready!")
        else:
            print("Not enough resources to make Espresso.")

    def make_latte(self):
        if self.check_resources(50, 20, 30):
            print("Making Latte...")
            self.water -= 50
            self.coffee_beans -= 20
            self.milk -= 30
            print("Latte is ready!")
        else:
            print("Not enough resources to make Latte.")


coffee_machine = CoffeeMachine(water=500, coffee_beans=250, milk=300)

coffee_machine.make_espresso()
coffee_machine.make_latte()

coffee_machine.add_resources(100, 50, 60)

coffee_machine.make_espresso()
coffee_machine.make_latte()
