# Relatório de Testes de Módulo/Sistema

## Responsabilidade do Testador
- Testador: Equipe de QA
- Objetivo: validar o fluxo de login e registrar problemas de compatibilidade entre frontend e backend.

## Legenda
- Teste: Código ou identificação do teste.
- Descrição: Passos detalhados do teste.
- Especificação: Verificação da função em relação ao caso de uso.
- Resultado: Qualificação do teste e evidências de erro quando houver.

## US001 – Autenticação de Usuário

### Teste 01: Login
A1 – Efetuar login no sistema

A1.1. O ator preenche o campo de email;

A1.2. O ator preenche o campo de senha;

A1.3. O ator clica no botão Entrar;

A1.4. O sistema envia requisição POST para `/auth/login`;

A1.5. O sistema retorna token de acesso e redireciona para a tela principal;

A1.6. Fim do fluxo.

Especificação: A função implementada deve enviar as credenciais para `/auth/login` e receber `access_token`, `token_type` e `user`.

Resultado: Identificado problema no front-end de login.
- O código está configurado de forma inconsistente entre a página estática (`frontend/login.html`) e o restante da aplicação.
- O fluxo correto deve usar `/auth/login`, mas a implementação anterior aparenta tratar o endpoint como `/login` em algumas partes do frontend.
- Foi corrigido o acesso no `frontend/login.html` para usar explicitamente `http://localhost:8000/auth/login`.

## US002 – Compatibilidade de Rotas da API

### Teste 02: Acesso a endpoint de contas a receber
A2 – Acessar lista de contas a receber

A2.1. O ator faz login corretamente;

A2.2. O ator acessa o recurso `/api/contas_receber`;

A2.3. O sistema retorna a lista de contas a receber;

A2.4. Fim do fluxo.

Especificação: O backend deve expor o endpoint `/api/contas_receber` para compatibilidade com os testes existentes.

Resultado: Falha de compatibilidade de rota.
- O backend originalmente expõe `/api/contas-receber`, enquanto os testes usam `/api/contas_receber`.
- É necessária a criação de aliases para aceitar ambas as formas.

### Teste 03: Acesso a endpoint de equipamentos usados
A3 – Registrar equipamento usado em serviço

A3.1. O ator faz login corretamente;

A3.2. O ator acessa o recurso `/api/equipamentos_usado`;

A3.3. O sistema cria o registro de equipamento usado e retorna ID;

A3.4. Fim do fluxo.

Especificação: O backend deve fornecer o endpoint `/api/equipamentos_usado` para os testes de integração.

Resultado: Falha de implementação.
- Não existia rota `/api/equipamentos_usado` no backend.
- Foi identificada a necessidade de um novo roteador para corresponder ao requisito de teste.

## Relatório de Bugs e Providências

Responsabilidade do Gerente

| Teste | Providência | Tarefas/Tipo |
| --- | --- | --- |
| Teste 01 – Login | Corrigir o front-end para usar `/auth/login` em todas as chamadas de login. | Tarefa: Bug de Implementação |
| Teste 02 – Acesso a Contas a Receber | Corrigir aliases de rota para `/api/contas_receber` e `/api/contas-receber`. | Tarefa: Bug de Implementação |
| Teste 03 – Equipamentos Usados | Implementar o endpoint `/api/equipamentos_usado` e validar a rota. | Tarefa: Bug de Implementação |

## Observações Gerais
- O fluxo de login é crítico: a URL do endpoint deve ser unificada para evitar falhas de autenticação.
- Os testes atuais apresentam inconsistência de nomenclatura de rotas entre frontend e backend.
- Recomenda-se revisar todos os endpoints de API para manter alias compatíveis com os testes existentes.
