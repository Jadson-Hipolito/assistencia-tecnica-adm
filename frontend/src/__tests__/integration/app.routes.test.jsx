import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'
import App from '../../App'
import { AuthProvider } from '../../context/AuthContext'

vi.mock('../../services/api', () => ({
  login: vi.fn(),
  listarClientes: vi.fn(),
  listarOrdens: vi.fn(),
}))

import { login, listarClientes, listarOrdens } from '../../services/api'

describe('Fluxo de rotas do frontend', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    localStorage.clear()
  })

  it('redireciona para login quando o usuário não está autenticado', async () => {
    render(
      <MemoryRouter initialEntries={['/clientes']}>
        <AuthProvider>
          <App />
        </AuthProvider>
      </MemoryRouter>
    )

    expect(await screen.findByRole('heading', { name: /login/i })).toBeInTheDocument()
  })

  it('exibe a lista de clientes para usuário autenticado', async () => {
    localStorage.setItem('token', 'fake-token')
    localStorage.setItem('user', JSON.stringify({ id: 1, nome: 'Maria' }))
    listarClientes.mockResolvedValue([{ id: 1, nome: 'Maria', email: 'maria@email.com' }])
    listarOrdens.mockResolvedValue([])

    render(
      <MemoryRouter initialEntries={['/clientes']}>
        <AuthProvider>
          <App />
        </AuthProvider>
      </MemoryRouter>
    )

    expect(await screen.findByText('Maria')).toBeInTheDocument()
  })
})