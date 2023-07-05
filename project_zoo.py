class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        print(f"Commands for {self.species} ({self.name}):")
        for command in self.commands:
            print(command)

class PetRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def print_commands(self, name):
        animal = self.find_animal(name)
        if animal:
            animal.get_commands()
        else:
            print("Animal not found")

    def add_command_to_animal(self, name, command):
        animal = self.find_animal(name)
        if animal:
            animal.add_command(command)
            print("Command added")
        else:
            print("Animal not found")

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.count > 0:
            raise Exception("Counter was not used in a resource block")
        return False

try:
    with Counter() as counter:
        registry = PetRegistry()
        print("Welcome to the Pet Registry!")

        while True:
            print("Menu:")
            print("1. Add a new animal")
            print("2. Find animal's commands")
            print("3. Add command to animal")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter animal's name: ")
                species = input("Enter animal's species: ")
                animal = Animal(name, species)
                counter.add()
                registry.add_animal(animal)
                print("Animal added")
            elif choice == "2":
                name = input("Enter animal's name: ")
                registry.print_commands(name)
            elif choice == "3":
                name = input("Enter animal's name: ")
                command = input("Enter command to add: ")
                registry.add_command_to_animal(name, command)
            elif choice == "4":
                break
            else:
                print("Invalid choice")

except Exception as e:
    print(e)