"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w stringu były najwięcej
i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4

2. (z gwiazdką) Stworzyć funkcję która przyjmie listę w liście elementem może być kolejna lista, lub liczba całkowita, zadaniem
funkcji jest 'spłaszczenie listy' i podanie wyniku, czyli, jeśli funkcja przyjmie listę [1, 2, [3, [4, 5]], 6, [[[7]]], 8, 9, 10]
to wynik powinien wynosić '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', liczba zagnieżdżeń w liście może być nieskończona, nie możemy zakładać
konkretnej liczby.

Po zrobieniu zadania, pushujemy wynik na nowy branch który stworzyliśmy i tworzymy pull requesta, pull request możemy zmerge;ować tylko
po akceptacji trenera
"""

# Zadanie 1
def popular_sign(string):
    counter = {}
    for sign in string:
@@ -25,4 +27,19 @@ def popular_sign(string):
    return sorted_counter[0]

string = "ala ma kota"
print(popular_sign(string))
print(popular_sign(string))


# Zadanie 2
def flatten_list(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result

lst = [1, 2, [3, [4, 5]], 6, [[[7]]], 8, 9, 10]
print(flatten_list(lst))
