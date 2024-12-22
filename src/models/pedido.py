from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from models.cliente import Cliente
from models.livros.livro import Livro


@dataclass
class Pedido():
    cliente: Cliente
    lista_de_livros: List[Livro] = field(default_factory=list) # Gera uma nova lista para cada instância
    data_do_pedido: datetime = field(default_factory=datetime.now)  # Gera uma nova data para cada instância
    
    def adicionar_livro(self, livro: Livro):
        self.lista_de_livros.append(livro)
        print(f'O livro: {livro.titulo} foi adicionado ao seu pedido.')
    
    def calcular_total(self) -> float:
        return sum(livro.preco for livro in self.lista_de_livros)
