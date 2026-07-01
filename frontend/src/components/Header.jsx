import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function Header() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/login')
  }

  return (
    <header className="app-header">
      <div className="app-brand">
        <Link to="/dashboard">Assistência Técnica</Link>
      </div>
      {user ? (
        <nav className="app-nav">
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/clientes">Clientes</Link>
          <Link to="/ordens">Ordens</Link>
          <Link to="/servicos">Serviços</Link>
          <Link to="/funcionarios">Funcionários</Link>
          <Link to="/aparelhos">Aparelhos</Link>
          <Link to="/equipamentos">Equipamentos</Link>
          <Link to="/visitas">Visitas</Link>
          <Link to="/contas">Contas</Link>
          <button type="button" onClick={handleLogout} className="logout-button">
            Sair
          </button>
          <span className="user-badge">{user.nome || user.email}</span>
        </nav>
      ) : null}
    </header>
  )
}
