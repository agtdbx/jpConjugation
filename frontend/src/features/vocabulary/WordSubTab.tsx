import styles from './WordSubTab.module.css';
import { type WordData } from './VocabularyTab'

interface WordSubTabProps {
  title: string;
  words: WordData[];
}

export default function WordSubTab({ title, words }: WordSubTabProps) {
  // Display data
  return (
    <div className={styles.container}>
      <h2 className={styles.title}>{title}</h2>

      <div className={styles.grid}>
        {words.map((word) => (
          <div className={styles.card} key={word.romaji}>
            <div className={styles.header}>
              <h3 className={styles.kanji}>{word.kanji}</h3>
              <span className={styles.type}>{word.type}</span>
            </div>
            <p className={styles.kana}>{word.kana} <span className={styles.romaji}>({word.romaji})</span></p>
            <p className={styles.traduction}>{word.traduction}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
