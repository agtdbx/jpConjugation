import { useState } from 'react';
import Home from './pages/Home'
import Session from './pages/Session'

function App() {
  const [exercices, setExercices] = useState<any[] | null>(null);

  if (!exercices) {
    return <Home onStart={(data) => setExercices(data)} />;
  }

  return (
    <Session
      exercices={exercices}
      onFinish={() => setExercices(null)}
    />
  );
}

export default App