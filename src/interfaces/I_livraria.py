from abc import ABC, abstractmethod
from typing import List

from models.cliente import Cliente
from models.livros.livro import Livro
from models.pedido import Pedido

class ILivraria(ABC):
    
    @abstractmethod
    def adicionar_livro(self, livro: Livro):
        pass
    
    @abstractmethod
    def registrar_cliente(self, cliente: Cliente):
        pass
    
    @abstractmethod
    def fazer_pedido(self, cliente: Cliente, livros: List[Livro]) -> Pedido:
        pass
    