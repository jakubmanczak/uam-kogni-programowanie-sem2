# for i in range(10):
#     print(i)
#
# for i in range(0, 10):
#     print(i)
#
# for i in range(10, 0, -2):
#     print(i)

# for i in range(1, 4):
#     for j in range(1, 5):
#         print(f"{i}/{j} --- pętla zewn. iteracja nr. {i}; pętla wewn. iteracja nr. {j}")

# cyfra = 0
# while not(cyfra == 10):
#     print(cyfra)
#     cyfra += 1

# cyfra = 5
# while not(cyfra == 10):
#     print(cyfra)
#     cyfra += 1

# cyfra = 50
# while not(cyfra <= 30):
#     print(cyfra)
#     cyfra -= 3

print("Aby zakończyć program wpisz znak \"q\"")
while True:
    znak = input()
    if znak == "q":
        break
    print("Nie wpisano \"q\"")
