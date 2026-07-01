import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarAparelho, listarClientes } from '../services/api'

export default function AparelhoCreatePage() {
  const [form, setForm] = useState({ tipo: '', marca: '', modelo: '', numero_serie: '', cliente_id: '' })
  const [clientes, setClientes] = useState([])
  const [loadingClients, setLoadingClients] = useState(true)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadClientes = async () => {
      setLoadingClients(true)
      try {
        const data = await listarClientes()
        setClientes(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar clientes')
      } finally {
        setLoadingClients(false)
      }
    }

    loadClientes()
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
      await criarAparelho({
        ...form,
        cliente_id: Number(form.cliente_id),
      })
      navigate('/aparelhos')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar aparelho')
    } finally {
      setSaving(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Novo Aparelho</h1>
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
        <button type="submit" disabled={saving || loadingClients}>
          {saving ? 'Salvando...' : 'Salvar aparelho'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
