# 🏪 Sistema de Gestão de Clientes e Vendas

Sistema desenvolvido em Python com banco de dados SQLite para gerenciamento completo de clientes, produtos e vendas.

---

## 🚀 Funcionalidades

### 👤 Clientes
- ✅ Cadastrar cliente com validação de CPF, email e telefone
- ✅ Buscar todos os clientes
- ✅ Buscar por nome ou ID
- ✅ Atualizar dados do cliente
- ✅ Deletar cliente

### 📦 Produtos
- ✅ Adicionar produto
- ✅ Listar todos os produtos
- ✅ Buscar por nome ou ID
- ✅ Atualizar produto
- ✅ Remover produto

### 💰 Vendas
- ✅ Registrar venda com validação de estoque
- ✅ Listar vendas
- ✅ Vendas por produto
- ✅ Produtos mais vendidos

### 📊 Relatórios
- ✅ Vendas por período
- ✅ Histórico de compras por cliente
- ✅ Produtos com estoque baixo
- ✅ Faturamento total

### 🔐 Autenticação
- ✅ Login com usuário e senha
- ✅ Senha criptografada com SHA-256
- ✅ Níveis de acesso por cargo (Master, Operador, Aprendiz)
- ✅ Criação automática do usuário Master no primeiro acesso

---

## 👥 Níveis de acesso

| Cargo | Acesso |
|-------|--------|
| Master | Acesso total + gerenciamento de usuários |
| Operador | Clientes, produtos e vendas |
| Aprendiz | Apenas consultas |

---

## 🔑 Reset de senha

Caso perca o acesso ao sistema, rode o script de reset no terminal:

```bash
python reset_admin.py
```

O script solicita uma nova senha para o usuário Master sem precisar acessar o banco manualmente.

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

### Tabela: usuarios
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária |
| nome | TEXT | Nome do usuário |
| login | TEXT UNIQUE | Login do usuário |
| senha | TEXT | Senha criptografada com SHA-256 |
| cargo | TEXT | Cargo do usuário |

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
│   ├── produtos.py        ← operações CRUD de produtos
│   ├── venda.py           ← operações de vendas
│   ├── relatorios.py      ← relatórios do sistema
│   └── validacoes.py      ← validação de dados
│
├── main.py                ← menu principal
├── reset_admin.py         ← script para reset de senha do Master (sistema local, caso não fosse, teria que fazer reset por email ou formas seguras)
└── README.md
```

---

## ⚙️ Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/VitorBVendramin/Estudo/tree/main/Python/projetos/sistema-gestao-clientes
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

> Na primeira execução o sistema solicitará a criação do usuário Master.

> Nenhuma biblioteca externa necessária. O projeto usa apenas módulos nativos do Python.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📈 Status

🟢 Concluído

---

## 👨‍💻 Autor

**Vitor Brunelli Vendramin**  
[![GitHub](https://img.shields.io/badge/GitHub-VitorBVendramin-181717?style=flat&logo=github)](https://github.com/VitorBVendramin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-vitorvendramin-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/vitorvendramin/)