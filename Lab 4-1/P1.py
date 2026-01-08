# Pornsawan Khararam
# 683040156-9

from datetime import datetime, timedelta
from cat import Cat

cat1 = Cat("Fluffy", "Persian", 2, "MEiii")
cat2 = Cat("Whiskers", "Siamese", 3, "TeH")
cat3 = Cat("Mittens", "Tabby", 1, "ARTx")

print("First cat date_in:", cat1.get_time_in())
cat1.greet()

print("Second cat date_out:", cat2.get_time_out())
cat2.set_time_out(datetime.now() + timedelta(days=2))
print("Second cat new date_out:", cat2.get_time_out())

cat3.owner = "ARTxEIEI"
cat3.age = 2

# Show the details of all 3 cats
print("Details of all cats:")
cat1.print_cat()
cat2.print_cat()
cat3.print_cat()

print("Total number of cats:", Cat.get_num())

Cat.reset_cat()

print("Total number of cats after reset:", Cat.get_num())