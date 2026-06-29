import { useEffect, useState } from 'react'
import { listarOrdens } from '../services/api'

export default function OrdensPage() {
  const [ordens, setOrdens] = useState([])

  useEffect(() => {
    listarOrdens().then(setOrdens)
  }, [])

  return (
    <div>
      <h1>Ordens de Serviço</h1>
      <ul>
        {ordens.map((ordem) => (
          <li key={ordem.id}>{ordem.descricao || 'Ordem sem descrição'}</li>
        ))}
      </ul>
    </div>
  )
}