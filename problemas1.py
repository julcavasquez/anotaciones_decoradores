

def funcion_decoradora(funcion_parametro):
    def funcion_interna(numbers):
        print("Inicio del calculo del promedio de la lista números.")
        print(funcion_parametro(numbers))
        print("El cálculo ha finalizado")
    return funcion_interna

@funcion_decoradora
def get_avg(numbers : list) -> float:
    return sum(numbers) / len(numbers)


list_numbers = [10,20,21,11,12]
get_avg(list_numbers)