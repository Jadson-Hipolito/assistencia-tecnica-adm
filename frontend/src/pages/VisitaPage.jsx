import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarVisitas } from '../services/api'

export default function VisitaPage() {
  const [visitas, setVisitas] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarVisitas()
        setVisitas(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar visitas')
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Visitas Técnicas</h1>
        <Link to="/visitas/novo" className="primary-button">
          Agendar visita
        </Link>
      </div>
      {loading && <p>Carregando visitas...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Ordem</th>
              <th>Funcionário</th>
              <th>Data agendada</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {visitas.length > 0 ? (
              visitas.map((visita) => (
                <tr key={visita.id}>
                  <td>{visita.id}</td>
                  <td>{visita.ordem_servico_id}</td>
                  <td>{visita.funcionario_id || 'N/A'}</td>
                  <td>{new Date(visita.data_agendamento).toLocaleString()}</td>
                  <td>{visita.status}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6">Nenhuma visita cadastrada.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
