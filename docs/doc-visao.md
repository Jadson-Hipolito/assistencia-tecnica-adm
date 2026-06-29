# Documento de Visão

## Descrição do Projeto

Título: Sistema de Gestão de Assistência Técnica

Descrição: O Sistema de Gestão de Assistência Técnica é uma aplicação web desenvolvida para automatizar e organizar os processos operacionais de uma assistência técnica, incluindo o controle de clientes, aparelhos, ordens de serviço, equipamentos e visitas técnicas.

O sistema centraliza todo o fluxo de atendimento técnico, desde a abertura da ordem de serviço até sua finalização e geração de cobrança, permitindo maior controle sobre prazos, serviços realizados e recursos utilizados.

Além disso, a aplicação possibilita o gerenciamento de estoque de equipamentos, registro de visitas técnicas e geração de relatórios gerenciais e operacionais, contribuindo para a tomada de decisão e melhoria da eficiência dos processos internos.

O sistema é de uso exclusivo de funcionários internos (administradores e técnicos), com controle de acesso baseado em perfis, garantindo segurança e organização das operações.

---


## Equipe e Definição de Papéis

Membro     |     Papel   |   E-mail   |
---------  | ----------- | ---------- |
Jadson     | Desenvolvedor, Testador | jadsonhipolito@gmail.com |
Mariana    | Analista, Desenvolvedor | araujodemedeirosmariana@gmail.com |

---

### Matriz de Competências

Membro     |     Competências   |
---------  | ----------- |
Jadson    | Python, FastAPI, SQLite, Git/GitHub, Modelagem de Dados, Arquitetura de Software |
Mariana   | Python, SQLite, Git/GitHub | 

---

## Perfis dos Usuários

O sistema é utilizado exclusivamente por funcionários internos da assistência técnica. Temos os seguintes perfis/atores:

Perfil        | Descrição   |
------------- | ----------- |
Administrador | Responsável pela gestão completa do sistema, incluindo cadastro de clientes, aparelhos, ordens de serviço, serviços, equipamentos e controle financeiro. Também possui acesso a relatórios e auditoria do sistema.|
Técnico       | Este usuário é responsável pela execução dos serviços, atualização das ordens de serviço e registro de peças utilizadas.|

---

## Lista de Requisitos Funcionais

### Requisito de Segurança - RF00 - Autenticação
Responsável por controlar o acesso ao sistema, permitindo que apenas funcionários cadastrados realizem login por meio de credenciais (e-mail e senha). O sistema valida as informações e cria uma sessão autenticada para o usuário, garantindo segurança no acesso às funcionalidades.

Regra: Somente funcionários podem acessar o sistema.

| Requisito               | Descrição                | Ator                   |
| ----------------------- | ------------------------ | ---------------------- |
| RF00.1 – Realizar Login        | Permite autenticar o funcionário por meio de e-mail e senha. | Administrador, Técnico |
| RF00.2 – Alterar Senha         | Permite alterar a senha de acesso.              | Administrador, Técnico |
| RF00.3 – Logout                | Permite encerrar a sessão do usuário.           | Administrador, Técnico |

---

### Entidade Funcionário - RF01 - Manter Funcionário
Um funcionário representa o usuário interno do sistema, podendo possuir perfil Administrador ou Técnico.


| Requisito               | Descrição                | Ator                   |
| ----------------------- | ------------------------ | ---------------------- |
| RF01.1 – Cadastrar Funcionário | Permite cadastrar um novo funcionário informando nome, e-mail, senha e perfil. | Administrador          |
| RF01.2 – Alterar Funcionário   | Permite atualizar os dados de um funcionário.   | Administrador          |
| RF01.3 – Consultar Funcionário | Permite consultar funcionários cadastrados.     | Administrador          |
| RF01.4 – Desativar Funcionário | Permite a desativação do funcionário do sistema.| Administrador          |

---

### Entidade Cliente - RF02 - Manter Cliente
Representa os clientes da assistência técnica

Requisito                     | Descrição   | Ator       |
----------------------------- | ----------- | ---------- |
RF02.1 - Cadastrar Cliente    | Insere novo cliente informando: id, nome, documento(CPF ou CNPJ conforme o tipo do cliente), contato, endereço. | Administrador |
RF02.2 - Alterar Cliente      | Atualiza qualquer dado contido no cadastro do cliente, caso seja necessário. | Administrador |
RF02.3 - Consultar Cliente    | Consulta do cliente através dos dados do mesmo. | Administrador, Técnico |
RF02.4 - Desativar Cliente    | Desativar um cliente informando o id. | Administrador |

