# Requisitos Funcionais (RF)

Os requisitos funcionais representam tudo o que o sistema deve fazer.

| ID   | Requisito Funcional                                                                   |
| ---- | ------------------------------------------------------------------------------------- |
| RF01 | O sistema deve permitir o cadastro de produtos.                                       |
| RF02 | O sistema deve permitir o cadastro de categorias de produtos.                         |
| RF03 | O sistema deve permitir o cadastro de fornecedores.                                   |
| RF04 | O sistema deve associar um produto a uma categoria.                                   |
| RF05 | O sistema deve associar produtos a fornecedores.                                      |
| RF06 | O sistema deve registrar a data de validade dos produtos.                             |
| RF07 | O sistema deve registrar a quantidade atual em estoque.                               |
| RF08 | O sistema deve registrar a quantidade mínima esperada para cada produto.              |
| RF09 | O sistema deve alertar quando a quantidade atual estiver abaixo da quantidade mínima. |
| RF10 | O sistema deve permitir aumentar a quantidade em estoque.                             |
| RF11 | O sistema deve permitir diminuir a quantidade em estoque.                             |
| RF12 | O sistema deve registrar movimentações de entrada e saída de estoque.                 |
| RF13 | O sistema deve permitir consultar todos os produtos cadastrados.                      |
| RF14 | O sistema deve permitir filtrar produtos por categoria.                               |
| RF15 | O sistema deve permitir consultar produtos vencidos.                                  |
| RF16 | O sistema deve permitir consultar produtos próximos do vencimento.                    |
| RF17 | O sistema deve armazenar informações no banco de dados MySQL.                         |
| RF18 | O sistema deve permitir conexão com banco de dados através do Java.                   |
| RF19 | O sistema deve tratar erros de conexão com o banco utilizando try/catch.              |
| RF20 | O sistema deve permitir atualização dos dados dos produtos.                           |

---

# Requisitos Não Funcionais (RNF)

Os requisitos não funcionais representam como o sistema deve funcionar.

| ID    | Requisito Não Funcional                                                              |
| ----- | ------------------------------------------------------------------------------------ |
| RNF01 | O sistema deverá ser desenvolvido na linguagem Java.                                 |
| RNF02 | O sistema deverá utilizar Java versão 17 ou 21.                                      |
| RNF03 | O sistema deverá utilizar o padrão Maven para gerenciamento do projeto.              |
| RNF04 | O sistema deverá utilizar o SGBD MySQL.                                              |
| RNF05 | O sistema deverá utilizar o driver mysql-connector-j versão 8.4.0.                   |
| RNF06 | O sistema deverá possuir estrutura organizada em pacotes (model, dao, conexao).      |
| RNF07 | O sistema deverá apresentar boa organização e legibilidade do código.                |
| RNF08 | O sistema deverá garantir integridade dos dados no banco.                            |
| RNF09 | O sistema deverá responder às consultas SQL corretamente.                            |
| RNF10 | O sistema deverá possuir tratamento de exceções para falhas de conexão.              |
| RNF11 | O sistema deverá permitir armazenamento persistente dos dados.                       |
| RNF12 | O sistema deverá possuir interface simples de utilização pelo terminal/console.      |
| RNF13 | O sistema deverá suportar operações básicas de CRUD (Create, Read, Update e Delete). |
| RNF14 | O banco de dados deverá seguir o modelo relacional.                                  |
| RNF15 | O sistema deverá permitir manutenção e expansão futura do código.                    |
