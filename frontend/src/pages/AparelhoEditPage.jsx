import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { atualizarAparelho, getAparelho, listarClientes } from '../services/api'

export default function AparelhoEditPage() {
  const { id } = useParams()
  const [form, setForm] = useState({ tipo: '', marca: '', modelo: '', numero_serie: '', cliente_id: '' })
  const [clientes, setClientes] = useState([])
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const [aparelhoData, clientesData] = await Promise.all([getAparelho(id), listarClientes()])
        setForm({
          tipo: aparelhoData.tipo || '',
          marca: aparelhoData.marca || '',
          modelo: aparelhoData.modelo || '',
          numero_serie: aparelhoData.numero_serie || '',
          cliente_id: aparelhoData.cliente_id || '',
        })
        setClientes(clientesData)
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
      await atualizarAparelho(id, {
        tipo: form.tipo,
        marca: form.marca,
        modelo: form.modelo,
        numero_serie: form.numero_serie,
        cliente_id: Number(form.cliente_id),
      })
      navigate('/aparelhos')
    } catch (err) {
      setError(err.message || 'Erro ao atualizar aparelho')
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando aparelho...</p></div>
  }

  return (
    <div className="page-container">
      <h1>Editar Aparelho</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Tipo
          <input name="tipo" value={form.tipo} onChange={handleChange} required />
        </label>
        <label>
          Marca
          <input name="marca" value={form.marca} onChange={handleChange} required />
        </label>
        <label>
          Modelo
          <input name="modelo" value={form.modelo} onChange={handleChange} required />
        </label>
        <label>
          Número de série
          <input name="numero_serie" value={form.numero_serie} onChange={handleChange} required />
        </label>
        <label>
          Cliente
          <select name="cliente_id" value={form.cliente_id} onChange={handleChange} required>
            <option value="">Selecione um cliente</option>
            {clientes.map((cliente) => (
              <option key={cliente.id} value={cliente.id}>
                {cliente.nome}
              </option>
            ))}
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
