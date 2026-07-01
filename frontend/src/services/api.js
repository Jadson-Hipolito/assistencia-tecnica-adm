const API_URL = 'http://localhost:8000'

const getToken = () => localStorage.getItem('token')

const request = async (endpoint, options = {}) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(getToken() ? { Authorization: `Bearer ${getToken()}` } : {}),
      ...options.headers,
    },
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({}))
    throw new Error(error.detail || 'Erro na requisição')
  }

  return response.json()
}

export const login = async (email, senha) => {
  return request('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, senha }),
  })
}

export const getProfile = async () => {
  return request('/auth/me')
}

export const listarClientes = async () => {
  return request('/clientes')
}

export const criarCliente = async (data) => {
  return request('/clientes', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const listarOrdens = async () => {
  return request('/ordens')
}

export const getOrdem = async (id) => {
  return request(`/ordens/${id}`)
}

export const criarOrdem = async (data) => {
  return request('/ordens', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const atualizarOrdem = async (id, data) => {
  return request(`/ordens/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const getCliente = async (id) => {
  return request(`/clientes/${id}`)
}

export const atualizarCliente = async (id, data) => {
  return request(`/clientes/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const listarServicos = async () => {
  return request('/servicos')
}

export const criarServico = async (data) => {
  return request('/servicos', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const criarFuncionario = async (data) => {
  return request('/funcionarios', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const getFuncionario = async (id) => {
  return request(`/funcionarios/${id}`)
}

export const atualizarFuncionario = async (id, data) => {
  return request(`/funcionarios/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const listarFuncionarios = async () => {
  return request('/funcionarios')
}

export const criarAparelho = async (data) => {
  return request('/aparelhos', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const getAparelho = async (id) => {
  return request(`/aparelhos/${id}`)
}

export const atualizarAparelho = async (id, data) => {
  return request(`/aparelhos/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const listarAparelhos = async () => {
  return request('/aparelhos')
}

export const listarEquipamentos = async () => {
  return request('/equipamentos')
}

export const criarEquipamento = async (data) => {
  return request('/equipamentos', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const getEquipamento = async (id) => {
  return request(`/equipamentos/${id}`)
}

export const atualizarEquipamento = async (id, data) => {
  return request(`/equipamentos/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const listarVisitas = async () => {
  return request('/visitas-tecnicas')
}

export const criarVisita = async (data) => {
  return request('/visitas-tecnicas', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const getVisita = async (id) => {
  return request(`/visitas-tecnicas/${id}`)
}

export const atualizarVisita = async (id, data) => {
  return request(`/visitas-tecnicas/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const listarContasReceber = async () => {
  return request('/contas-receber')
}

export const pagarContaReceber = async (id) => {
  return request(`/contas-receber/${id}/pagar`, {
    method: 'PATCH',
  })
}

export const criarContaReceber = async (data) => {
  return request('/contas-receber', {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export const getContaReceber = async (id) => {
  return request(`/contas-receber/${id}`)
}

export const atualizarContaReceber = async (id, data) => {
  return request(`/contas-receber/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data),
  })
}

export const excluirCliente = async (id) => {
  return request(`/clientes/${id}`, {
    method: 'DELETE',
  })
}
