import { Navigate, Route, Routes } from 'react-router-dom'
import Header from './components/Header'
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import ClientesPage from './pages/ClientesPage'
import ClienteCreatePage from './pages/ClienteCreatePage'
import ClienteEditPage from './pages/ClienteEditPage'
import ClienteDeletePage from './pages/ClienteDeletePage'
import OrdensPage from './pages/OrdensPage'
import OrdemCreatePage from './pages/OrdemCreatePage'
import OrdemDetailPage from './pages/OrdemDetailPage'
import OrdemEditPage from './pages/OrdemEditPage'
import ServicosPage from './pages/ServicosPage'
import FuncionarioPage from './pages/FuncionarioPage'
import FuncionarioCreatePage from './pages/FuncionarioCreatePage'
import FuncionarioEditPage from './pages/FuncionarioEditPage'
import AparelhoPage from './pages/AparelhoPage'
import AparelhoCreatePage from './pages/AparelhoCreatePage'
import AparelhoEditPage from './pages/AparelhoEditPage'
import EquipamentoPage from './pages/EquipamentoPage'
import EquipamentoCreatePage from './pages/EquipamentoCreatePage'
import EquipamentoEditPage from './pages/EquipamentoEditPage'
import VisitaPage from './pages/VisitaPage'
import VisitaCreatePage from './pages/VisitaCreatePage'
import VisitaEditPage from './pages/VisitaEditPage'
import ContasPage from './pages/ContasPage'
import ContasCreatePage from './pages/ContasCreatePage'
import ContasEditPage from './pages/ContasEditPage'
import { useAuth } from './context/AuthContext'

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth()

  if (loading) return <p>Carregando...</p>
  return user ? children : <Navigate to="/login" replace />
}

function AppLayout({ children }) {
  return (
    <>
      <Header />
      <main>{children}</main>
    </>
  )
}

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <AppLayout>
              <DashboardPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/clientes/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ClienteCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/clientes/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ClienteEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/clientes/:id/excluir"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ClienteDeletePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/clientes"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ClientesPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/ordens/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <OrdemCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/ordens/:id"
        element={
          <ProtectedRoute>
            <AppLayout>
              <OrdemDetailPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/ordens/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <OrdemEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/ordens"
        element={
          <ProtectedRoute>
            <AppLayout>
              <OrdensPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/servicos"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ServicosPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/funcionarios/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <FuncionarioCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/funcionarios/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <FuncionarioEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/funcionarios"
        element={
          <ProtectedRoute>
            <AppLayout>
              <FuncionarioPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/aparelhos/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <AparelhoCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/aparelhos/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <AparelhoEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/aparelhos"
        element={
          <ProtectedRoute>
            <AppLayout>
              <AparelhoPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/equipamentos/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <EquipamentoCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/equipamentos/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <EquipamentoEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/equipamentos"
        element={
          <ProtectedRoute>
            <AppLayout>
              <EquipamentoPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/visitas/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <VisitaCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/visitas/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <VisitaEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/visitas"
        element={
          <ProtectedRoute>
            <AppLayout>
              <VisitaPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/contas/novo"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ContasCreatePage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/contas/:id/editar"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ContasEditPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/contas"
        element={
          <ProtectedRoute>
            <AppLayout>
              <ContasPage />
            </AppLayout>
          </ProtectedRoute>
        }
      />
      <Route path="/" element={<Navigate to="/dashboard" replace />} />
      <Route path="*" element={<Navigate to="/login" replace />} />
    </Routes>
  )
}
