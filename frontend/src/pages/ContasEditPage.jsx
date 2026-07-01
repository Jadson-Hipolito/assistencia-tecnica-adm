import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarContaReceber, getContaReceber, listarOrdens } from '../services/api'

export default function ContasEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ ordem_servico_id: '', valor_total: '', data_vencimento: '', status: '' })
  const [ordens, setOrdens] = useState([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const [conta, ordensData] = await Promise.all([getContaReceber(id), listarOrdens()])
        setForm({
          ordem_servico_id: conta.ordem_servico_id || '',
          valor_total: conta.valor_total || '',
          data_vencimento: conta.data_vencimento || '',
          status: conta.status || '',
        })
        setOrdens(ordensData)
      } catch (err) {
        setError(err.message || 'Erro ao carregar dados')
      } finally {
        setLoading(false)
      }
    }

    loadData()
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
      await atualizarContaReceber(id, {
        ordem_servico_id: Number(form.ordem_servico_id),
        valor_total: Number(form.valor_total),
        data_vencimento: form.data_vencimento,
        status: form.status,
      })
      navigate('/contas')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar conta')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando conta...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Conta</h1>
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
        <label>
          Status
          <select name="status" value={form.status} onChange={handleChange} required>
            <option value="PENDENTE">PENDENTE</option>
            <option value="PAGO">PAGO</option>
          </select>
        </label>
        <button type="submit" disabled={saving}>
          {saving ? 'Atualizando...' : 'Salvar alterações'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
