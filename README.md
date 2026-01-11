# API Smartmart Dashboard

API REST para gerenciamento de produtos e análise de vendas. Fornece endpoints para cadastro, edição, importação via CSV e consulta de dados. Desenvolvido com **Django REST Framework**, **PostgreSQL** e **Docker**.

<br>

## Tecnologias Utilizadas

- **Python 3.14** - Linguagem de programação do projeto
- **Django Rest Framework** — Framework para APIs REST
- **psycopg2-binary** — Driver PostgreSQL para Python
- **python-dotenv** — Gerenciamento de variáveis de ambiente
- **PostgreSQL 16** — Banco de dados relacional
- **Docker** — Containerização de ambientes
- **Poetry** — Gerenciamento de dependências e ambientes via `pyproject.toml`
- **Black, Flake8 e isort** – Formatação e linting de código.

<br>

## Estrutura do Projeto

```
api_smartmart_dashboard/
├───api
│   ├───admin.py
│   ├───apps.py
│   ├───models.py
│   ├───tests.py
│   ├───views.py
│   ├───__init__.py
│   │
│   ├───application
│   │   └───use_cases
│   │       ├───category
│   │       │   ├───create_category.py
│   │       │   └───list_category.py
│   │       │
│   │       ├───product
│   │       │   ├───create_product.py
│   │       │   ├───export_product.py
│   │       │   ├───list_product.py
│   │       │   └───upload_product.py
│   │       │
│   │       └───sale
│   │           ├───export_sale.py
│   │           ├───get_sale.py
│   │           ├───list_sales.py
│   │           └───update_sale.py
│   │
│   ├───domain
│   │   ├───entities
│   │   │   ├───category_entity.py
│   │   │   ├───product_entity.py
│   │   │   └───sale_entity.py
│   │   │
│   │   └───repositories
│   │       ├───category_repository.py
│   │       ├───product_repository.py
│   │       └───sale_repository.py
│   │
│   └───infrastructure
│       ├───__init__.py
│       │
│       ├───database
│       │   ├───models
│       │   │   ├───categories_model.py
│       │   │   ├───products_model.py
│       │   │   └───sales_model.py
│       │   │
│       │   └───repositories
│       │       ├───category_repository.py
│       │       ├───product_repository.py
│       │       └───sale_repository.py
│       │
│       └───django
│           ├───urls.py
│           │
│           ├───serializers
│           │   ├───category_serializer.py
│           │   ├───product_serializer.py
│           │   └───sale_serializer.py
│           │
│           └───views
│               ├───category
│               │   └───category_view.py
│               │
│               ├───product
│               │   ├───export_product_view.py
│               │   ├───import_product_view.py
│               │   └───product_view.py
│               │
│               └───sale
│                   ├───export_sale_view.py
│                   └───sale_view.py
├───tests
│   ├───application
│   │   ├───category
│   │   │   ├───test_create_category.py
│   │   │   └───test_list_category.py
│   │   │
│   │   ├───product
│   │   │   ├───test_create_product.py
│   │   │   ├───test_export_product.py
│   │   │   ├───test_list_product.py
│   │   │   └───test_upload_product.py
│   │   │
│   │   └───sale
│   │       ├───test_export_sale.py
│   │       ├───test_get_sale.py
│   │       ├───test_list_sale.py
│   │       └───test_update_sale.py
│   │
│   └───domain
│       ├───entities
│       │   ├───test_category_entity.py
│       │   ├───test_product_entity.py
│       │   └───test_sale_entity.py
│       │
│       └───repositories
│           ├───test_category_repository.py
│           ├───test_product_repository.py
│           └───test_sale_repository.py
│
├───core
│   ├───asgi.py
│   ├───settings.py
│   ├───urls.py
│   ├───wsgi.py
│   └───__init__.py
│
├───docker
│   └───postgres
│       └───init.sql
│
├───.env
├───.flake8
├───.gitignore
├───docker-compose.yml
├───manage.py
├───poetry.lock
├───pyproject.toml
└───README.md
```

<br>

## Arquitetura

A API Smartmart Dashboard foi construída seguindo os princípios da **Clean Architecture**, **Separation of Concerns** e **Dependency Inversion**, com uma abordagem de **Domain-Driven Design (DDD simplificado)**, visando manter o código **organizado**, **desacoplado**, **testável** e **fácil de evoluir**.

### Visão Geral

O fluxo da aplicação segue o padrão:

```
HTTP Request
   ↓
Django View / Serializer
   ↓
Use Case
   ↓
Domain (Entities + Repositories)
   ↓
Infrastructure (Repositório Django ORM)
   ↓
Database
   ↓
Serializer
   ↓
HTTP Response
```

<br>

## Camadas

**Views / Serializers**

Traduz requisições HTTP para objetos de domínio e respostas de volta para JSON, sem conter regras de negócio.

<br>

**Application (use cases)**

Contém os casos de uso da aplicação.

<br>

**Domain**

Contém as entidades e interfaces de repositório, definindo as regras de negócio puras, sem depender de frameworks ou banco de dados.

<br>

**Infrastructure**

implementa os detalhes técnicos, como banco de dados, ORM e repositórios.

<br>

## Infraestrutura

A aplicação e o banco de dados rodam em containers separados, comunicando-se por meio de uma Docker Network. O banco PostgreSQL é inicializado automaticamente, e a persistência dos dados é feita com o uso de volumes Docker.

<br>

## Rotas

| Método   | Rota                | Descrição                                                               |
| -------- | ------------------- | ----------------------------------------------------------------------- |
| **POST** | `/categories/`      | Adicionar categoria via JSON                                            |
| **GET**  | `/categories/`      | Listar categorias                                                       |
| **POST** | `/products/`        | Adicionar produto via JSON                                              |
| **GET**  | `/products/`        | Listar produtos com ou sem o uso de filtros via JSON                    |
| **GET**  | `/products/export/` | Baixar arquivo.csv com todos os produtos que estão no banco de dados    |
| **POST** | `/products/import/` | Adicionar produtos por meio de um arquivo.csv                           |
| **GET**  | `/sales/`           | Listar vendas                                                           |
| **PUT**  | `/sales/<int:id>/`  | Alterar informações da venda com base no id da venda                    |
| **PUT**  | `/sales/export/`    | Baixar arquivo.csv com todas as vendas que estão no banco de dados vend |

<br>

## Pré-requisitos

- **Docker**
- **Docker Compose**
- **Não é necessário instalar Python ou PostgreSQL localmente**

<br>

## Variáveis de Ambiente (**.env**)

Crie um arquivo **.env** na raiz do projeto:

```env
NAME_DB=smartmart
USER_DB=root_smartmart
PASSWORD_DB=rootpassword
HOST_DB=localhost
PORT_DB=5432
```

<br>

## Docker

Subir a aplicação + banco de dados

```bash
docker compose up --build
```

A API ficará disponível em:

```
http://localhost:8000
```

Banco de dados ficará disponível em:

```
http://localhost:5432
```

<br>

## Banco de Dados

- PostgreSQL 16
- Inicializado automaticamente via init.sql
- Persistência via volume Docker

### Acessar o banco dentro do container:

```bash
docker exec -it smartmart_db psql -U root_smartmart smartmart
```
