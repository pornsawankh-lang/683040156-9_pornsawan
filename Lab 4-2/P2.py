# Pornsawan Khararam
# 683040156-9

from cat import Cat

cat1 = Cat("Whiskers", 3, "Siamese", "White")
cat2 = Cat.from_birth_year("Mittens", 2018, "Persian", "Gray")

print(Cat.get_species_info())
cat1.meow()
cat1.eat(50)
cat1.play(10)
cat1.sleep(5)
print(cat1.get_status())
print(f"Is {cat1.name} senior? {Cat.is_senior(cat1.age)}")
print(f"Healthy food for 4kg cat: {Cat.calculate_healthy_food_amount(4)}g")