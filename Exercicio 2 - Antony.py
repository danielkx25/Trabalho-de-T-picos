loop = 1
salario_total = 0
salario_final = 0
while loop < 13:
    try:
        salario_actual = input("Digite el salario del mes "+str(loop)+":")
        gastos = input("Digite los gastos del mes :")

        salario_actual = float(salario_actual)
        #** **#
        ultimo_salario_final = salario_final
        salario_final += (salario_actual - gastos)

        if(salario_final < 0):
            salario_final = ultimo_salario_final
            raise ValueError()
        #** **#
        salario_total += salario_actual
        salario_final *= 1.05

        print("Mes "+str(loop)+":")
        print("Salario recebido: "+str(salario_actual))
        print("Gastos: "+str(gastos))
        print("Salario total hasta ahora: "+str(salario_total))
        print("Dinero disponible (calculado después del incremento del 5%): "+str(salario_final))

        loop+=1

    except ValueError:
        print("No puedes gastar mas de lo que tienes")