
# def funcion_decoradora(funcion_parametro):
#     def funcion_interna(number):
#         num = float(input("Ingrese un número"))
#         print(funcion_parametro(num))
#         print("El cálculo ha finalizado")
#     return funcion_interna 


# @funcion_decoradora
def funcion_doble() -> str:
    number : float = float(input("Ingerse un número: "))
    return str(number * 2)

print(funcion_doble())
