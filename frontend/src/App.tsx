import { useState } from 'react';
import Home from './pages/Home'
import Session from './pages/Session'
import { useLocalStorage } from "./hooks/useLocalStorage"

export interface Options {
  number_conjugation: number;
  displayMode: string;
  displayRules: boolean;
  sections: Record<string, { types: string[], values: string[] }>;
}

function App() {
  const [exercices, setExercices] = useState<any[] | null>(null);
  const [options, setOptions] = useLocalStorage<Options>('jp-conjugation-options', {
    number_conjugation: 10,
    displayMode: "romaji",
    displayRules: true,
    sections: {}
  })

  if (!exercices) {
    return <Home
      options={options}
      setOptions={setOptions}
      onStart={(data) => setExercices(data)}
    />;
  }

  return (
    <Session
      options={options}
      exercices={exercices}
      onFinish={() => setExercices(null)}
    />
  );
}

export default App