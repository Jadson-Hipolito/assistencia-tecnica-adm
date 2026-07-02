# Contagem de Pontos de Função - Sistema de Gestão de Assistência Técnica

## 1. Introdução

Este documento apresenta a Contagem de Pontos de Função (Function Point Analysis - FPA) do Sistema de Gestão de Assistência Técnica, elaborada com base no Documento de Visão, Lista de Requisitos Funcionais, User Stories e Modelo Conceitual.

Foram utilizadas as três abordagens recomendadas pelo IFPUG:

- Contagem Indicativa (Ci)
- Contagem Estimativa (Ce)
- Contagem Detalhada (Cd)

---

# 2. Base da Contagem

A contagem foi realizada considerando:

- Documento de Visão
- Requisitos Funcionais (RF00–RF12)
- User Stories (US00–US12)
- Modelo Conceitual
- Casos de Uso

---

# 3. Identificação das Funções de Dados

## 3.1 Arquivos Lógicos Internos (ALI)

| Nº | ALI | Requisito |
|---|-------------------------|---------|
| 1 | Funcionário | RF01 |
| 2 | Cliente | RF02 |
| 3 | Aparelho | RF03 |
| 4 | Ordem de Serviço | RF04 |
| 5 | Serviço | RF05 |
| 6 | OrdemServicoServico | RF06 |
| 7 | Equipamento | RF07 |
| 8 | Visita Técnica | RF08 |
| 9 | Conta a Receber | RF09 |
|10 | Garantia | RF12 |
|11 | Auditoria Log | RF10 |

Total de ALIs: **11**

---

## 3.2 Arquivos de Interface Externa (AIE)

| Nº | Interface | Requisito |
|---|------------------------|---------|
|1|Gateway de Pagamento|RF09|

Total de AIEs: **1**

---

# 4. Contagem Indicativa (Ci)

Segundo o método IFPUG:

- ALI = 35 PF
- AIE = 15 PF

## Cálculo

```
Ci = (11 × 35) + (1 × 15)

Ci = 385 + 15

Ci = 400 PF
```

---

# 5. Contagem Estimativa (Ce)

## 5.1 Funções de Dados

| Tipo | Quantidade | PF Unitário | Total |
|------|-----------:|------------:|------:|
| ALI | 11 | 7 | 77 |
| AIE | 1 | 5 | 5 |

Subtotal = **82 PF**

---

## 5.2 Funções de Transação

### Entradas Externas (EE)

| Operação |
|-----------|
| Login |
| Alterar senha |
| Logout |
| Cadastrar Funcionário |
| Alterar Funcionário |
| Desativar Funcionário |
| Cadastrar Cliente |
| Alterar Cliente |
| Desativar Cliente |
| Cadastrar Aparelho |
| Alterar Aparelho |
| Desativar Aparelho |
| Abrir Ordem de Serviço |
| Editar Ordem de Serviço |
| Atualizar Status |
| Encerrar Ordem |
| Cadastrar Serviço |
| Alterar Serviço |
| Desativar Serviço |
| Adicionar Serviço |
| Remover Serviço |
| Cadastrar Equipamento |
| Alterar Equipamento |
| Atualizar Estoque |
| Registrar Visita |
| Reagendar Visita |
| Cancelar Visita |
| Registrar Pagamento Offline |
| Estornar Pagamento |
| Registrar Atendimento em Garantia |
| Consultar Logs |

Total EE = **31**

---

### Consultas Externas (CE)

| Operação |
|-----------|
| Consultar Funcionário |
| Consultar Cliente |
| Consultar Aparelho |
| Consultar Ordem de Serviço |
| Consultar Serviço |
| Consultar Equipamento |
| Consultar Garantia |
| Emitir Relatórios |
| Filtrar Relatórios |
| Consultar Auditoria |
| Consultar Conta |
| Consultar Visitas |
| Consultar Estoque |
| Consultar Serviços Executados |

Total CE = **14**

---

### Saídas Externas (SE)

