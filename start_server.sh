#!/bin/bash
# Parar qualquer servidor antigo na porta 8000
fuser -k 8000/tcp 2>/dev/null || true

# Ir para a raiz do projeto
cd "$(dirname "$0")"

# Iniciar servidor
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
