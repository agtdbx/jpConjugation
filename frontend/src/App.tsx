import { useState } from 'react';
import Home from './pages/Home'
import Session from './pages/Session'
import { useLocalStorage } from "./hooks/useLocalStorage"

// Intern type
export interface ExerciceData {
  romaji: string;
  kanji: string;
  traduction: string;
  form: string;
  tense: string;
  rules: string[];
  result: string;
}

// API Return type
export interface FormSchema {
  title: string;
  values: Record<string, string>;
}

export interface CategorySchema {
  title: string;
  types: Record<string, string>;
  tenses: Record<string, string>;
  orders: Record<string, number>;
}

export interface ConjugationSchema {
  forms: FormSchema;
  categories: Record<string, CategorySchema>;
}

// Options type
export interface CategorySelection {
  types: string[];
  tenses: string[];
  chainedTenses: string[];
}

export interface ConjugationOptions {
  numberConjugation: number;
  displayMode: string;
  displayRules: boolean;
  forms: string[];
  categories: Record<string, CategorySelection>;
}

export interface Options {
  conjugation: ConjugationOptions;
}

function App() {
  const [exercices, setExercices] = useState<ExerciceData[] | null>(null);
  const [options, setOptions] = useLocalStorage<Options>('jp-conjugation-options', {
    conjugation: {
      numberConjugation: 10,
      displayMode: "romaji",
      displayRules: true,
      forms: [],
      categories: {},
    }
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