---

### Entidade Aparelho - RF03 - Gerenciar Aparelho
Um aparelho representa um equipamento pertencente ao cliente que será avaliado, reparado ou acompanhado pela assistência técnica.

Regra: Todo aparelho deve estar vinculado a um cliente previamente cadastrado.

Requisito                   | Descrição                                         | Ator                    |
--------------------------- | --------------------------------------------------| ----------------------- |
RF03.1 - Cadastrar Aparelho | Permite cadastrar aparelho vinculado a um cliente | Administrador           |
RF03.2 - Alterar Aparelho   | Atualiza dados do aparelho                        | Administrador           |
RF03.3 - Consultar Aparelho | Consulta aparelho por id                          | Administrador, Técnico  |
RF03.4 - Desativar Aparelho | Desativa aparelho sem OS em andamento             | Administrador           |

---

### Entidade Ordem_Serviço - RF04 - Gerenciar Ordem_Serviço
Uma ordem de serviço registra o atendimento realizado, podendo conter vários equipamentos e status de acompanhamento.

Regra: Uma Ordem de Serviço somente poderá ser aberta para um cliente e um aparelho cadastrados.

Requisito                     | Descrição   | Ator           |
----------------------------- | ----------- | -------------- |
RF04.1 - Abrir ordem de Serviço  | Criar ordem de serviço para solicitação de reparo ou manutenção, incluindo informações do aparelho e descrição do problema e quaisquer detalhes relevantes. | Administrador |
RF04.2 - Editar ordem de serviço | Atualiza uma OS informando:informações sobre o cliente, descrição do problema e quaisquer detalhes relevantes. | Administrador |
RF04.3 - Consultar ordem de serviço | Consulta uma OS informando: id. | Técnico, Administrador |
RF04.4 - Atualizar Status da OS     | Alterar o status da OS conforme andamento. | Técnico, Administrador |
RF04.5 - Encerrar ordem de serviço   | Encerramento da OS após a conclusão das atividades.  | Técnico |

---

### Entidade Serviço - RF05 - Gerenciar Serviço
Representa o catálogo de serviços oferecidos pela assistência técnica.

Regra: Apenas serviços ativos podem ser vinculados a uma Ordem de Serviço.

Requisito                  | Descrição                     | Ator                   |
-------------------------- | ----------------------------- | ---------------------- |
RF05.1 - Cadastrar Serviço | Cadastra serviço no catálogo  | Administrador          |
RF05.2 - Alterar Serviço   | Atualiza serviço existente    | Administrador          |
RF05.3 - Consultar Serviço | Consulta serviços cadastrados | Administrador, Técnico |
RF05.4 - Desativar Serviço | Desativa serviço do catálogo  | Administrador          |

---

### Entidade OrdemServicoServico - RF06 - Registrar OrdemServicoServico
Relaciona os serviços executados em uma ordem de serviço.

Regra: Os serviços somente poderão ser registrados após a abertura da Ordem de Serviço, e a Ordem de Serviço somente poderá ser finalizada após a conclusão de todos os serviços registrados.

| Requisito                  | Descrição                                                     | Ator                   |
| -------------------------- | ------------------------------------------------------------- | ---------------------- |
| RF06.1 – Adicionar Serviço | Permite adicionar um serviço a uma ordem de serviço.          | Administrador, Técnico |
| RF06.2 – Remover Serviço   | Permite remover um serviço da ordem de serviço.               | Administrador, Técnico |
| RF06.3 – Calcular Subtotal | Calcula automaticamente o subtotal de cada serviço executado. | Sistema                |


---

### Entidade Equipamento  - RF07 - Gerenciar Equipamento 
Um componente essencial ao realizar OS. Ele tem: código, tipo, marca, modelo, quantidade.

Regra: A quantidade de equipamentos em estoque não pode assumir valores negativos.

Requisito                      | Descrição                                                        | Ator                   |
------------------------------ | ---------------------------------------------------------------- | ---------------------- |
RF07.1 - Cadastrar Equipamento | Insere novo equipamento informando: id, nome, tipo e quantidade. | Administrador          |
RF07.2 - Alterar Equipamento   | Permite atualizar os dados do equipamento.                       | Administrador, Técnico |
RF07.3 - Consultar Equipamento | Permite consultar equipamentos cadastrados.                      | Administrador, Técnico |
RF07.4 - Atualizar Estoque     | Permite controlar a quantidade disponível em estoque.            | Administrador, Técnico |

