import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { getOrdem, atualizarOrdem } from '../services/api'

export default function OrdemEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ descricao: '', status: '' })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadOrdem = async () => {
      setLoading(true)
      setError('')
      try {
        const ordem = await getOrdem(id)
        setForm({
          descricao: ordem.descricao || '',
          status: ordem.status || 'ABERTA',
        })
      } catch (err) {
        setError(err.message || 'Erro ao carregar ordem')
      } finally {
        setLoading(false)
      }
    }

    loadOrdem()
  }, [id])

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setSaving(true)

    try {
      await atualizarOrdem(id, form)
      navigate(`/ordens/${id}`)
    } catch (err) {
      setError(err.message || 'Erro ao atualizar ordem')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando ordem...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Ordem</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Descrição
          <textarea name="descricao" value={form.descricao} onChange={handleChange} required />
        </label>
        <label>
          Status
          <select name="status" value={form.status} onChange={handleChange} required>
            <option value="ABERTA">ABERTA</option>
            <option value="EM_ANDAMENTO">EM ANDAMENTO</option>
            <option value="FINALIZADA">FINALIZADA</option>
          </select>
        </label>
        <button type="submit" disabled={saving}>
          {saving ? 'Salvando...' : 'Salvar ordem'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
