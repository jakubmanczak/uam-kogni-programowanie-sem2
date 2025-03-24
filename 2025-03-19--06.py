# zadanie 5
import time, random

print("Losuję szczęśliwe liczby...")
los1 = random.randint(1, 49)
los2 = 0
while not(los2) or los2 == los1:
    los2 = random.randint(1, 49)
los3 = 0
while not(los3) or los3 == los2 or los3 == los1:
    los3 = random.randint(1, 49)
los4 = 0
while not(los4) or los4 == los3 or los4 == los2 or los4 == los1:
    los4 = random.randint(1, 49)
los5 = 0
while not(los5) or los5 == los4 or los5 == los3 or los5 == los2 or los5 == los1:
    los5 = random.randint(1, 49)
los6 = 0
while not(los6) or los6 == los5 or los6 == los4 or los6 == los3 or los6 == los2 or los6 == los1:
    los6 = random.randint(1, 49)

time.sleep(.5)
print(f"Los 1: {los1}")
time.sleep(.5)
print(f"Los 2: {los2}")
time.sleep(.5)
print(f"Los 3: {los3}")
time.sleep(.5)
print(f"Los 4: {los4}")
time.sleep(.5)
print(f"Los 5: {los5}")
time.sleep(.5)
print(f"Los 6: {los6}")


# złe podejście
#     działałoby tylko dla liczb jednocyfrowych...
#     albo dla dwucyfrowych jakbym w drugiej zmiennej zapisywał długość liczb...
#     ale to zbyt skomplikowane dla losowaniu sześciu.. jakbym miał losować 60 to może.
# for i in range(6):
#     time.sleep(.5)
#     los = 0
#     akceptowalne = False
#     while not akceptowalne:
#         if not i:
#             akceptowalne = True
#             break
#         los = random.randint(1, 6)
#         wylosowane = -1
#         natrafiono = False
#         for j in range(i):
#             wylosowane = wylosowane / 10
#             if wylosowane == los:
#                 natrafiono = True
#         if not natrafiono:
#             akceptowalne = True
#             if not i:
#                 wylosowane = los
#             else:
#                 wylosowane *= 10
#                 wylosowane += los
#     print(los)
