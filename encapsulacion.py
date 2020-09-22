class CasillaDeVotacion:

  def __init__(self, identificador, pais):
    self._identificador = identificador
    self._pais = pais
    self._region = None
  #Decoradores: los identificamos con el simbolo '@'
  @property
  def region(self):
    return self._region
  
  @region.setter
  def region(self, region):
    if region in self._pais:
      self._region = region
    else:
          raise ValueError(f'La region {region} esta en la lista')
    
if __name__=='__main__':
  casilla = CasillaDeVotacion(123, ['CDMX','Veracruz','Tabasco','Campeche'])
  print({casilla.region})
  casilla.region = 'Veracruz'
  print(f'Despues de settear ahora la region es: {casilla.region}')
