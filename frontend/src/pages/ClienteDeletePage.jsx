import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { getCliente, excluirCliente } from '../services/api'

export default function ClienteDeletePage() {
  const { id } = useParams()
  const [cliente, setCliente] = useState(null)
  const [loading, setLoading] = useState(true)
  const [deleting, setDeleting] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  useEffect(() => {
    const loadCliente = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await getCliente(id)
        setCliente(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar cliente')
      } finally {
        setLoading(false)
      }
    }

    loadCliente()
  }, [id])

  const handleDelete = async () => {
    setError('')
    setDeleting(true)
    try {
      await excluirCliente(id)
      navigate('/clientes')
    } catch (err) {
      setError(err.message || 'Erro ao excluir cliente')
    } finally {
      setDeleting(false)
    }
  }

  if (loading) {
    return <div className="page-container"><p>Carregando cliente...</p></div>
  }

  if (error) {
    return (
      <div className="page-container">
        <p className="error-message">{error}</p>
      </div>
    )
  }

  return (
    <div className="page-container">
      <h1>Excluir Cliente</h1>
      <div className="details-card">
        <p><strong>ID:</strong> {cliente.id}</p>
        <p><strong>Nome:</strong> {cliente.nome}</p>
        <p><strong>Documento:</strong> {cliente.documento || 'N/A'}</p>
        <p><strong>Endereço:</strong> {cliente.endereco || 'N/A'}</p>
        <p><strong>Contato:</strong> {cliente.contato || 'N/A'}</p>
        <p><strong>Ativo:</strong> {cliente.ativo ? 'Sim' : 'Não'}</p>
      </div>
      <button type="button" className="danger-button" onClick={handleDelete} disabled={deleting}>
        {deleting ? 'Excluindo...' : 'Confirmar exclusão'}
      </button>
    </div>
  )
}
