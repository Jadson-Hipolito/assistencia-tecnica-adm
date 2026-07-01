import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarEquipamento, getEquipamento } from '../services/api'

export default function EquipamentoEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ nome: '', tipo: '', marca: '', modelo: '', codigo: '', descricao: '' })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadEquipamento = async () => {
      setLoading(true)
      setError('')
      try {
        const equipamento = await getEquipamento(id)
        setForm({
          nome: equipamento.nome || '',
          tipo: equipamento.tipo || '',
          marca: equipamento.marca || '',
          modelo: equipamento.modelo || '',
          codigo: equipamento.codigo || '',
          descricao: equipamento.descricao || '',
        })
      } catch (err) {
        setError(err.message || 'Erro ao carregar equipamento')
      } finally {
        setLoading(false)
      }
    }

    loadEquipamento()
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
      await atualizarEquipamento(id, form)
      navigate('/equipamentos')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar equipamento')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando equipamento...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Equipamento</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Nome
          <input name="nome" value={form.nome} onChange={handleChange} required />
        </label>
        <label>
          Tipo
          <input name="tipo" value={form.tipo} onChange={handleChange} required />
        </label>
        <label>
          Marca
          <input name="marca" value={form.marca} onChange={handleChange} />
        </label>
        <label>
          Modelo
          <input name="modelo" value={form.modelo} onChange={handleChange} />
        </label>
        <label>
          Código
          <input name="codigo" value={form.codigo} onChange={handleChange} required />
        </label>
        <label>
          Descrição
          <textarea name="descricao" value={form.descricao} onChange={handleChange} />
        </label>
        <button type="submit" disabled={saving}>
          {saving ? 'Atualizando...' : 'Salvar alterações'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
