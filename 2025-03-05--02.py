print("Ile masz lat?")
wiek = int(input())

# if (wiek >= 18):
#     print("Brawo!")
#     print("Jesteś pełnoletni!")
# else:
#     print("Nie jesteś pełnoletni!")
# print("To był program sprawdzający pełnoletniość")

# if wiek <= 3:
#     print("Jesteś niemowlęciem!")
# elif wiek < 12:
#     print("Jesteś dzieckiem!")
# elif wiek < 20:
#     print("Jesteś nastolatkiem!")
# else:
#     print("Jesteś dorosły!")

if wiek <= 3:
    print("Jesteś niemowlęciem!")
if wiek < 12:
    print("Jesteś dzieckiem!")
if wiek < 20:
    print("Jesteś nastolatkiem!")
if wiek >= 20:
    print("Jesteś dorosły!")
