import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarCliente, getCliente } from '../services/api'

export default function ClienteEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ nome: '', documento: '', endereco: '', contato: '', ativo: true })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadCliente = async () => {
      setLoading(true)
      setError('')
      try {
        const cliente = await getCliente(id)
        setForm({
          nome: cliente.nome || '',
          documento: cliente.documento || '',
          endereco: cliente.endereco || '',
          contato: cliente.contato || '',
          ativo: cliente.ativo ?? true,
        })
      } catch (err) {
        setError(err.message || 'Erro ao carregar cliente')
      } finally {
        setLoading(false)
      }
    }

    loadCliente()
  }, [id])

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target
    setForm((current) => ({
      ...current,
      [name]: type === 'checkbox' ? checked : value,
    }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setSaving(true)

    try {
      await atualizarCliente(id, form)
      navigate('/clientes')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar cliente')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando cliente...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Cliente</h1>
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
        <label className="checkbox-label">
          <input name="ativo" type="checkbox" checked={form.ativo} onChange={handleChange} />
          Ativo
        </label>
        <button type="submit" disabled={saving}>
          {saving ? 'Atualizando...' : 'Salvar alterações'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
