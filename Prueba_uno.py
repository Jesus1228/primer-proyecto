variable = 'Hola'
variable2 = 'mundo'
print(variable, variable2)

class Cacatua:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def Patada(self):
        print('Te pateo', self.nombre)

cacatua = Cacatua('Ronie', 'gruñe')
cacatua.Patada()
