import { describe, it, expect, vi, beforeEach } from 'vitest'
import { login, listarClientes, listarOrdens } from '../services/api'

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
})