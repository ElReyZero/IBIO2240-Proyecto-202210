

class InvalidParameters(Exception):
    """
    Excepción que se lanza cuando los parámetros ingresados no son válidos.
    """
    def __init__(self, message):
        self.message = message