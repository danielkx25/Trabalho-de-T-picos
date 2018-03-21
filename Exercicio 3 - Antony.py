class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = list()
        self.gasto = list()

    def LeerSalario(self, pos, salario):
        self.salario.append(salario)

    def LeerGasto(self, pos, gasto):
        self.gasto.append(gasto)

    def CalcularDineroRestante(self):
        salario_anual = 0
        gasto_anual = 0
        for element in self.salario:
            salario_anual = salario_anual + element

        for element in self.gasto:
            gasto_anual += element

        if salario_anual <= 22847.76:
            imposto = 0
        elif salario_anual > 22847.76 and salario_anual <= 33919.80:
            imposto = salario_anual * (7.5 / 100)
        elif salario_anual > 33919.80 and salario_anual <= 45012.60:
            imposto = salario_anual * (15 / 100)
        elif salario_anual > 45012.60 and salario_anual <= 55976.16:
            imposto = salario_anual * (22.5 / 100)
        elif salario_anual > 55976.16:
            imposto = salario_anual * (27.5 / 100)



        self.salario_anual = salario_anual
        self.salario_aumentado = salario_anual * 1.05
        self.promedio_salarial = salario_anual/12
        self.gasto_anual = gasto_anual
        self.impuesto = imposto
        self.dinero_restante = self.salario_aumentado - imposto - gasto_anual



    def ImprimirInformacion(self):
        print("Su nombre: " + self.nombre + " " + self.apellido)
        print("Su salario en los últimos 12 meses: " + str(self.salario_anual))
        print("Su promedio salarial: " + str(self.salario_anual / 12))
        print("Su salario con aumento de 5%: " + str(self.salario_aumentado))
        print("Gastos: " + str(self.gasto_anual))
        print("IRPF a pagar: " + str(self.impuesto))
        print("Dinero restante: " + str(self.dinero_restante))

nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")

personaObj = Persona(nombre,apellido)

loop = 1
while loop <=12:
        salario_mes = float(input("Digite el salario del mes "+str(loop)+": "))
        gasto_mes = float(input("Digite el gasto total del mes "+str(loop)+": "))
        personaObj.LeerSalario(loop,salario_mes)
        personaObj.LeerGasto(loop,gasto_mes)
        loop+=1

personaObj.CalcularDineroRestante()
personaObj.ImprimirInformacion()
