"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w stringu były najwięcej
i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4

2. (z gwiazdką) Stworzyć funkcję która przyjmie listę w liście elementem może być kolejna lista, lub liczba całkowita, zadaniem
funkcji jest 'spłaszczenie listy' i podanie wyniku, czyli, jeśli funkcja przyjmie listę [1, 2, [3, [4, 5]], 6, [[[7]]], 8, 9, 10]
to wynik powinien wynosić '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', liczba zagnieżdżeń w liście może być nieskończona, nie możemy zakładać
konkretnej liczby.
"""

def count_most_common_sign(input_str):
    sign_count = {}
    for sign in input_str:
        if sign in signs_count:
            sign_count[sign] += 1
        else:
            sign_count[sign] = 1
    most_common_sign = max(sign_count, key=sign_count.get)
    return most_common_sign, sign_count[most_common_sign]

result = count_most_common_sign('ala ma kota')
print(result)