# Lista de User Stories

| ID   | Título      | Descrição                                                     | Requisitos Funcionais | Responsável |
|------|-------------|---------------------------------------------------------------|----------------------|--------------|
| US00 | Autenticação | Permite que funcionários realizem login, logout e recuperação de senha utilizando e-mail e senha. | Jadson |
| US01 | Manter Funcionario |  O usuário administrador do sistema pode realizar as operações de cadastrar, atualizar, consultar, desativar e listar os usuários comuns do sistema.| RF01 | Mariana |     
| US02 | Manter cliente | O sistema deve manter um cadastro de cliente que não possuir acesso ao sistema. Um cliente tem os atributos nome, id, endereço, contato. O usuário administrador do sistema pode realizar as operações de cadastrar, atualizar, consultar, desativar  clientes do sistema.| RF02 | Jadson |
| US03 | Gerenciar Aparelho | O sistema deve manter um cadastro de aparelho de um cliente. Um aparelho tem os atributos id, tipo, marca, modelo, numero_serie, cliente_id | RF03 | Mariana |
| US04 | Gerenciar Ordem_Serviço | Permite ao administrador abrir, consultar, atualizar, encerrar ordens de serviço | RF04 | Jadson |
| US05 | Gerenciar Serviço | Permite ao usuário administrador gerenciar o catálogo de serviços oferecidos pela assistência técnica, incluindo cadastro, consulta, atualização e desativação de serviços, com seu respectivo valor padrão.| RF05 | Mariana |
| US06 | Registrar OrdemServicoServico | Relaciona os serviços executados em uma ordem de serviço.| RF06 | Jadson |
| US07 | Gerenciar Equipamento | Permite ao administrador cadastrar, consultar, atualizar e desativar equipamentos/peças utilizados nos serviços. | RF07 | Mariana |
| US08 | Agendar Visita_Técnica | Permite ao administrador agendar visitas vinculadas a uma OS.| RF08 | Jadson |
| US09 |Gerenciar Conta_Receber | Gerencia automaticamente as contas a receber com valor_total da OS, data_emissão atual e data_vencimento calculada e permite registrar pagamentos (offline e online), incluindo marcar conta como paga. | RF09 | Mariana |
| US10 | AuditoriaLog | Registra as operações realizadas pelos funcionários.| RF10 | Jadson |
| US11 | Gerar Relatório | Permite gerar um relatórios com opções filtração e de exportação.| RF11 | Mariana |
| US12 | Controle de Garantia | Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.| RF12| Jadson |
| 
---
# Documento Lista de User Stories

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories**.

---

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento de Visão do projeto Sistema de Gestão de Assistência Técnica.

---

## Histórico de revisões

| Data       | Versão | Descrição                                     | Autor  |
|------------|--------|-----------------------------------------------|--------|
| 30/03/2026 | 0.1.0  | Criação inicial da lista de User Stories      | Jadson |
| 31/03/2026 | 1.0.0  | Documento completo com User Stories revisado  | Jadson |
| 17/04/2026 | 1.1.0  | Correção de inconsistências e adição de novas US12 e US13 | Mariana |
| 30/05/2026 |       | Correção de inconsistências e adição de nova US14 | Mariana |

---

# 📌 USER STORIES

---

## US00 - Autenticação

**Descrição:**
Permite que funcionários realizem autenticação no sistema por meio de e-mail e senha, além de permitir encerramento de sessão e recuperação de senha, garantindo acesso seguro às funcionalidades do sistema.

**Requisitos:** RF00.1, RF00.2, RF00.3

**Prioridade:** Essencial
**Estimativa:** 8h

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- Login realizado com e-mail e senha válidos
- E-mail ou senha incorretos retornam erro de autenticação
- Apenas usuários ativos podem acessar o sistema
- Usuário consegue encerrar sessão (logout) com sucesso
- Sessão expira após 30 minutos de inatividade

---

## US01 - Manter Funcionário

**Descrição:**  
Permite ao usuário administrador gerenciar funcionários, incluindo cadastro, atualização, consulta e desativação, com classificação em Técnico ou Administrativo.

**Requisitos:** RF01.1, RF01.2, RF01.3, RF01.4 

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Cadastrar funcionário com tipo TECNICO (especialidade, comissão) ou ADMINISTRATIVO (cargo, setor, bônus) 
- Consulta por nome, ID, CPF, tipo ou status retorna resultados corretos 
- Dados inválidos geram erro 
- Desativar funcionário - impede login
- CPF duplicado gera erro
- Funcionário com OS em aberto não pode ser desativado
- Listar todos os funcionários

---

## US02 - Manter Cliente

**Descrição:**  
Permite ao usuário administrador realizar todas as operações de gestão de clientes: cadastrar, atualizar, consultar e desativar clientes (PF e PJ).

**Requisitos:**  RF02.1, RF02.2, RF02.3, RF02.4 

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Cadastrar cliente com CPF (PF) ou CNPJ (PJ) válido  
- Atualizar dados de cliente existente  
- Consultar cliente por ID, nome, CPF, CNPJ ou contato
- Desativar cliente 
- Listar todos os cliente
- CPF/CNPJ duplicado gera erro
- Cliente com OS em aberto não pode ser desativado
- Validação de campos obrigatórios (nome, contato, documento)

