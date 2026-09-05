# Sistema de Gestão de Suporte de TI e Ativos

Sistema de gestão de suporte técnico e ativos de TI desenvolvido em **Python + MySQL**.

O sistema permite gerir usuários, chamados de suporte, categorias, ativos, atribuições e histórico das operações realizadas.

## Tecnologias

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- Git
- GitHub

## Funcionalidades

- Gestão de usuários
- Gestão de categorias
- Gestão de chamados
- Gestão de ativos de TI
- Atribuição de ativos aos usuários
- Devolução de ativos
- Comentários em chamados
- Histórico de alterações
- Consultas
- Relatórios
- Controle de acesso dos usuários
- Persistência dos dados em MySQL

## Acesso ao sistema

Ao criar/inicializar o banco de dados, o sistema cria automaticamente uma conta administrativa.

### Conta ADMIN inicial

```text
Nome: ADMIN
Email: admin@gmail.com
Estado: TRUE
```

O campo `estado` controla o acesso do usuário ao sistema:

- `TRUE` → possui acesso
- `FALSE` → não possui acesso

A conta `ADMIN` é responsável por adicionar novos usuários ao sistema.

Não existe cadastro de usuários pelo próprio usuário.

## Chamados

Os chamados possuem diferentes níveis de prioridade:

- `BAIXA`
- `NORMAL`
- `ALTA`
- `CRITICA`

### Estados dos chamados

- `ABERTO`
- `EM_ATENDIMENTO`
- `AGUARDANDO`
- `RESOLVIDO`
- `FECHADO`
- `CANCELADO`

O sistema possui regras para controlar as alterações dos estados dos chamados.

## Ativos

O sistema permite cadastrar e controlar equipamentos e outros ativos de TI.

Cada ativo possui um número de patrimônio único.

### Regras dos ativos

- O patrimônio não pode ser duplicado.
- Um ativo descartado não pode ser atribuído.
- Um ativo em manutenção não deve ser atribuído.
- Um ativo disponível pode ser atribuído.
- Um ativo em uso deve possuir uma atribuição ativa.
- Um ativo não pode possuir duas atribuições ativas.
- A devolução encerra a atribuição e mantém o histórico.

## Banco de dados

O sistema utiliza **MySQL** para armazenamento dos dados.

### Principais tabelas

- `usuarios`
- `categorias`
- `chamados`
- `ativos`
- `atribuicoes`
- `comentarios`
- `historico_chamados`

As tabelas utilizam **chaves primárias (PK)** e **chaves estrangeiras (FK)** para manter os relacionamentos e a integridade dos dados.

## Configuração

As informações de acesso ao banco de dados são armazenadas em variáveis de ambiente através do arquivo `.env`.

### Exemplo do `.env`

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=seu_banco
```

O arquivo `.env` não deve ser enviado para o GitHub.

Para configurar o projeto, utilize o `.env.example`:

```env
MYSQL_HOST=localhost
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_DATABASE=seu_banco
```

## Instalação

Clone o repositório:

```bash
git clone git@github.com:EdilBorg/software-projects.git
```

Entre no projeto:

```bash
cd software-projects/sistema-suporte-ti
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install mysql-connector-python python-dotenv
```

Configure o arquivo `.env` e execute:

```bash
python main.py
```

## Estrutura do projeto

```text
sistema-suporte-ti/
│
├── Banco.py
├── main.py
├── usuario.py
├── chamados.py
├── ativos.py
├── atribuicoes.py
├── categorias.py
├── utilis.py
│
├── .env.example
├── .gitignore
└── README.md
```

## Menu principal

```text
1 - Gestão de usuários
2 - Categorias
3 - Chamados
4 - Ativos
5 - Atribuição de ativos
6 - Consultas / Histórico
7 - Relatórios
0 - Sair
```

## Integridade dos dados

O sistema utiliza:

- Chaves primárias
- Chaves estrangeiras
- Campos obrigatórios
- Valores únicos
- Validação das operações
- Regras de negócio
- Controle de atribuição dos ativos
- Preservação do histórico
- Tratamento de erros do MySQL

## Objetivo do projeto

Este projeto tem como objetivo aplicar conhecimentos de:

- Python
- Programação modular
- SQL
- MySQL
- CRUD
- Banco de dados relacionais
- Relacionamentos entre tabelas
- Chaves primárias e estrangeiras
- Regras de negócio
- Controle de acesso
- Tratamento de erros
- Git e GitHub

## Status

**Em desenvolvimento**

O projeto está sendo desenvolvido por etapas e novas funcionalidades serão adicionadas durante o desenvolvimento.

## Autor

**Edil Borges**

Projeto desenvolvido para fins de estudo, prática e portfólio.