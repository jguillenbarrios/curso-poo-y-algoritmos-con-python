class Persona:
  def __init__(self, nombre):
    self.nombre = nombre
  '''Cuando una persona avanza normalmente lo hace caminando'''
  def avanza(self):
    print('Ando caminando')
  

class Ciclista(Persona):
  def __init__(self, nombre):
    super().__init__(nombre)
  ''' Un ciclista avanza diferente, avanza en bicicleta'''
  def avanza(self):
    print('Ando en bicicleta')

def main():
  persona = Persona('Jesus')
  persona.avanza()
  ciclista = Ciclista('Virgina')
  ciclista.avanza()

if __name__ == '__main__':
  main()