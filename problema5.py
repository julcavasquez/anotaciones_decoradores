def funcion_decoradora(funcion_parametro) -> function:
    def funcion_interna(number):
        print("Hola, estoy decorando esta función")
        funcion_parametro(number)
        print("Terminé de decorar")
    return funcion_interna 

@funcion_decoradora
def mostrar(n) -> None:
    print("Ingresaste el número", n)

mostrar(50)