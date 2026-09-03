import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Conjugation from './pages/Conjugation'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/conjugation" element={<Conjugation />} />
    </Routes>
  )
}

export default App