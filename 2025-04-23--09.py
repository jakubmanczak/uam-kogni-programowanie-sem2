# Usuwanie białych znaków: Napisz funkcję usun_biale_znaki(string), która usuwa wszystkie białe znaki
# (spacje, tabulatory, nowe linie) z podanego stringa.
# Przykład użycia: usun_biale_znaki("hello world ") powinno zwrócić "helloworld".
# Wykorzystaj tylko instrukcje warunkowe, pętle (bez biblioteki string).

def usun_biale_znaki(znaki):
    noweznaki = ""
    for znak in znaki[:]:
        if not(znak == ' ' or znak == '\t' or znak == '\n'):
           noweznaki += znak
    return noweznaki

assert(usun_biale_znaki("hello world ") == "helloworld")
print(usun_biale_znaki("hello world "))
