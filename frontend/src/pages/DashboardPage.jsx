import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarClientes, listarOrdens, listarServicos, listarFuncionarios, listarVisitas, listarContasReceber } from '../services/api'

export default function DashboardPage() {
  const [stats, setStats] = useState({ clientes: 0, ordens: 0, servicos: 0, funcionarios: 0, visitas: 0, contas: 0 })
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    const loadStats = async () => {
      setLoading(true)
      setError('')
      try {
        const [clientes, ordens, servicos, funcionarios, visitas, contas] = await Promise.all([
          listarClientes(),
          listarOrdens(),
          listarServicos(),
          listarFuncionarios(),
          listarVisitas(),
          listarContasReceber(),
        ])

        setStats({
          clientes: clientes.length,
          ordens: ordens.length,
          servicos: servicos.length,
          funcionarios: funcionarios.length,
          visitas: visitas.length,
          contas: contas.length,
        })
      } catch (err) {
        setError(err.message || 'Erro ao carregar dashboard')
      } finally {
        setLoading(false)
      }
    }

    loadStats()
  }, [])

  return (
    <div className="page-container">
      <div className="page-header">
        <div>
          <h1>Dashboard</h1>
          <p>Visão geral rápida do sistema.</p>
        </div>
        <div className="dashboard-actions">
          <Link to="/clientes" className="primary-button">
            Clientes
          </Link>
          <Link to="/ordens" className="primary-button secondary">
            Ordens
          </Link>
          <Link to="/servicos" className="primary-button secondary">
            Serviços
          </Link>
          <Link to="/funcionarios" className="primary-button secondary">
            Funcionários
          </Link>
          <Link to="/visitas" className="primary-button secondary">
            Visitas
          </Link>
          <Link to="/contas" className="primary-button secondary">
            Contas
          </Link>
        </div>
      </div>

      {loading && <p>Carregando dados...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && (
        <div className="dashboard-grid">
          <div className="dashboard-card">
            <h2>Clientes</h2>
            <p>{stats.clientes}</p>
          </div>
          <div className="dashboard-card">
            <h2>Ordens</h2>
            <p>{stats.ordens}</p>
          </div>
          <div className="dashboard-card">
            <h2>Serviços</h2>
            <p>{stats.servicos}</p>
          </div>
          <div className="dashboard-card">
            <h2>Funcionários</h2>
            <p>{stats.funcionarios}</p>
          </div>
          <div className="dashboard-card">
            <h2>Visitas</h2>
            <p>{stats.visitas}</p>
          </div>
          <div className="dashboard-card">
            <h2>Contas</h2>
            <p>{stats.contas}</p>
          </div>
        </div>
      )}
    </div>
  )
}
