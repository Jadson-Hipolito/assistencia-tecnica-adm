import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarFuncionarios } from '../services/api'

export default function FuncionarioPage() {
  const [funcionarios, setFuncionarios] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadData = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarFuncionarios()
        setFuncionarios(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar funcionários')
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Funcionários</h1>
        <Link to="/funcionarios/novo" className="primary-button">
          Novo funcionário
        </Link>
      </div>
      {loading && <p>Carregando funcionários...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>E-mail</th>
              <th>Cargo</th>
              <th>Telefone</th>
              <th>Ativo</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {funcionarios.length > 0 ? (
              funcionarios.map((funcionario) => (
                <tr key={funcionario.id}>
                  <td>{funcionario.id}</td>
                  <td>{funcionario.nome}</td>
                  <td>{funcionario.email}</td>
                  <td>{funcionario.cargo}</td>
                  <td>{funcionario.telefone}</td>
                  <td>{funcionario.ativo ? 'Sim' : 'Não'}</td>
                  <td>
                    <Link to={`/funcionarios/${funcionario.id}/editar`} className="small-button">
                      Editar
                    </Link>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7">Nenhum funcionário cadastrado.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
