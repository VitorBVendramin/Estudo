# 🏪 Sistema de Gestão de Clientes e Vendas

Sistema desenvolvido em Python com banco de dados SQLite para gerenciamento completo de clientes, produtos e vendas.

---

## 🚀 Funcionalidades

### 👤 Clientes
- ✅ Cadastrar cliente
- ✅ Buscar todos os clientes
- ✅ Buscar por nome ou ID
- ✅ Atualizar dados do cliente
- ✅ Deletar cliente

### 📦 Produtos
- ✅ Adicionar produto
- ✅ Remover produto
- ✅ Atualizar estoque
- ✅ Listar produtos
- ✅ Buscar por nome ou ID

### 💰 Vendas
- ✅ Registrar venda com validação de estoque
- ✅ Buscar vendas por cliente
- ✅ Buscar vendas por produto
- ✅ Relatório de vendas por período
- ✅ Produto mais vendido

---

## 🗄️ Banco de dados

### Tabela: clientes
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária |
| nome | TEXT | Nome do cliente |
| email | TEXT | Email do cliente |
| telefone | TEXT | Telefone do cliente |
| cpf | TEXT | CPF do cliente |
| endereco | TEXT | Endereço do cliente |

### Tabela: produtos
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária |
| nome | TEXT | Nome do produto |
| quantidade | INTEGER | Quantidade em estoque |
| preco | REAL | Preço do produto |

### Tabela: vendas
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária |
| cliente_id | INTEGER | Chave estrangeira → clientes(id) |
| produto_id | INTEGER | Chave estrangeira → produtos(id) |
| quantidade | INTEGER | Quantidade vendida |
| valor | REAL | Valor da venda |
| data | TEXT | Data da venda |

---

## 📁 Estrutura do projeto

```
sistema-gestao-clientes/
│
├── database/
│   └── database.py        ← conexão e criação das tabelas
│
├── models/
│   ├── cliente.py         ← operações CRUD de clientes
│   ├── produto.py         ← operações CRUD de produtos
│   └── venda.py           ← operações de vendas e relatórios
│
├── main.py                ← menu principal
└── README.md
```

---

## ⚙️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/VitorBVendramin/sistema-gestao-clientes.git
cd sistema-gestao-clientes
```

**2. Crie o banco de dados**
```bash
python database/database.py
```

**3. Execute o sistema**
```bash
python main.py
```

> Nenhuma biblioteca externa necessária.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

---

## 📈 Status

🟡 Em desenvolvimento

---

## 👨‍💻 Autor

**Vitor Brunelli Vendramin**  
[![GitHub](https://img.shields.io/badge/GitHub-VitorBVendramin-181717?style=flat&logo=github)](https://github.com/VitorBVendramin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vitorvendramin-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/vitorvendramin/)