# Zamiana miejscami pierwszej i ostatniej litery w stringu: Napisz funkcję zamien_pierwsza_i_ostatnia(string),
# która zamienia miejscami pierwszą i ostatnią literę w podanym stringu.
# Przykład użycia: zamien_pierwsza_i_ostatnia("hello") powinno zwrócić "oellh".

def zamien_pierwsza_i_ostatnia(znaki):
    if len(znaki) < 2:
        return znaki

    noweznaki = ""
    pierwszy = znaki[0]
    ostatni = znaki[-1]
    for i in range(len(znaki)):
        if i == 0:
            noweznaki += ostatni
        elif i == len(znaki)-1:
            noweznaki += pierwszy
        else:
            noweznaki += znaki[i]
    return noweznaki

assert(zamien_pierwsza_i_ostatnia("hello") == "oellh")
print(zamien_pierwsza_i_ostatnia("hello"))
