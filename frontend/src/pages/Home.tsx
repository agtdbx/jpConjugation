import styles from './Home.module.css';
import { useState, useCallback } from 'react'
import { type Options, type ExerciceData, type ConjugationOptions } from "../App"
import ConjugationTab from '../features/conjugation/ConjugationTab'
import VocabularyTab from '../features/vocabulary/VocabularyTab'

interface HomeProps {
  options: Options;
  setOptions: (data: React.SetStateAction<Options>) => void;
  onStart: (data: ExerciceData[]) => void;
}

export default function Home({ options, setOptions, onStart }: HomeProps) {
  const [activeTab, setActiveTab] = useState<'conjugation' | 'vocabulary'>('conjugation');

  const setConjugationOptions = useCallback((
    updater: React.SetStateAction<ConjugationOptions>
  ) => {
    setOptions((prevGlobalOptions) => {
      const newConjugationOptions =
        typeof updater === 'function'
          ? updater(prevGlobalOptions.conjugation)
          : updater;

      return {
        ...prevGlobalOptions,
        conjugation: newConjugationOptions
      };
    });
  }, [setOptions]);

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
          options={options.conjugation}
          setOptions={setConjugationOptions}
          onStart={onStart} />
      )}
      {activeTab === 'vocabulary' && <VocabularyTab />}
    </div>
  );
}
