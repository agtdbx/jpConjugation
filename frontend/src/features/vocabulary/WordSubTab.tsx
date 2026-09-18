import styles from './WordSubTab.module.css';
import { useState } from 'react'
import { type WordData } from './VocabularyTab'

interface WordSubTabProps {
  title: string;
  words: WordData[];
}

export default function WordSubTab({ title, words }: WordSubTabProps) {
  const [search, setSearch] = useState<string>('')
  const [sort, setSort] = useState<'kanji' | 'romaji' | 'type' | 'traduction'>('kanji');

  const sortKanji = (a: WordData, b: WordData) => a.kanji.localeCompare(b.kanji, 'ja');
  const sortRomaji = (a: WordData, b: WordData) => a.romaji.localeCompare(b.romaji);
  const sortType = (a: WordData, b: WordData) => {
    const typeCompare = a.type.localeCompare(b.type);
    if (typeCompare === 0) {
      return a.romaji.localeCompare(b.romaji);
    }
    return typeCompare;
  };
  const sortTraduction = (a: WordData, b: WordData) => a.traduction.localeCompare(b.traduction);

  let sortFunction = sortKanji;
  if (sort === 'romaji') sortFunction = sortRomaji;
  else if (sort === 'type') sortFunction = sortType;
  else if (sort === 'traduction') sortFunction = sortTraduction;

  // Apply search
  const visibleWords = words.filter((word) => {
    if (!search.trim()) return true;

    const lowerSearch = search.toLowerCase();

    return (
      word.kanji.toLowerCase().includes(lowerSearch) ||
      word.kana.toLowerCase().includes(lowerSearch) ||
      word.romaji.toLowerCase().includes(lowerSearch) ||
      word.traduction.toLowerCase().includes(lowerSearch)
    );
  }).sort(sortFunction);

  // Display data
  return (
    <div className={styles.container}>

      <div className={styles.options}>
        <input
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          className={styles.searchBar}
          placeholder="Rechercher par kanji, kana, romaji, traduction..."
        />
        <select
          value={sort}
          onChange={(event) => setSort(event.target.value as 'kanji' | 'romaji' | 'type' | 'traduction')}
          className={styles.sort}
        >
          <option value="kanji">Kanji</option>
          <option value="romaji">Romaji</option>
          <option value="type">Type</option>
          <option value="traduction">Traduction</option>
        </select>
      </div>

      <h2 className={styles.title}>{title}</h2>

      {visibleWords.length === 0 && (
        <p className={styles.noResults}>Aucun résultat.</p>
      )}

      <div className={styles.grid}>
        {visibleWords.map((word) => (
          <div className={styles.card} key={`${word.kanji}-${word.romaji}`}>
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
