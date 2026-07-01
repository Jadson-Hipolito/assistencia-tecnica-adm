import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { getOrdem } from '../services/api'

export default function OrdemDetailPage() {
  const { id } = useParams()
  const [ordem, setOrdem] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadOrdem = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await getOrdem(id)
        setOrdem(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar ordem')
      } finally {
        setLoading(false)
      }
    }

    loadOrdem()
  }, [id])

  if (loading) {
    return <div className="page-container"><p>Carregando ordem...</p></div>
  }

  if (error) {
    return (
      <div className="page-container">
        <p className="error-message">{error}</p>
      </div>
    )
  }

  if (!ordem) {
    return (
      <div className="page-container">
        <p>Ordem de serviço não encontrada.</p>
      </div>
    )
  }

  return (
    <div className="page-container">
      <div className="page-header">
        <div>
          <h1>Detalhes da Ordem</h1>
        </div>
        <div className="dashboard-actions">
          <Link to={`/ordens/${ordem.id}/editar`} className="primary-button secondary">
            Editar ordem
          </Link>
        </div>
      </div>
      <div className="details-card">
        <p><strong>ID:</strong> {ordem.id}</p>
        <p><strong>Descrição:</strong> {ordem.descricao || 'Sem descrição'}</p>
        <p><strong>Status:</strong> {ordem.status || 'N/A'}</p>
        <p><strong>Valor total:</strong> {ordem.valor_total ? `R$ ${ordem.valor_total}` : 'R$ 0,00'}</p>
        <p><strong>Cliente ID:</strong> {ordem.cliente_id ?? 'N/A'}</p>
        <p><strong>Aparelho ID:</strong> {ordem.aparelho_id ?? 'N/A'}</p>
        <p><strong>Data de abertura:</strong> {ordem.data_abertura ? new Date(ordem.data_abertura).toLocaleString() : 'N/A'}</p>
        <p><strong>Data de fechamento:</strong> {ordem.data_fechamento ? new Date(ordem.data_fechamento).toLocaleString() : 'Ainda aberta'}</p>
      </div>
    </div>
  )
}
