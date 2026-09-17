import styles from './TenseSubTab.module.css';
import { type TenseData } from './VocabularyTab'

interface TenseSubTabProps {
  tenses: TenseData;
  forms: Record<string, string>;
}

export default function TenseSubTab({ tenses, forms }: TenseSubTabProps) {
  return (
    <div className={styles.container}>

      {/* VERBS */}
      <h2 className={styles.sectionTitle}>Temps des verbes</h2>
      <div className={styles.tenseList}>
        {tenses.verbs.map((tense) => (
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

      {/* ADJECTIVES */}
      <h2 className={styles.sectionTitle}>Temps des adjectifs</h2>
      <div className={styles.tenseList}>
        {tenses.adjectives.map((tense) => (
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
  )
}
