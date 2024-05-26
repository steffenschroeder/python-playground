"""
For every 4 digit number: if you calc:
    number sorted descending - number sorted ascending
    the result will finally converge 6174
"""


def order(n: int, asc: bool) -> int:
    return int("".join(sorted(str(n), key=int, reverse=not asc)))


numbers = [3245, 8963, 5198]

for number in numbers:
    while True:
        print(number)
        if number == 6174:
            break
        number = order(number, asc=False) - order(number, asc=True)
    print()
