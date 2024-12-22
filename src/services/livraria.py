from dataclasses import dataclass, field
from typing import List

from interfaces.I_livraria import ILivraria
from models.cliente import Cliente
from models.livros.livro import Livro
from models.pedido import Pedido


@dataclass
class Livraria(ILivraria):
    # O uso de field(default_factory=list) cria uma nova lista para cada instância,
    # evitando que objetos mutáveis sejam compartilhados entre instâncias.
    livros_disponiveis: List[Livro] = field(default_factory=list)
    clientes: List[Cliente] = field(default_factory=list)
    pedidos: List[Pedido] = field(default_factory=list)
    
    def adicionar_livro(self, livro: Livro):
        self.livros_disponiveis.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à livraria.")
        
    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nome}' registrado com sucesso.")
        
    def fazer_pedido(self, cliente: Cliente, livros: List[Livro]) -> Pedido:
        pedido = Pedido(cliente=cliente)
        for livro in livros:
            if livro in self.livros_disponiveis:
                pedido.adicionar_livro(livro)
            else:
                raise ValueError(f'Livro: {livro.titulo} não está disponível')
        self.pedidos.append(Pedido(cliente=cliente, lista_de_livros=livros))
        print(f"Pedido realizado para o(a) cliente '{cliente.nome}'. Total de livros: {len(livros)}.")
        return pedido
