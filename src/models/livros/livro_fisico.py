
from models.livros.livro import Livro

class LivroFisico(Livro):
    
    def __init__(self, titulo: str, autor: str, preco: float, numero_paginas: int):
        super().__init__(titulo, autor, preco)
        self._numero_paginas = numero_paginas
    
    @property
    def numero_paginas(self):
        return self._numero_paginas
    
    def exibir_detalhes(self) -> str:
        return super().exibir_detalhes() + f', Número de Páginas: {self._numero_paginas}'
        