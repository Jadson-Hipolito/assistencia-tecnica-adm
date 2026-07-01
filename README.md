# 🛠️ Sistema de Assistência Técnica

## 📌 Objetivo

O Sistema de Assistência Técnica facilita o gerenciamento de clientes, equipamentos, ordens de serviço, contas a receber e notificações, com foco em organização e eficiência no atendimento técnico.

---

## 🚀 Funcionalidades

* Cadastro e gerenciamento de clientes
* Cadastro de equipamentos usados e serviços executados
* Criação, atualização e controle de ordens de serviço
* Gestão de funcionários e técnicos
* Controle financeiro de contas a receber
* Relatórios de clientes, funcionários e ordens

---

## 💻 Tecnologias Utilizadas

* **Python 3.12+**
* **FastAPI**
* **SQLite**
* **SQLAlchemy**
* **React**
* **Vite**
* **Vitest**
* **Git & GitHub**

---

## 📂 Estrutura do Projeto

* `backend/` → API FastAPI e lógica do servidor
  * `backend/app/` → aplicação FastAPI, modelos, routers e configuração de banco
  * `backend/tests/unit/` → testes unitários backend
  * `backend/tests/integration/` → testes de integração backend
* `frontend/` → aplicativo React e testes Vitest
* `docs/` → documentação do projeto
* `data/` → arquivos persistentes e banco SQLite

---

## 🔧 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Jadson-Hipolito/assistencia-tecnica-adm
cd assistencia-tecnica-adm
```

### 2. Criar e ativar o ambiente virtual Python

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências do backend

```bash
pip install -r backend/requirements.txt
```

### 4. Executar o servidor backend

A partir da raiz do projeto:

```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

A partir da pasta `backend`:

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Ou execute o script de inicialização:

```bash
./start_server.sh
```

---

## 🧪 Testes

### Backend

```bash
.venv/bin/python -m pytest -q backend/tests/unit backend/tests/integration
```

### Frontend

```bash
cd frontend
npm install
npm run test
```

Testes frontend específicos:

```bash
npm run test:unit
npm run test:integration
npm run test:coverage
```

---

## 🛠️ Frontend

O frontend está em `frontend/` e usa React com Vite. Os testes são executados com Vitest.

---

## 📂 Notas sobre a organização

* `backend/` agora é um pacote Python com `backend/__init__.py`
* A aplicação backend expõe o app em `backend.app.main`
* Os testes backend foram movidos para `backend/tests/unit` e `backend/tests/integration`

---

## 📚 Documentação

* 📄 [Documento de Visão](docs/doc-visao.md)
* 📊 [Modelo de Dados](docs/doc-modelos.md)
* 📋 [User Stories](docs/doc-userstories.md)
* 🏗️ [Arquitetura do Software](docs/arquitetura.md)

---

## 👥 Equipe

* Jadson Hipólito de Almeida
* Mariana Araújo de Medeiros

---

## ✅ Status do Projeto

🚧 Em desenvolvimento
