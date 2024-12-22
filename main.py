from models.cliente import Cliente
from models.livros.ebook import Ebook, FormatoEbook
from models.livros.livro_fisico import LivroFisico
from services.livraria import Livraria

if __name__ == '__main__':
    livraria = Livraria()
    
    ebook1 = Ebook(titulo="Aprenda Python", autor="Guido van Rossum", preco=39.90, formato=FormatoEbook.PDF)    
    livro_fisico1 = LivroFisico(titulo="Introdução ao Django", autor="Adrian Holovaty", preco=79.90, numero_paginas=350)

    livraria.adicionar_livro(ebook1)
    livraria.adicionar_livro(livro_fisico1)

    cliente1 = Cliente(nome="Maria Silva", email="maria@example.com")
    livraria.registrar_cliente(cliente1)
    try:
        pedido = livraria.fazer_pedido(cliente=cliente1, livros=[ebook1, livro_fisico1])
        print(f'Pedido realizado para o cliente {pedido.cliente.nome}')
        print(f'Total do pedido: {pedido.calcular_total():.2f}')
        for livro in pedido.lista_de_livros:
            print(livro.exibir_detalhes())
    except ValueError as e: 
        print(f'Erro ao fazer pedido: {e}')
    

