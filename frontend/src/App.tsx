import { useState } from 'react';
import Home from './pages/Home'
import Session from './pages/Session'
import { useLocalStorage } from "./hooks/useLocalStorage"

export interface ExerciceData {
  romaji: string;
  kanji: string;
  traduction: string;
  form: string;
  tense: string;
  rules: string[];
  result: string;
}

export interface SectionSchema {
  title: string;
  types: Record<string, string>;
  values: Record<string, string>;
}

export interface SchemaData {
  sections: Record<string, SectionSchema>;
}

export interface Options {
  number_conjugation: number;
  displayMode: string;
  displayRules: boolean;
  sections: Record<string, { types: string[], values: string[] }>;
}

function App() {
  const [exercices, setExercices] = useState<ExerciceData[] | null>(null);
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
