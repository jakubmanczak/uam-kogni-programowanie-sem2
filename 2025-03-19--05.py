# zadanie 4
import time, random

print("Losuję szczęśliwe liczby...")
for i in range(6):
    time.sleep(.5)
    print(f"{random.randint(1, 49)}")
