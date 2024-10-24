class Cliente:
    def __init__(self, n, fone):
        self._nome = n
        self._telefone = fone


#metodo Get
    def get_nome(self):
        return self._nome


#metodo set
    def set_nome(self, nome):
        self._nome = nome
