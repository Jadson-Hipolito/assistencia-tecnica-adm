import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarAparelhos } from '../services/api'

export default function AparelhoPage() {
  const [aparelhos, setAparelhos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarAparelhos()
        setAparelhos(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar aparelhos')
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Aparelhos</h1>
        <Link to="/aparelhos/novo" className="primary-button">
          Novo aparelho
        </Link>
      </div>
      {loading && <p>Carregando aparelhos...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Tipo</th>
              <th>Marca</th>
              <th>Modelo</th>
              <th>Série</th>
              <th>Cliente ID</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {aparelhos.length > 0 ? (
              aparelhos.map((aparelho) => (
                <tr key={aparelho.id}>
                  <td>{aparelho.id}</td>
                  <td>{aparelho.tipo}</td>
                  <td>{aparelho.marca}</td>
                  <td>{aparelho.modelo}</td>
                  <td>{aparelho.numero_serie}</td>
                  <td>{aparelho.cliente_id}</td>
                  <td>
                    <Link to={`/aparelhos/${aparelho.id}/editar`} className="small-button">
                      Editar
                    </Link>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7">Nenhum aparelho cadastrado.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
