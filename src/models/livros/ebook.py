from enum import Enum
from models.livros.livro import Livro

class FormatoEbook(Enum):
    PDF = 'PDF'
    EPUB = 'EPUB'
    MOBI = 'MOBI'

class Ebook(Livro):
    def __init__(self, titulo: str, autor: str, preco: float, formato: FormatoEbook):
        super().__init__(titulo, autor, preco)
        self._formato = formato
        
    @property
    def formato(self):
        return self._formato.value
    
    def exibir_detalhes(self) -> str:
        return super().exibir_detalhes() + f', Formato: {self._formato.value}'
