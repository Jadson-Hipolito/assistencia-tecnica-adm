import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarOrdens } from '../services/api'

export default function OrdensPage() {
  const [ordens, setOrdens] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadOrdens = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarOrdens()
        setOrdens(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar ordens')
      } finally {
        setLoading(false)
      }
    }

    loadOrdens()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Ordens de Serviço</h1>
        <Link to="/ordens/novo" className="primary-button">
          Nova ordem
        </Link>
      </div>
      {loading && <p>Carregando ordens...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Descrição</th>
              <th>Status</th>
              <th>Valor Total</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {ordens.length > 0 ? (
              ordens.map((ordem) => (
                <tr key={ordem.id}>
                  <td>{ordem.id}</td>
                  <td>{ordem.descricao || 'Sem descrição'}</td>
                  <td>{ordem.status || 'N/A'}</td>
                  <td>{ordem.valor_total ? `R$ ${ordem.valor_total}` : 'R$ 0,00'}</td>
                  <td>
                    <Link to={`/ordens/${ordem.id}`} className="small-button">
                      Ver detalhes
                    </Link>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5">Nenhuma ordem cadastrada.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