| Operação |
|-----------|
| Emitir Comprovante |
| Exportar Relatório PDF |
| Exportar Relatório CSV |

Total SE = **3**

---

## Resultado

| Tipo | Quantidade | PF |
|------|-----------:|---:|
| EE |31|124|
| CE |14|56|
| SE |3|15|

Subtotal Transações = **195 PF**

---

## Resultado Final (Ce)

```
Ce = Dados + Transações

Ce = 82 + 195

Ce = 277 PF
```

---

# 6. Contagem Detalhada (Cd)

## 6.1 Classificação das Funções de Dados

| ALI | Complexidade | PF |
|------|--------------|---:|
| Funcionário | Média |10|
| Cliente | Média |10|
| Aparelho | Baixa |7|
| Ordem de Serviço | Média |10|
| Serviço | Baixa |7|
| OrdemServicoServico | Média |10|
| Equipamento | Baixa |7|
| Visita Técnica | Baixa |7|
| Conta a Receber | Alta |15|
| Garantia | Baixa |7|
| Auditoria Log | Média |10|
| Gateway de Pagamento (AIE) | Baixa |5|

Subtotal Dados = **105 PF**

---

## 6.2 Classificação das Funções de Transação

| Complexidade | Quantidade | PF Unitário | Total |
|--------------|-----------:|------------:|------:|
| Baixa |24|3|72|
| Média |17|4|68|
| Alta |7|6|42|

Subtotal Transações = **182 PF**

---

## Resultado Final

```
Cd = 105 + 182

Cd = 287 PF
```

---

# 7. Matriz de Rastreabilidade PF × User Stories

| User Story | Descrição | PF |
|------------|------------------------------|----:|
| US00 | Autenticação |10|
| US01 | Manter Funcionário |20|
| US02 | Manter Cliente |18|
| US03 | Gerenciar Aparelho |14|
| US04 | Gerenciar Ordem de Serviço |32|
| US05 | Gerenciar Serviço |12|
| US06 | Registrar OrdemServicoServico |20|
| US07 | Gerenciar Equipamento |16|
| US08 | Agendar Visita Técnica |12|
| US09 | Gerenciar Conta a Receber |34|
| US10 | Auditoria Log |14|
| US11 | Gerar Relatório |26|
| US12 | Controle de Garantia |16|
| Infraestrutura, Segurança e Integrações |43|

---

## Total

**287 Pontos de Função**

---

# 8. Resumo das Contagens

| Método | Total |
|---------|------:|
| Contagem Indicativa (Ci) |400 PF|
| Contagem Estimativa (Ce) |277 PF|
| Contagem Detalhada (Cd) |287 PF|

---

# 9. Estimativa de Prazo

## Produtividade

- 8 horas por PF
- Equipe: 2 desenvolvedores

### Cálculos

```
Horas Totais

287 × 8 = 2.296 horas
```

```
Dias

2.296 ÷ 16 = 144 dias
```

```
Meses

144 ÷ 22 = 6,5 meses
```

---

# 10. Estimativa de Custo

Valor da hora:

```
R$17,00
```

```
2.296 × 17

=

R$39.032,00
```

---

# 11. Conclusão

Após a análise do Documento de Visão, User Stories, Requisitos Funcionais e Modelo Conceitual, o Sistema de Gestão de Assistência Técnica possui uma estimativa de **287 Pontos de Função** pela Contagem Detalhada (Cd), sendo este o valor recomendado para planejamento, cronograma e estimativa de custos do projeto.

A Contagem Detalhada representa de forma mais precisa a complexidade funcional do sistema e é a recomendada para utilização em trabalhos acadêmicos e projetos de desenvolvimento de software.
## 10. Histórico de Revisões

| Data | Versão | Descrição | Autor |
|:---|:---:|:---|:---|
| 08/05/2026 | 1.0.0 | Criação inicial do documento de contagem de PF | Mariana |
| 08/05/2026 | 1.0.0 | Revisão e validação das contagens | Jadson |
| 02/07/2026 | 1.0.1 | Criação final do documento de contagem de PF | Mariana |

---