---


### Entidade Visita_Técnica - RF08 - Agendar Visita_Técnica
Uma visita técnica representa um atendimento presencial vinculado a uma ordem de serviço.

Regra: Toda visita técnica deve estar vinculada a uma Ordem de Serviço e a um funcionário responsável.

| Requisito                 | Descrição                             | Ator          |
| ------------------------- | ------------------------------------- | ------------- |
| RF08.1 – Registrar Visita | Permite registrar uma visita técnica. | Administrador |
| RF08.2 – Reagendar Visita | Permite reagendar uma visita técnica. | Administrador |
| RF08.3 – Cancelar Visita  | Permite cancelar uma visita técnica.  | Administrador |

---

### Entidade Conta_Receber - RF9 - Gerenciar Conta_Receber 
Controla os valores gerados pelas ordens de serviço.

Regra: Ao finalizar uma Ordem de Serviço, o sistema deve gerar automaticamente uma Conta a Receber vinculada à ordem.

| Requisito       | Descrição                 | Ator          |
| --------------- | ------------------------- | ------------- |
| RF09.1 - Gerar Conta a Receber | Ao finalizar uma Ordem de Serviço, o sistema cria automaticamente uma conta a receber vinculada à OS | Sistema |
| RF09.2 - Registrar Pagamento Offline | Administrador registra pagamentos realizados fora do sistema   | Administrador |
| RF09.3 - Confirmar Pagamento | Atualiza status da conta para **PAGO** após validação                  | Sistema       |
| RF09.4 - Calcular Multa e Juros | Aplica multa de 2% + juros de 0,33% ao dia em caso de atraso        | Sistema       |
| RF09.5 - Processar Pagamento Online | Processa pagamento via gateway de pagamento integrado           | Sistema       |
| RF09.6 - Validar Transação | Valida transação retornada pelo gateway de pagamento                     | Sistema       |
| RF09.7 - Estornar Pagamento | Permite estorno de pagamento realizado (administrador)                  | Administrador |
| RF09.8 - Emitir Comprovante | Gera comprovante em PDF do pagamento realizado                          | Sistema       |

---

### Entidade AuditoriaLog - RF10 - AuditoriaLog
Registra as operações realizadas pelos funcionários.

Regra: As ações realizadas pelos funcionários no sistema devem ser registradas em log de auditoria para fins de rastreabilidade.

| Requisito                | Descrição                                                        | Ator          |
| ------------------------ | ---------------------------------------------------------------- | ------------- |
| RF10.1 – Registrar Ações | Registra automaticamente as ações realizadas pelos funcionários. | Sistema       |
| RF10.2 – Consultar Logs  | Permite consultar os registros de auditoria.                     | Administrador |

---

### Entidade Relatórios - RF11 - Gerar Relatório
Permite emitir relatórios para acompanhamento das atividades da assistência técnica.

Regra: Somente funcionários autorizados podem emitir relatórios do sistema.

| Requisito                    | Descrição                                                       | Ator                   |
| ---------------------------- | --------------------------------------------------------------- | ---------------------- |
| RF11.1 - Emitir Relatórios   | Gera relatórios diversos, como histórico de serviços realizados, Ordens de Serviço por período, faturamento por período e produtividade por técnico (quantidade de serviços, tempo gasto e comissão) | Técnico, Administrador |
| RF11.2 - Filtrar por Status  | Permite filtrar relatórios por status das Ordens de Serviço  | Administrador |
| RF11.3 - Exportar Relatórios | Exporta relatórios nos formatos PDF e CSV  | Administrador |

---

### Entidade Controle de Garantia - RF12 - Controle de Garantia
Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.

Regra:

| Requisito               | Descrição                               | Ator                   |
| ----------------------- | --------------------------------------- | ---------------------- |
| RF12.1 – Consultar Garantia | Permite consultar serviços ou ordens de serviço ainda dentro do prazo de garantia. | Técnico, Administrador |
| RF12.2 – Verificar Validade da Garantia | O sistema verifica automaticamente se a OS ainda está dentro do período de garantia com base na data_fim + garantia_dias. | Sistema |
| RF12.3 – Registrar Atendimento em Garantia | Permite registrar nova visita ou serviço relacionado a garantia. | Técnico |

---

### Modelo Conceitual

Abaixo apresentamos o modelo conceitual usando o **Mermaid**.

