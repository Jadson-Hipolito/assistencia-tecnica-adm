from .funcionario_schema import (
    FuncionarioCreate,
    FuncionarioResponse,
    FuncionarioUpdate,
)

from .cliente_schema import (
    ClienteCreate,
    ClienteResponse,
    ClienteUpdate,
)

from .servico_schema import (
    ServicoCreate,
    ServicoResponse,
    ServicoUpdate,
)

from .equipamento_schema import (
    EquipamentoCreate,
    EquipamentoResponse,
    EquipamentoUpdate,
)

from .aparelho_schema import (
    AparelhoCreate,
    AparelhoResponse,
    AparelhoUpdate,
)

from .ordem_servico_schema import (
    OrdemServicoCreate,
    OrdemServicoResponse,
    OrdemServicoUpdate,
)

from .ordem_servico_servico_schema import (
    OrdemServicoServicoCreate,
    OrdemServicoServicoResponse,
)

from .visita_tecnica_schema import (
    VisitaTecnicaCreate,
    VisitaTecnicaResponse,
    VisitaTecnicaUpdate,
)

from .conta_receber_schema import (
    ContaReceberCreate,
    ContaReceberResponse,
    ContaReceberUpdate,
)

from .auditoria_log_schema import (
    AuditoriaLogCreate,
    AuditoriaLogResponse,
)

__all__ = [
    # Funcionário
    "FuncionarioCreate",
    "FuncionarioResponse",
    "FuncionarioUpdate",

    # Cliente
    "ClienteCreate",
    "ClienteResponse",
    "ClienteUpdate",

    # Serviço
    "ServicoCreate",
    "ServicoResponse",
    "ServicoUpdate",

    # Equipamento
    "EquipamentoCreate",
    "EquipamentoResponse",
    "EquipamentoUpdate",

    # Aparelho
    "AparelhoCreate",
    "AparelhoResponse",
    "AparelhoUpdate",

    # Ordem de Serviço
    "OrdemServicoCreate",
    "OrdemServicoResponse",
    "OrdemServicoUpdate",

    # Ordem Serviço x Serviço
    "OrdemServicoServicoCreate",
    "OrdemServicoServicoResponse",

    # Visita Técnica
    "VisitaTecnicaCreate",
    "VisitaTecnicaResponse",
    "VisitaTecnicaUpdate",

    # Conta a Receber
    "ContaReceberCreate",
    "ContaReceberResponse",
    "ContaReceberUpdate",

    # Auditoria
    "AuditoriaLogCreate",
    "AuditoriaLogResponse",
]
