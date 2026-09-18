import styles from './TenseSubTab.module.css';
import { useState } from 'react'
import { type TenseData, type TenseVerbData, type TenseAdjectiveData } from './VocabularyTab'

interface TenseSubTabProps {
  tenses: TenseData;
  forms: Record<string, string>;
}

export default function TenseSubTab({ tenses, forms }: TenseSubTabProps) {
  const [search, setSearch] = useState<string>('')
  const [sort, setSort] = useState<'order' | 'name'>('order');

  const sortVerbOrder = (a: TenseVerbData, b: TenseVerbData) => a.order - b.order;
  const sortVerbName = (a: TenseVerbData, b: TenseVerbData) => a.name.localeCompare(b.name, 'ja');
  const sortAdjectiveOrder = (a: TenseAdjectiveData, b: TenseAdjectiveData) => a.order - b.order;
  const sortAdjectiveName = (a: TenseAdjectiveData, b: TenseAdjectiveData) => a.name.localeCompare(b.name, 'ja');

  let sortVerbFunction = sortVerbOrder;
  let sortAdjectiveFunction = sortAdjectiveOrder;
  if (sort === 'name') {
    sortVerbFunction = sortVerbName;
    sortAdjectiveFunction = sortAdjectiveName;
  }

  // Apply search
  const visibleVerbTenses = tenses.verbs.filter((tense) => {
    if (!search.trim()) return true;

    const lowerSearch = search.toLowerCase();

    return (
      tense.name.toLowerCase().includes(lowerSearch) ||
      tense.info.toLowerCase().includes(lowerSearch)
    );
  }).sort(sortVerbFunction);

  const visibleAdjectiveTenses = tenses.adjectives.filter((tense) => {
    if (!search.trim()) return true;

    const lowerSearch = search.toLowerCase();

    return (
      tense.name.toLowerCase().includes(lowerSearch) ||
      tense.info.toLowerCase().includes(lowerSearch)
    );
  }).sort(sortAdjectiveFunction);

  return (
    <div className={styles.container}>

      <div className={styles.options}>
        <input
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          className={styles.searchBar}
          placeholder="Rechercher par nom, description..."
        />
        <select
          value={sort}
          onChange={(event) => setSort(event.target.value as 'order' | 'name')}
          className={styles.sort}
        >
          <option value="order">Ordre</option>
          <option value="name">Nom</option>
        </select>
      </div>

      <div className={styles.sections}>
        {/* VERBS */}
        <div className={styles.subSections}>
          <h2 className={styles.sectionTitle}>Temps des verbes</h2>
          {visibleVerbTenses.length === 0 && (
            <p className={styles.noResults}>Aucun résultat.</p>
          )}
          <div className={styles.tenseList}>
            {visibleVerbTenses.map((tense) => (
              <div className={styles.card} key={tense.name}>
                <div className={styles.cardHeader}>
                  <h3 className={styles.tenseName}>{tense.name}</h3>
                  <span className={styles.badge}>Ordre : {tense.order}</span>
                </div>
                <p className={styles.info}>{tense.info}</p>

                <div className={styles.rulesContainer}>
                  <div className={`${styles.tableHeader} ${styles.gridVerbs}`}>
                    <p>Forme</p>
                    <p>Godan</p>
                    <p>Ichidan</p>
                    <p>Exception (suru)</p>
                  </div>

                  {Object.entries(tense.rules.godan).map(([id, rule]) => (
                    <div key={id} className={`${styles.ruleRow} ${styles.gridVerbs}`}>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Forme</span>
                        <strong>{forms[id]}</strong>
                      </div>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Godan</span>
                        <span>{rule}</span>
                      </div>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Ichidan</span>
                        <span>{tense.rules.ichidan[id]}</span>
                      </div>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Exception</span>
                        <span>{tense.rules.exception[id]}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* ADJECTIVES */}
        <div className={styles.subSections}>
          <h2 className={styles.sectionTitle}>Temps des adjectifs</h2>
          {visibleAdjectiveTenses.length === 0 && (
            <p className={styles.noResults}>Aucun résultat.</p>
          )}
          <div className={styles.tenseList}>
            {visibleAdjectiveTenses.map((tense) => (
              <div className={styles.card} key={tense.name}>
                <div className={styles.cardHeader}>
                  <h3 className={styles.tenseName}>{tense.name}</h3>
                  <span className={styles.badge}>Ordre : {tense.order}</span>
                </div>
                <p className={styles.info}>{tense.info}</p>

                <div className={styles.rulesContainer}>
                  <div className={`${styles.tableHeader} ${styles.gridAdjs}`}>
                    <p>Forme</p>
                    <p>Adjectif-i</p>
                    <p>Adjectif-na</p>
                  </div>

                  {Object.entries(tense.rules.i).map(([id, rule]) => (
                    <div key={id} className={`${styles.ruleRow} ${styles.gridAdjs}`}>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Forme</span>
                        <strong>{forms[id]}</strong>
                      </div>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Adjectif-i</span>
                        <span>{rule}</span>
                      </div>
                      <div className={styles.cell}>
                        <span className={styles.mobileLabel}>Adjectif-na</span>
                        <span>{tense.rules.na[id]}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>

      </div>
    </div>
  )
}
