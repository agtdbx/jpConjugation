import { useState, useEffect } from 'react'


export default function Home() {
  // Create states
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  // Setup first call at first page render

  useEffect(() => {
    fetch('http://localhost:8000/api/options')
      .then(response => {
        if (!response.ok) throw new Error("Erreur réseau")
        return response.json()
      })
      .then(jsonData => {
        setData(jsonData)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  // Display loading text
  if (loading) return <div>Chargement des options depuis le serveur...</div>
  // Display error
  if (error) return <div>Erreur : {error}</div>

  // Display data
  return (
    <div>
      <h1>Configuration de la session</h1>
      <p>Voici les données brutes envoyées par FastAPI :</p>
      {/* La balise <pre> garde le formatage JSON pour qu'il soit lisible */}
      <pre style={{ textAlign: 'left', background: '#f4f4f4', padding: '1rem', color: 'black' }}>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  )
}