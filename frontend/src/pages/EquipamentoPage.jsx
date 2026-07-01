import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarEquipamentos } from '../services/api'

export default function EquipamentoPage() {
  const [equipamentos, setEquipamentos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarEquipamentos()
        setEquipamentos(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar equipamentos')
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Equipamentos</h1>
        <Link to="/equipamentos/novo" className="primary-button">
          Novo equipamento
        </Link>
      </div>
      {loading && <p>Carregando equipamentos...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Tipo</th>
              <th>Marca</th>
              <th>Modelo</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {equipamentos.length > 0 ? (
              equipamentos.map((equipamento) => (
                <tr key={equipamento.id}>
                  <td>{equipamento.id}</td>
                  <td>{equipamento.nome}</td>
                  <td>{equipamento.tipo}</td>
                  <td>{equipamento.marca}</td>
                  <td>{equipamento.modelo}</td>
                  <td>
                    <Link to={`/equipamentos/${equipamento.id}/editar`} className="small-button">
                      Editar
                    </Link>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="6">Nenhum equipamento cadastrado.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
