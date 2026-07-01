import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarContasReceber, pagarContaReceber } from '../services/api'

export default function ContasPage() {
  const [contas, setContas] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [savingId, setSavingId] = useState(null)

  useEffect(() => {
    const loadContas = async () => {
      setLoading(true)
      setError('')
      try {
        const data = await listarContasReceber()
        setContas(data)
      } catch (err) {
        setError(err.message || 'Erro ao carregar contas a receber')
      } finally {
        setLoading(false)
      }
    }

    loadContas()
  }, [])

  const handlePagar = async (id) => {
    setError('')
    setSavingId(id)
    try {
      const updated = await pagarContaReceber(id)
      setContas((current) => current.map((conta) => (conta.id === id ? updated : conta)))
    } catch (err) {
      setError(err.message || 'Erro ao marcar conta como paga')
    } finally {
      setSavingId(null)
    }
  }

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>Contas a Receber</h1>
        <Link to="/contas/novo" className="primary-button">
          Nova conta
        </Link>
      </div>
      {loading && <p>Carregando contas...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Ordem</th>
              <th>Valor</th>
              <th>Vencimento</th>
              <th>Status</th>
              <th>Ações</th>
            </tr>
          </thead>
          <tbody>
            {contas.length > 0 ? (
              contas.map((conta) => (
                <tr key={conta.id}>
                  <td>{conta.id}</td>
                  <td>{conta.ordem_servico_id}</td>
                  <td>{`R$ ${conta.valor_total}`}</td>
                  <td>{new Date(conta.data_vencimento).toLocaleDateString()}</td>
                  <td>{conta.status}</td>
                  <td>
                    <Link to={`/contas/${conta.id}/editar`} className="small-button">
                      Editar
                    </Link>
                    {conta.status !== 'PAGO' ? (
                      <button
                        type="button"
                        className="small-button"
                        onClick={() => handlePagar(conta.id)}
                        disabled={savingId === conta.id}
                      >
                        {savingId === conta.id ? 'Processando...' : 'Marcar pago'}
                      </button>
                    ) : (
                      <span>Pago</span>
                    )}
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="7">Nenhuma conta a receber cadastrada.</td>
              </tr>
            )}
          </tbody>
        </table>
      )}
    </div>
  )
}
