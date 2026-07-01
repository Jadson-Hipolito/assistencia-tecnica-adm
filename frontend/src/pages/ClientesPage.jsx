import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarClientes } from '../services/api'

export default function ClientesPage() {
  const [clientes, setClientes] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadClientes = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarClientes()
        setClientes(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar clientes')
      } finally {
        setLoading(false)
      }
    }

    loadClientes()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Clientes</h1>
        <Link to="/clientes/novo" className="primary-button">
          Novo cliente
        </Link>
      </div>
      {loading && <p>Carregando clientes...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Documento</th>
              <th>Endereço</th>
              <th>Contato</th>
              <th>Ativo</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {clientes.length > 0 ? (
              clientes.map((cliente) => (
                <tr key={cliente.id}>
                  <td>{cliente.id}</td>
                  <td>{cliente.nome}</td>
                  <td>{cliente.documento || 'N/A'}</td>
                  <td>{cliente.endereco || 'N/A'}</td>
                  <td>{cliente.contato || 'N/A'}</td>
                  <td>{cliente.ativo ? 'Sim' : 'Não'}</td>
                  <td>
                    <div className="row-actions">
                      <Link to={`/clientes/${cliente.id}/editar`} className="small-button">
                        Editar
                      </Link>
                      <Link to={`/clientes/${cliente.id}/excluir`} className="small-button danger-button">
                        Excluir
                      </Link>
                    </div>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7">Nenhum cliente cadastrado.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