---

## US03 - Gerenciar Aparelho

**Descrição:**
O sistema deve manter um cadastro de aparelho de um cliente. Um aparelho tem os atributos id, tipo, marca, modelo, numero_serie, cliente_id.

**Requisitos:** RF03.1, RF03.2, RF03.3, RF03.4

**Prioridade:** Essencial  
**Estimativa:**  6h

 **Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana 

**Testes de Aceitação:**
- Cadastrar um novo aparelho vinculado a um cliente_id existente
- Atualizar dados do aparelho
- Consultar aparelho por id, numero_serie, ou cliente_id
- Excluir (desativar logicamente) um aparelho. Um aparelho com OS em andamento não pode ser desativado

---

## US04 - Gerenciar Ordem_Serviço 

**Descrição:** 
Permite ao administrador e técnico consultar, editar, atualizar o status e encerrar ordens de serviço conforme o andamento do atendimento.

**Requisitos:** RF04.1, RF04.2, RF04.3, RF04.4, RF04.5.

**Prioridade:** Essencial  
**Estimativa:**  12h

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- Funcionário registra uma nova Ordem de Serviço para um cliente cadastrado.
- A Ordem de Serviço criada recebe status inicial ABERTA
- Editar Ordem de Serviço (descrição, técnico) - apenas se não finalizada
- Consultar Ordem de Serviço por ID, cliente, período ou status
- Encerrar Ordem de Serviço com status FINALIZADA e data_encerramento atual
- Técnico só vê Ordem de Serviço onde é responsável
- Ordem de Serviço com status FINALIZADA ou CANCELADA não pode ser editada
- Status disponíveis: ABERTA, EM_ANDAMENTO, AGUARDANDO_PECA, FINALIZADA, CANCELADA
- Técnico só altera Ordem de Serviço onde é responsável
- CANCELADA só permitido para Ordem de Serviço em ABERTA ou EM_ANDAMENTO

---

## US05 - Gerenciar Serviço

**Descrição:**  
Permite ao administrador gerenciar o catálogo de serviços oferecidos pela assistência técnica, incluindo cadastro, consulta, atualização e desativação de serviços, com seus respectivos valores padrão.

**Requisitos:** RF05.1, RF05.2, RF05.3, RF05.4  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana 


**Testes de Aceitação:**
- Cadastrar um novo serviço com nome, descrição, valor_padrao (R$)
- Consultar serviços por id, nome 
- Atualizar o valor_padrao de um serviço existente
- Tentar cadastrar um serviço com nome duplicado deve gerar um erro

---

### US06 - Registrar OrdemServicoServico

**Descrição:** 
Permite registrar os serviços executados em uma Ordem de Serviço, vinculando os serviços realizados ao atendimento do cliente, permitindo controle do que foi executado e composição do valor final

**Requisito Funcional Sugerido:** RF06.1,RF06.2, RF06.3

**Prioridade:** Essencial
**Estimativa:** 6h

 **Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**
- É possível vincular um ou mais serviços a uma Ordem de Serviço
- Apenas Ordens de Serviço abertas podem receber serviços
- Os serviços registrados ficam associados corretamente à OS
- O sistema calcula automaticamente o valor total dos serviços
- A comissão do técnico é calculada automaticamente com base nos serviços executados
- Não é permitido adicionar serviços em uma Ordem de Serviço finalizada

---

## US07 - Gerenciar Equipamento

**Descrição:**  
Permite cadastrar equipamentos, alterar e consultar equipamentos.

**Requisitos:** RF07.1, RF07.2, RF07.3, RF07.4  

**Prioridade:** Essencial  
**Estimativa:** 6h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana
  

**Testes de Aceitação:**  
- Equipamento cadastrado com sucesso 
- Consultar equipamento por ID, código, tipo ou modelo
- Código duplicado gera erro

---

## US08 - Agendar Visita_Técnica

**Descrição:**  
Permite ao administrador agendar visitas e ao técnico registrar a realização das visitas técnicas vinculadas a uma OS.

**Requisitos:** RF08.1, RF08.2, RF08.3 

**Prioridade:** Importante  
**Estimativa:** 5h  
 
**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Agendar visita com data_agendamento futura 
- OS inválida gera erro 
- Registrar realização com data_realizacao atual e resultado
- Apenas técnico designado pode registrar realização
- OS deve estar em ABERTA ou EM_ANDAMENTO
- Múltiplas visitas permitidas por OS 

---

## US09 - Gerenciar Conta_Receber

**Descrição:**  
Gerencia automaticamente as contas a receber com valor_total da OS, data_emissão atual e data_vencimento calculada.

**Requisitos:** RF09.1, RF09.2, RF09.3, RF09.4, RF09.5, RF09.6, RF09.7, RF09.8 

**Prioridade:** Essencial  
**Estimativa:** 8h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana 

