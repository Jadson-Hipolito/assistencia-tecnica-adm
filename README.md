# 🛠️ Sistema de Assistência Técnica

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge\&logo=react\&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge\&logo=vite\&logoColor=white)
![License](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=for-the-badge)

</p>

---

## 📖 Sobre o Projeto

O **Sistema de Assistência Técnica** é uma aplicação web desenvolvida para auxiliar empresas de assistência técnica no gerenciamento de clientes, equipamentos, ordens de serviço, funcionários e controle financeiro.

O projeto utiliza uma arquitetura baseada em **FastAPI** no backend e **React + Vite** no frontend, seguindo boas práticas de organização, testes automatizados e separação de responsabilidades.

---

## ✨ Funcionalidades

### 👥 Clientes

* Cadastro de clientes
* Edição de informações
* Exclusão de registros
* Pesquisa de clientes

### 📱 Equipamentos

* Cadastro de equipamentos
* Associação ao cliente
* Histórico de serviços

### 🛠️ Ordens de Serviço

* Criação de OS
* Atualização de status
* Controle de serviços executados
* Consulta de ordens

### 👨‍💼 Funcionários

* Cadastro de técnicos
* Controle de permissões

### 💰 Financeiro

* Contas a receber
* Controle de pagamentos
* Situação financeira

### 📊 Relatórios

* Clientes
* Funcionários
* Ordens de serviço

---

# 🏗 Arquitetura

```text
React + Vite
       │
       ▼
    FastAPI
       │
 SQLAlchemy ORM
       │
     SQLite
```

---

# 🖥️ Tecnologias Utilizadas

| Tecnologia   | Finalidade      |
| ------------ | --------------- |
| Python 3.12+ | Backend         |
| FastAPI      | API REST        |
| SQLAlchemy   | ORM             |
| SQLite       | Banco de dados  |
| React        | Interface       |
| Vite         | Build Frontend  |
| Vitest       | Testes Frontend |
| Pytest       | Testes Backend  |
| Git          | Versionamento   |

---

# 🔐 Credenciais Padrão

| Campo     | Valor                   |
| --------- | ----------------------- |
| **Email** | `admin@assistencia.com` |
| **Senha** | `admin123`              |

---

# 📁 Estrutura do Projeto

```text
assistencia-tecnica-adm/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── tests/
│       ├── unit/
│       └── integration/
│
├── frontend/
│
├── docs/
│
├── data/
│
├── README.md
└── requirements.txt
```

---

# ⚙️ Instalação

## Clonar o repositório

```bash
git clone https://github.com/Jadson-Hipolito/assistencia-tecnica-adm.git

cd assistencia-tecnica-adm
```

---

## Criar ambiente virtual

### Linux / WSL

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv

.venv\Scripts\activate
```

---

## Instalar dependências

```bash
pip install -r backend/requirements.txt
```

---

# ▶️ Executando o Backend

Na raiz do projeto:

```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Ou

```bash
cd backend

uvicorn app.main:app --reload
```

Também é possível utilizar

```bash
./start_server.sh
```

---

# 💻 Executando o Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🧪 Testes

## Backend

```bash
pytest backend/tests/unit backend/tests/integration -q
```

## Frontend

```bash
cd frontend

npm test
```

### Testes específicos

```bash
npm run test:unit

npm run test:integration

npm run test:coverage
```

---

# 📚 Documentação

| Documento          | Descrição                 |
| ------------------ | ------------------------- |
| Documento de Visão | `docs/doc-visao.md`       |
| Modelo de Dados    | `docs/doc-modelos.md`     |
| User Stories       | `docs/doc-userstories.md` |
| Arquitetura        | `docs/arquitetura.md`     |

---

# 📌 API

Após iniciar o backend:

Swagger

```text
http://localhost:8000/docs
```

ReDoc

```text
http://localhost:8000/redoc
```

---

# 🚀 Roadmap

* [x] Cadastro de Clientes
* [x] Cadastro de Equipamentos
* [x] Ordens de Serviço
* [x] Controle Financeiro
* [x] Sistema de Funcionários
* [x] API REST
* [x] Testes Automatizados
* [ ] Dashboard Gerencial
* [ ] Notificações em Tempo Real
* [ ] Backup Automático
* [ ] Deploy em Produção

---

# 👨‍💻 Equipe

**Jadson Hipólito de Almeida**

**Mariana Araújo de Medeiros**

---

# 📈 Status do Projeto

> 🚧 **Em desenvolvimento**

Novas funcionalidades estão sendo implementadas continuamente visando tornar o sistema cada vez mais completo e robusto.
