import styles from './Home.module.css';
import { useState } from 'react'
import { type Options, type ExerciceData } from "../App"
import ConjugationTab from '../features/conjugation/ConjugationTab'

interface HomeProps {
  options: Options;
  setOptions: (data: React.SetStateAction<Options>) => void;
  onStart: (data: ExerciceData[]) => void;
}

export default function Home({ options, setOptions, onStart }: HomeProps) {
  const [activeTab, setActiveTab] = useState<'conjugation' | 'vocabulary'>('conjugation');

  const getTabClass = (tabId: string) => {
    if (tabId === activeTab) return styles.activeTab;
    return '';
  }

  return (
    <div className={styles.container}>

      {/* Tabs */}
      <div className={styles.tabs}>
        <button className={getTabClass('conjugation')} onClick={() => setActiveTab('conjugation')}>Conjugaison</button>
        <button className={getTabClass('vocabulary')} onClick={() => setActiveTab('vocabulary')}>Vocabulaire</button>
      </div>

      {/* Content */}
      {activeTab === 'conjugation' && (
        <ConjugationTab
          options={options}
          setOptions={setOptions}
          onStart={onStart} />
      )}
      {/* {activeTab === 'vocabulary' && <VocabularyTab />} */}
    </div>
  );
}
