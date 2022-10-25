
def funcion_decoradora(funcion_parametro):
    def funcion_interna(number):
        res = funcion_parametro(number)
        if res:
            print("Es par")
        else:
            print("Es impar")
    return funcion_interna 


@funcion_decoradora
def cal_par_impar(n : int) -> bool:
    return n % 2 == 0


num: int = int(input("Ingrese un número"))
cal_par_impar(num)