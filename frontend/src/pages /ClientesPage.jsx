import { useEffect, useState } from 'react'
import { listarClientes } from '../services/api'

export default function ClientesPage() {
  const [clientes, setClientes] = useState([])

  useEffect(() => {
    listarClientes().then(setClientes)
  }, [])

  return (
    <div>
      <h1>Clientes</h1>
      <ul>
        {clientes.map((cliente) => (
          <li key={cliente.id}>{cliente.nome}</li>
        ))}
      </ul>
    </div>
  )
}