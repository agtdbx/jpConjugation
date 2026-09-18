import styles from './VocabularyTab.module.css';
import { useState, useEffect } from 'react'
import WordSubTab from './WordSubTab';
import TenseSubTab from './TenseSubTab';

export interface WordData {
  romaji: string;
  kana: string;
  kanji: string;
  traduction: string;
  type: string;
}

export interface TenseVerbData {
  name: string;
  allowedForms: string[];
  order: number;
  info: string;
  rules: {
    godan: Record<string, string>;
    ichidan: Record<string, string>;
    exception: Record<string, string>;
  };
}

export interface TenseAdjectiveData {
  name: string;
  allowedForms: string[];
  order: number;
  info: string;
  rules: {
    i: Record<string, string>;
    na: Record<string, string>;
  };
}

export interface TenseData {
  verbs: TenseVerbData[];
  adjectives: TenseAdjectiveData[];
}

interface VocabularyData {
  forms: Record<string, string>;
  verbs: WordData[];
  adjectives: WordData[];
  tenses: TenseData;
}

export default function VocabularyTab() {
  // Create states
  const [activeTab, setActiveTab] = useState<'verbs' | 'adjectives' | 'tenses'>('verbs');
  const [data, setData] = useState<VocabularyData | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const getTabClass = (tabId: string) => {
    if (tabId === activeTab) return styles.activeTab;
    return '';
  }

  // Get vocabulary data from api
  useEffect(() => {
    // Get schema
    fetch(`${import.meta.env.VITE_API_URL}/api/vocabulary`)
      .then(res => {
        if (!res.ok) throw new Error("Erreur réseau")
        return res.json()
      })
      .then(vocabularyData => {
        setData(vocabularyData);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      })
  }, [setData])

  // Display loading / error text
  if (loading) return <div>Chargement des données depuis le serveur... (~50 secondes)</div>
  if (error) return <div>Erreur : {error}</div>

  // Display data
  return (
    <div className={styles.container}>
      <div className={styles.tabs}>
        <button className={getTabClass('verbs')} onClick={() => setActiveTab('verbs')}>Verbes</button>
        <button className={getTabClass('adjectives')} onClick={() => setActiveTab('adjectives')}>Adjectifs</button>
        <button className={getTabClass('tenses')} onClick={() => setActiveTab('tenses')}>Temps</button>
      </div>
      {data && activeTab === 'verbs' &&
        <WordSubTab
          title='Verbes'
          words={data.verbs}
        />}
      {data && activeTab === 'adjectives' &&
        <WordSubTab
          title='Adjectifs'
          words={data.adjectives}
        />}
      {data && activeTab === 'tenses' &&
        <TenseSubTab
          tenses={data.tenses}
          forms={data.forms}
        />}
    </div>
  )
}
