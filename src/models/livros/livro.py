from interfaces.i_livro import ILivro

class Livro(ILivro):
    def __init__(self, titulo: str, autor: str, preco: float):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def preco(self):
        return self._preco
    
    def exibir_detalhes(self) -> str:
        return f'Título: {self.titulo}, Autor: {self.autor}, Preço: {self.preco:.2f}'
