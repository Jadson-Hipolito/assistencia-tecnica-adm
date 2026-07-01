import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarEquipamento } from '../services/api'

export default function EquipamentoCreatePage() {
  const [form, setForm] = useState({ nome: '', tipo: '', marca: '', modelo: '', codigo: '', descricao: '' })
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
      await criarEquipamento(form)
      navigate('/equipamentos')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar equipamento')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Novo Equipamento</h1>
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
        <button type="submit" disabled={loading}>
          {loading ? 'Salvando...' : 'Salvar equipamento'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
