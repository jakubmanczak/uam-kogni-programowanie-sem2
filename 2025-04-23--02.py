# Własna funkcja range: Napisz funkcję o nazwie moj_range(start, stop), która działa podobnie jak wbudowana funkcja range.
# Funkcja powinna generować sekwencję liczb od start (włącznie) do stop(wyłącznie).
# Wykorzystaj pętlę while, aby generować kolejne liczby w sekwencji.

def moj_range(start, stop, step):
    i = start
    liczby = []
    while i < stop:
        liczby.append(i)
        i += step
    return liczby

for i in moj_range(1, 10, 2):
    print(i)
