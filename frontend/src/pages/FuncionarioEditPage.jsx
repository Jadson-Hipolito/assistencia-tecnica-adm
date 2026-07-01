import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarFuncionario, getFuncionario } from '../services/api'

export default function FuncionarioEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ nome: '', email: '', cargo: '', telefone: '', ativo: true })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadFuncionario = async () => {
      setLoading(true)
      setError('')
      try {
        const funcionario = await getFuncionario(id)
        setForm({
          nome: funcionario.nome || '',
          email: funcionario.email || '',
          cargo: funcionario.cargo || '',
          telefone: funcionario.telefone || '',
          ativo: funcionario.ativo ?? true,
        })
      } catch (err) {
        setError(err.message || 'Erro ao carregar funcionário')
      } finally {
        setLoading(false)
      }
    }

    loadFuncionario()
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
      await atualizarFuncionario(id, form)
      navigate('/funcionarios')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar funcionário')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando funcionário...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Funcionário</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Nome
          <input name="nome" value={form.nome} onChange={handleChange} required />
        </label>
        <label>
          E-mail
          <input name="email" type="email" value={form.email} onChange={handleChange} required />
        </label>
        <label>
          Cargo
          <input name="cargo" value={form.cargo} onChange={handleChange} required />
        </label>
        <label>
          Telefone
          <input name="telefone" value={form.telefone} onChange={handleChange} required />
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
