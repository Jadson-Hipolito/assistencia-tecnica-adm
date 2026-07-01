import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarVisita, listarFuncionarios, listarOrdens } from '../services/api'

export default function VisitaCreatePage() {
  const [form, setForm] = useState({ ordem_servico_id: '', funcionario_id: '', data_agendamento: new Date().toISOString().slice(0, 16) })
  const [ordens, setOrdens] = useState([])
  const [funcionarios, setFuncionarios] = useState([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadOptions = async () => {
      setLoading(true)
      try {
        const [ordensData, funcionariosData] = await Promise.all([listarOrdens(), listarFuncionarios()])
        setOrdens(ordensData)
        setFuncionarios(funcionariosData)
      } catch (err) {
        setError(err.message || 'Erro ao carregar dados')
      } finally {
        setLoading(false)
      }
    }

    loadOptions()
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
      await criarVisita({
        ordem_servico_id: Number(form.ordem_servico_id),
        funcionario_id: form.funcionario_id ? Number(form.funcionario_id) : null,
        data_agendamento: form.data_agendamento,
      })
      navigate('/visitas')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar visita')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Agendar Visita</h1>
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
          Funcionário
          <select name="funcionario_id" value={form.funcionario_id} onChange={handleChange}>
            <option value="">Não atribuir</option>
            {funcionarios.map((funcionario) => (
              <option key={funcionario.id} value={funcionario.id}>
                {funcionario.nome}
              </option>
            ))}
          </select>
        </label>
        <label>
          Data de agendamento
          <input
            name="data_agendamento"
            type="datetime-local"
            value={form.data_agendamento}
            onChange={handleChange}
            required
          />
        </label>
        <button type="submit" disabled={saving || loading}>
          {saving ? 'Salvando...' : 'Agendar visita'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
