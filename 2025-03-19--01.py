import random

# for i in range(10):
#     # ewentualnie można by jeszcze dać zakres o jeden mniejszy
#     # i dodać lub odjąć random.random() - ale po co?
#     los = random.randint(-5, 5) * random.random()
#     print(los)
# print("-----")
# for i in range(10):
#     los = 10 * random.random() - 5
#     print(los)
# print("-----")
# for i in range(10): # liczby rzeczywiste
#     los = random.uniform(-5, 5) # nie używać na nadchodzącym projekcie
#     print(los)
# print("-----")
# for i in range(10):
#     los = 10 * random.random() - 5
#     los = round(los, 5)
#     print(los)
# print("-----")
# for i in range(10):
#     los = 10 * random.random() - 5
#     print(f"{los:.2f}")

slowo = "Kognitywistyka"
los = random.choice(slowo)
print(los)
