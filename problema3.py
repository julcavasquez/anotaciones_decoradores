


def duplicar_letra() -> list:
    palabra: str  = input("Ingrese una palabra: ")
    res: list  = []
    for p in palabra:
        res.append(p)
        res.append(p)
    return res

print(duplicar_letra())