```mermaid
erDiagram
    %% Entidades Base
    class Funcionario {
    int id PK
    string nome
    string email
    string senha
    string perfil   
}

class Cliente {
    int id PK
    string tipo_pessoa
    string nome
    string documento
    string contato
    string email
    string endereco
}
    
    %% Entidades de Negócio
    class Aparelho {
    int id PK
    string tipo
    string marca
    string modelo
    string numero_serie
    string status
    int cliente_id FK
}

class Ordem_Servico {
    int id PK
    string status
    string descricao
    date data_abertura
    date data_fechamento
    int cliente_id FK
    int aparelho_id FK
}

class Servico {
    int id PK
    string nome
    string descricao
    decimal valor_padrao
}

class OrdemServicoServico {
    int ordem_servico_id FK
    int servico_id FK
    int quantidade
    decimal valor_aplicado
}

class Equipamento {
    int id PK
    string nome
    string tipo
    int quantidade
    string status
}

class VisitaTecnica {
    int id PK
    date data
    string observacao
    int ordem_servico_id FK
    int funcionario_id FK
}
    
    %% Entidades Financeiras
    class ContaReceber {
        int id PK
        decimal valor_total
        decimal valor_multa
        decimal valor_desconto
        string status
        date vencimento
        int ordem_servico_id FK
}
    
    %% Entidades de Suporte
    class Garantia {
        int id PK
        int ordem_servico_id FK
        date data_inicio
        date data_fim
        int prazo_dias
        string status  
}

class AuditoriaLog {
    int id PK
    string acao
    string entidade
    date data_hora
    int funcionario_id FK
} 
        
    %% Relacionamentos de Associação
    CLIENTE ||--o{ APARELHO : "possui"
    CLIENTE ||--o{ ORDEM_SERVICO : "solicita"         
    APARELHO ||--o{ ORDEM_SERVICO : "registrado_em" 
    SERVICO ||--o{ ORDEMSERVICOSERVICO : "executado_em" 
    ORDEM_SERVICO ||--o{ ORDEMSERVICOSERVICO : "contem"
    ORDEM_SERVICO ||--|| CONTA_RECEBER : "gera"
    ORDEM_SERVICO ||--|| GARANTIA : "contem"
    FUNCIONARIO ||--o{ VISITA_TECNICA : "realiza"
    ORDEM_SERVICO ||--o{ VISITA_TECNICA : "gera"    
    FUNCIONARIO ||--o{ AUDITORIA_LOG : "gera"
```


## Lista de Requisitos Não-Funcionais

Requisito                                 | Descrição   |
---------                                 | ----------- |
RNF01 - Deve ser acessível via navegador | Deve abrir perfeitamento no Firefox e no Chrome. |
RNF02 - Usabilidade | O sistema deverá possuir uma interface intuitiva e de fácil utilização, permitindo que usuários com pouca experiência em sistemas consigam utilizá-lo sem dificuldades significativas. |
RNF03 -	Segurança |	As senhas dos usuários devem ser armazenadas de forma criptografada (hash). O controle de acesso deve ser rigorosamente baseado nos perfis definidos. |
RNF04 - Desempenho | O sistema deve responder às operações principais em até 3 segundos em condições normais de uso.|
RNF05 - Backup | O banco de dados deve permitir realização de backups periódicos para recuperação de informações.|
RNF06 - Auditoria | O sistema deve registrar automaticamente operações de inclusão, alteração, exclusão e mudança de status realizadas pelos usuários.|

---


## Riscos

Data | Risco | Prioridade | Responsável | Status | Providência/Solução |
------ | ------ | ------ | ------ | ------ | ------ |
31/03/2026 | Mudança de escopo com inclusão de funcionalidades não planejadas durante o desenvolvimento. | Alta | Mariana | Monitorando	| Utilizar metodologia ágil com sprints curtas para priorizar entregas e congelar escopo a cada iteração. |
31/03/2026 | Indisponibilidade ou falha na integração com gateway de pagamento. | Média | Jadson | Monitorando | Pesquisar e ter um plano B com outro provedor de pagamento; implementar registro de falhas para retentativa. |
31/03/2026 | Dificuldade de adaptação dos usuários à nova ferramenta. |	Média |	Mariana | Monitorando |	Realizar treinamentos iniciais e produzir manuais de usuário simplificados. |


### Referências

MODELO BSI – Doc 001 – Documento de Visão. Documento construído a partir do modelo BSI. Disponível em: https://docs.google.com/document/d/1DPBcyGHgflmz5RDsZQ2X8KVBPoEF5PdAz9BBNFyLa6A/edit?usp=sharing
. Acesso em: 28 mar. 2026.

