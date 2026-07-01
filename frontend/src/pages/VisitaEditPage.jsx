import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarVisita, getVisita, listarFuncionarios, listarOrdens } from '../services/api'

export default function VisitaEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ ordem_servico_id: '', funcionario_id: '', data_agendamento: '', status: '' })
  const [ordens, setOrdens] = useState([])
  const [funcionarios, setFuncionarios] = useState([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const [visita, ordensData, funcionariosData] = await Promise.all([
          getVisita(id),
          listarOrdens(),
          listarFuncionarios(),
        ])

        setForm({
          ordem_servico_id: visita.ordem_servico_id || '',
          funcionario_id: visita.funcionario_id || '',
          data_agendamento: visita.data_agendamento ? visita.data_agendamento.slice(0, 16) : '',
          status: visita.status || '',
        })
        setOrdens(ordensData)
        setFuncionarios(funcionariosData)
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
      await atualizarVisita(id, {
        ordem_servico_id: Number(form.ordem_servico_id),
        funcionario_id: form.funcionario_id ? Number(form.funcionario_id) : null,
        data_agendamento: form.data_agendamento,
        status: form.status,
      })
      navigate('/visitas')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar visita')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando visita...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Visita</h1>
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
        <label>
          Status
          <select name="status" value={form.status} onChange={handleChange} required>
            <option value="AGENDADA">AGENDADA</option>
            <option value="CONCLUIDA">CONCLUIDA</option>
            <option value="CANCELADA">CANCELADA</option>
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
