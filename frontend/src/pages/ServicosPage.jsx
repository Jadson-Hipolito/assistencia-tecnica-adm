import { useEffect, useState } from 'react'
import { criarServico, listarServicos } from '../services/api'

export default function ServicosPage() {
  const [servicos, setServicos] = useState([])
  const [form, setForm] = useState({ nome: '', descricao: '', valor_padrao: '' })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadServicos = async () => {
      try {
        const data = await listarServicos()
        setServicos(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar serviços')
      } finally {
        setLoading(false)
      }
    }

    loadServicos()
  }, [])

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setSaving(true)

    try {
      const created = await criarServico({
        nome: form.nome,
        descricao: form.descricao,
        valor_padrao: Number(form.valor_padrao),
      })
      setServicos((current) => [...current, created])
      setForm({ nome: '', descricao: '', valor_padrao: '' })
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar serviço')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Serviços</h1>
      {loading && <p>Carregando serviços...</p>}
      {error && <p className="error-message">{error}</p>}

      <form className="card-form" onSubmit={handleSubmit}>
        <h2>Novo Serviço</h2>
        <label>
          Nome
          <input name="nome" value={form.nome} onChange={handleChange} required />
        </label>
        <label>
          Descrição
          <textarea name="descricao" value={form.descricao} onChange={handleChange} required />
        </label>
        <label>
          Valor padrão
          <input
            name="valor_padrao"
            type="number"
            step="0.01"
            value={form.valor_padrao}
            onChange={handleChange}
            required
          />
        </label>
        <button type="submit" disabled={saving}>
          {saving ? 'Salvando...' : 'Salvar serviço'}
        </button>
      </form>

      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Descrição</th>
              <th>Valor padrão</th>
            </tr>
          </thead>
          <tbody>
            {servicos.length > 0 ? (
              servicos.map((servico) => (
                <tr key={servico.id}>
                  <td>{servico.id}</td>
                  <td>{servico.nome}</td>
                  <td>{servico.descricao}</td>
                  <td>{`R$ ${servico.valor_padrao}`}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4">Nenhum serviço cadastrado.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
