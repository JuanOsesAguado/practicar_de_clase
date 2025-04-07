class Poli(object):
    """Clase Polinomio."""

    def __init__(self):
        """Crea un polinomio del grado cero."""
        self.termino_mayor = None
        self.grado = -1
    
    def agregar_termino(self):
        