**Testes de Aceitação:**  
- Conta gerada automaticamente ao encerrar a OS  
- Campos: valor, data_emissão, data_vencimento (30 dias), status_pagamento
- Valor correto 
- Data_emissão = data atual
- Data_vencimento calculada corretamente
- OS sem valor_total válido impede encerramento 
- Funcionário registra pagamento offline ou online da conta.
- Status alterado para PAGO com data_pagamento atual
- Conta já paga não pode ser alterada
- Conta vencida pode ser paga com multa
- Marcar conta como paga (status PAGO com data_pagamento atual)
- Conta com status PAGO não pode ser alterada novamente

---

## US10 - AuditoriaLog
Permite registrar automaticamente as ações realizadas pelos funcionários no sistema e consultar o histórico de operações, garantindo rastreabilidade e controle das atividades.

**Requisitos:** RF10.1, RF10.2  

**Prioridade:** Essencial  
**Estimativa:** 5h  

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Jadson
- Revisor: Mariana
- Testador: Jadson

**Testes de Aceitação:** 
- O sistema registra automaticamente ações realizadas por funcionários
- Cada registro de auditoria contém informações como usuário, ação realizada e data/hora
- Ações críticas do sistema são obrigatoriamente registradas em log
- O administrador consegue consultar o histórico de auditoria
- É possível filtrar logs por usuário, data ou tipo de ação
- Registros de auditoria não podem ser alterados ou excluídos
- O sistema mantém histórico completo das operações realizadas
- Tentativas de acesso ou ações inválidas também são registradas no log

---

## US11 - Gerar Relatório

**Descrição:**
Permite gerar um relatório de ordens de serviço filtrado, com opção de exportação (PDF/CSV).

**Requisitos:** RF11.1, RF11.2, RF11.3

**Prioridade:** Importante
**Estimativa:** 6h

**Responsáveis:**
- Analista: Mariana
- Desenvolvedor: Mariana
- Revisor: Jadson
- Testador: Mariana

**Testes de Aceitação:**
- Relatório gerado com sucesso no período selecionado
- Filtro por status funciona
- Filtro por técnico funciona
- Exibe: ID da OS, data_abertura, data_encerramento, status, valor_total
- Listar todos os aparelhos de um cliente específico
- Listar OS por cliente específico
- Listar OS por funcionário específico
- Listar OS por aparelhos de um cliente específico
- Listar OS por periodo
- Listar OS por status
- A listagem de serviços para uso em uma nova OS deve exibir apenas os serviços com status = ATIVO
- Relatório de produtividade por técnico/período
- Exibe totalizadores (quantidade de OS e valor total no período)
- Período inválido (data_fim < data_início) gera erro
- Opção de exportar para PDF e CSV funciona

---

## US12 - Controle de Garantia 

**Descrição:**
Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.

**Requisitos:** RF12.1, RF12.2, RF12.3

**Prioridade:** Importante
**Estimativa:** 5h

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Jadson
- Revisor: Mariana
- Testador: Jadson

**Testes de Aceitação:**
- Exibe OS com garantia ativa (dentro do prazo)
- Exibe OS com garantia expirada (data_encerramento + garantia_dias < data atual)
- Calcular data_fim_garantia
- Alerta visual para garantias que vencem em até 7 dias
- Consulta por cliente ou equipamento
- Exibe quantidade de dias restantes de garantia
- Permite registrar atendimento em garantia (nova OS vinculada)
- Verificar garantia ativa

---


# Matriz de Rastreabilidade - Requisitos Funcionais x User Stories

| ID    | Requisito Funcional            | User Stories | Total |
| ------| -------------------------------| ------------ | ----- |
| RF00  | Autenticação                   | US00         |   1   | 
| RF01  | Manter Funcionário             | US01         |   1   |
| RF02  | Manter Cliente                 | US02         |   1   |
| RF03  | Gerenciar Aparelho             | US03         |   1   |
| RF04  | Gerenciar Ordem_Serviço        | US04         |   1   |
| RF05  | Gerenciar Serviço              | US05         |   1   |
| RF06  | Registrar OrdemServicoServico  | US06         |   1   | 
| RF07  | Gerenciar Equipamento          | US07         |   1   |
| RF08  | Agendar Visita_Técnica         | US08         |   1   |
| RF09  | Gerenciar Conta_Receber        | US09         |   1   |
| RF10  | AuditoriaLog                   | US10         |   1   |
| RF11  | Gerar Relatório                | US11         |   1   |
| RF12  | Controle de Garantia           | US12         |   1   |


## 📊 Estatísticas

- **Total de Requisitos Funcionais:** 13
- **Total de User Stories:** 13
- **Média de US por RF:** 1:1
- **Total estimado de desenvolvimento:** 87 horas

## 🔄 Mapeamento US × Perfis de Usuário

| Perfil | User Stories |
|:-------|:-------------|
| Técnico |	US00, US02, US03, US04, US06, US10 |
| Administrativo | US00, US01, US02, US03, US04, US05, US06, US07, US08, US09, US10, US11, US12 |

