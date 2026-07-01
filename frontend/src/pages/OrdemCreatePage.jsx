import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { criarOrdem, listarClientes, listarServicos } from '../services/api'

export default function OrdemCreatePage() {
  const [form, setForm] = useState({ descricao: '', status: 'ABERTA', cliente_id: '', aparelho_id: '' })
  const [clientes, setClientes] = useState([])
  const [servicos, setServicos] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  useEffect(() => {
    const loadDependencies = async () => {
      try {
        const [clientesData, servicosData] = await Promise.all([listarClientes(), listarServicos()])
        setClientes(clientesData)
        setServicos(servicosData)
      } catch (err) {
        setError('Erro ao carregar clientes ou serviços')
      }
    }

    loadDependencies()
  }, [])

  const handleChange = (event) => {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    setLoading(true)

    try {
      await criarOrdem({
        descricao: form.descricao,
        status: form.status,
        cliente_id: Number(form.cliente_id),
        aparelho_id: Number(form.aparelho_id),
      })
      navigate('/ordens')
    } catch (err) {
      setError(err.message || 'Erro ao cadastrar ordem')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page-container">
      <h1>Nova Ordem de Serviço</h1>
      <form className="card-form" onSubmit={handleSubmit}>
        <label>
          Descrição
          <textarea name="descricao" value={form.descricao} onChange={handleChange} required />
        </label>
        <label>
          Status
          <select name="status" value={form.status} onChange={handleChange}>
            <option value="ABERTA">ABERTA</option>
            <option value="EM_ANDAMENTO">EM ANDAMENTO</option>
            <option value="FINALIZADA">FINALIZADA</option>
          </select>
        </label>
        <label>
          Cliente
          <select name="cliente_id" value={form.cliente_id} onChange={handleChange} required>
            <option value="">Selecione um cliente</option>
            {clientes.map((cliente) => (
              <option key={cliente.id} value={cliente.id}>{cliente.nome}</option>
            ))}
          </select>
        </label>
        <label>
          Aparelho ID
          <input name="aparelho_id" type="number" value={form.aparelho_id} onChange={handleChange} required placeholder="Digite o ID do aparelho" />
        </label>
        <button type="submit" disabled={loading}>
          {loading ? 'Salvando...' : 'Salvar ordem'}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  )
}
