# Pornsawan Khararam
# 683040156-9

class Cat:
    species = "Felis catus"
    total_cats = 0
    average_lifespan = 15

    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.hungry = False
        self.energy = 100
        self.happiness = 100
        Cat.total_cats += 1

    def meow(self):
        if self.hungry:
            print(f"{self.name} meows loudly: 'Meow! I'm hungry!'")
        elif self.energy < 50:
            print(f"{self.name} meows weakly: 'meow... tired...'")
        elif self.happiness > 80:
            print(f"{self.name} meows happily: 'Meow! ^.^'")
        else:
            print(f"{self.name} meows normally: 'Meow.'")

    def eat(self, food_amount):
        if food_amount > 0:
            self.hungry = False
            self.energy = min(100, self.energy + food_amount // 10) 
            self.happiness = min(100, self.happiness + food_amount // 20) 
            print(f"{self.name} ate {food_amount}g of food. Hungry: {self.hungry}, Energy: {self.energy}, Happiness: {self.happiness}")
        else:
            print("Invalid food amount.")

    def play(self, play_time):
        if play_time > 0:
            self.energy = max(0, self.energy - play_time * 2)
            self.happiness = min(100, self.happiness + play_time)
            self.hungry = True if self.energy < 30 else False 
            print(f"{self.name} played for {play_time} minutes. Hungry: {self.hungry}, Energy: {self.energy}, Happiness: {self.happiness}")
        else:
            print("Invalid play time.")

    def sleep(self, hours):
        if hours > 0:
            self.energy = min(100, self.energy + hours * 10)
            self.hungry = True if hours < 2 else False 
            print(f"{self.name} slept for {hours} hours. Energy: {self.energy}, Hungry: {self.hungry}")
        else:
            print("Invalid sleep hours.")

    def get_status(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "color": self.color,
            "hungry": self.hungry,
            "energy": self.energy,
            "happiness": self.happiness
        }

    @classmethod
    def from_birth_year(cls, name, birth_year, breed, color):
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age, breed, color)

    @classmethod
    def get_species_info(cls):
        return f"Species: {cls.species}, Average Lifespan: {cls.average_lifespan} years, Total Cats: {cls.total_cats}"

    @staticmethod
    def is_senior(age):
        return age > 7

    @staticmethod
    def calculate_healthy_food_amount(weight_kg):
        return weight_kg * 20