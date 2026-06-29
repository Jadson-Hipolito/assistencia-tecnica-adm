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

export const listarClientes = async () => {
  return request('/clientes')
}

export const listarOrdens = async () => {
  return request('/ordens')
}
