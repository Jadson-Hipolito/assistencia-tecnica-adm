import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarCliente } from '../services/api'

export default function ClienteCreatePage() {
  const [form, setForm] = useState({ nome: '', documento: '', endereco: '', contato: '' })
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setLoading(true)

    try {
      await criarCliente(form)
      navigate('/clientes')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar cliente')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Novo Cliente</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Nome
          <input name="nome" value={form.nome} onChange={handleChange} required />
        </label>
        <label>
          Documento
          <input name="documento" value={form.documento} onChange={handleChange} required />
        </label>
        <label>
          Endereço
          <input name="endereco" value={form.endereco} onChange={handleChange} required />
        </label>
        <label>
          Contato
          <input name="contato" value={form.contato} onChange={handleChange} required />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? 'Salvando...' : 'Salvar cliente'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
