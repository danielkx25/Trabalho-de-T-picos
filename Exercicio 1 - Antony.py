nombre = input("Digite su nombre:")
apellido =  input("Digite su apellido:")
print("Lectura de salarios")
loop = 1
salario_anual = 0
gasto_anual = 0
while loop <=12:
        salario_anual += float(input("Digite el salario del mes "+str(loop)+": "))
        gasto_anual += float(input("Digite el gasto total del mes "+str(loop)+": "))
        loop=loop+1

if salario_anual <= 22847.76:
    imposto = 0
elif salario_anual > 22847.76 and salario_anual <= 33919.80:
    imposto = salario_anual*(7.5/100)
elif salario_anual > 33919.80 and salario_anual <= 45012.60:
    imposto = salario_anual*(15/100)
elif salario_anual > 45012.60 and salario_anual <= 55976.16:
    imposto = salario_anual*(22.5/100)
elif salario_anual > 55976.16:
    imposto = salario_anual*(27.5/100)

salario_aumentado = salario_anual*1.05
dinero_restante = salario_aumentado-imposto-gasto_anual
print("Su nombre: "+nombre+" "+apellido)
print("Su salario en los últimos 12 meses: "+str(salario_anual))
print("Su promedio salarial: "+str(salario_anual/12))
print("Su salario con aumento de 5%: "+str(salario_aumentado))
print("Gastos: "+str(gasto_anual))
print("IRPF a pagar: "+str(imposto))
print("Dinero restante: "+str(dinero_restante))

