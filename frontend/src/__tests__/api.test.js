import { describe, it, expect, vi, beforeEach } from 'vitest'
import {
  login,
  listarClientes,
  listarOrdens,
  listarFuncionarios,
  listarAparelhos,
  listarEquipamentos,
  listarVisitas,
  listarContasReceber,
  pagarContaReceber,
} from '../services/api'

describe('API Service', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    global.fetch = vi.fn()
    localStorage.clear()
  })

  it('deve fazer login com sucesso', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => ({ token: 'fake-token', user: { id: 1 } }),
    })

    const result = await login('teste@email.com', 'senha123')
    expect(result).toEqual({ token: 'fake-token', user: { id: 1 } })
    expect(global.fetch).toHaveBeenCalledWith(
      'http://localhost:8000/auth/login',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'teste@email.com', senha: 'senha123' }),
      })
    )
  })

  it('deve listar clientes', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, nome: 'Ana' }],
    })

    const result = await listarClientes()
    expect(result).toEqual([{ id: 1, nome: 'Ana' }])
  })

  it('deve listar ordens de serviço', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, descricao: 'Troca de tela' }],
    })

    const result = await listarOrdens()
    expect(result).toEqual([{ id: 1, descricao: 'Troca de tela' }])
  })

  it('deve listar funcionários', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, nome: 'Carlos' }],
    })

    const result = await listarFuncionarios()
    expect(result).toEqual([{ id: 1, nome: 'Carlos' }])
  })

  it('deve listar aparelhos', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, tipo: 'Smartphone' }],
    })

    const result = await listarAparelhos()
    expect(result).toEqual([{ id: 1, tipo: 'Smartphone' }])
  })

  it('deve listar equipamentos', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, nome: 'Osciloscópio' }],
    })

    const result = await listarEquipamentos()
    expect(result).toEqual([{ id: 1, nome: 'Osciloscópio' }])
  })

  it('deve listar visitas técnicas', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, status: 'AGENDADA' }],
    })

    const result = await listarVisitas()
    expect(result).toEqual([{ id: 1, status: 'AGENDADA' }])
  })

  it('deve listar contas a receber', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => [{ id: 1, valor_total: 120.5 }],
    })

    const result = await listarContasReceber()
    expect(result).toEqual([{ id: 1, valor_total: 120.5 }])
  })

  it('deve marcar conta como paga', async () => {
    global.fetch.mockResolvedValue({
      ok: true,
      json: async () => ({ id: 1, status: 'PAGO' }),
    })

    const result = await pagarContaReceber(1)
    expect(result).toEqual({ id: 1, status: 'PAGO' })
  })
})