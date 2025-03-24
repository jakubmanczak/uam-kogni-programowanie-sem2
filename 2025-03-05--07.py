print("Podaj nazwę nowego użytkownika: ")
username = input()
print("Podaj nowe hasło: ")
setpassw = input()

print("-------------")
print("Podaj hasło: ")
password = input()

if setpassw == password:
    print("Hasło prawidłowe!")
else:
    print("Hasło fałszywe!")
