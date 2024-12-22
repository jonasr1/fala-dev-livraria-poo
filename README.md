# Desafio de Programação Orientada a Objetos - Sistema de Livraria

## Descrição
Desenvolver um sistema básico de gerenciamento de livraria que inclui livros digitais e físicos. O sistema deve implementar funcionalidades para adicionar livros, registrar clientes, fazer pedidos e calcular o total dos pedidos, utilizando conceitos de herança e polimorfismo.

---

## Requisitos

### 1. **Classes Base e Derivadas**

Criar a classe base `Livro` com as seguintes propriedades:
- **Título**
- **Autor**
- **Preço**

Implementar as classes derivadas:
- **Ebook** (adicional: `Formato` [PDF, EPUB])
- **LivroFisico** (adicional: `NumeroPaginas`)

---

### 2. **Exibir Detalhes**

- Adicionar o método virtual `ExibirDetalhes` na classe base `Livro`.
- Sobrescrever o método nas classes derivadas para incluir os detalhes específicos de cada tipo de livro.

---

### 3. **Gerenciamento de Livros**

Criar a classe `Livraria` com:
- Listas para:
  - `LivrosDisponiveis`
  - `Clientes`
  - `Pedidos`
- Métodos:
  - `AdicionarLivro`
  - `RegistrarCliente`
  - `FazerPedido`

---

### 4. **Classe Cliente**

Criar a classe `Cliente` com as seguintes propriedades:
- **Nome**
- **Email**

---

### 5. **Classe Pedido**

Criar a classe `Pedido` com:
- **Propriedades**:
  - `Cliente`
  - `ListaDeLivros`
  - `DataDoPedido`
- **Métodos**:
  - `AdicionarLivro`
  - `CalcularTotal`

---

### 6. **Implementar Interfaces**

- **ILivro**:
  - Definir um contrato para as propriedades e métodos da classe `Livro`.
  - Implementar na classe `Livro`.
  
- **ILivraria**:
  - Definir um contrato para os métodos de gerenciamento de livros.
  - Implementar na classe `Livraria`.

---

### 7. **Teste no Método Main**

- Instanciar a classe `Livraria`.
- Adicionar livros (Ebook e LivroFisico).
- Registrar cliente.
- Fazer um pedido e adicionar livros.
- Calcular e exibir:
  - **Total do pedido**
  - **Detalhes dos livros**


# Estrutura do Projeto - Sistema de Livraria

## Estrutura de Diretórios

```plaintext
📦 desafio_livraria
 ┣ 📂src
 ┃ ┣ 📂interfaces
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜livro_interface.py
 ┃ ┃ ┗ 📜livraria_interface.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📂livros
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┣ 📜livro.py
 ┃ ┃ ┃ ┣ 📜ebook.py
 ┃ ┃ ┃ ┗ 📜livro_fisico.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜cliente.py
 ┃ ┃ ┗ 📜pedido.py
 ┃ ┣ 📂services
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜livraria.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜main.py
 ┣ 📜.gitignore
 ┗ 📜README.md
