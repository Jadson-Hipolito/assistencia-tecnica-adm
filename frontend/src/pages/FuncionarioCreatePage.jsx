import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarFuncionario } from '../services/api'

export default function FuncionarioCreatePage() {
  const [form, setForm] = useState({ nome: '', email: '', senha: '', cargo: '', telefone: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
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
      await criarFuncionario(form)
      navigate('/funcionarios')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar funcionário')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Novo Funcionário</h1>
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
          Senha
          <input name="senha" type="password" value={form.senha} onChange={handleChange} required />
        </label>
        <label>
          Cargo
          <input name="cargo" value={form.cargo} onChange={handleChange} required />
        </label>
        <label>
          Telefone
          <input name="telefone" value={form.telefone} onChange={handleChange} required />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? 'Salvando...' : 'Salvar funcionário'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
