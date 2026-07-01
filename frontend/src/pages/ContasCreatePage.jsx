import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarContaReceber, listarOrdens } from '../services/api'

export default function ContasCreatePage() {
  const [form, setForm] = useState({ ordem_servico_id: '', valor_total: '', data_vencimento: '' })
  const [ordens, setOrdens] = useState([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadOrdens = async () => {
      setLoading(true)
      try {
        setOrdens(await listarOrdens())
      } catch (err) {
        setError(err.message || 'Erro ao carregar ordens')
      } finally {
        setLoading(false)
      }
    }

    loadOrdens()
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
      await criarContaReceber({
        ordem_servico_id: Number(form.ordem_servico_id),
        valor_total: Number(form.valor_total),
        data_vencimento: form.data_vencimento,
      })
      navigate('/contas')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar conta')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Nova Conta a Receber</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Ordem de Serviço
          <select name="ordem_servico_id" value={form.ordem_servico_id} onChange={handleChange} required>
            <option value="">Selecione uma ordem</option>
            {ordens.map((ordem) => (
              <option key={ordem.id} value={ordem.id}>
                {ordem.descricao}
              </option>
            ))}
          </select>
        </label>
        <label>
          Valor total
          <input
            name="valor_total"
            type="number"
            step="0.01"
            value={form.valor_total}
            onChange={handleChange}
            required
          />
        </label>
        <label>
          Vencimento
          <input name="data_vencimento" type="date" value={form.data_vencimento} onChange={handleChange} required />
        </label>
        <button type="submit" disabled={saving || loading}>
          {saving ? 'Salvando...' : 'Salvar conta'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
