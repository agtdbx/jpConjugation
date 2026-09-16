import styles from './WordCategorySelector.module.css';
import Section from "../../components/Section";
import Toggle from "../../components/Toggle";
import Button from "../../components/Button";
import { type CategorySchema, type CategorySelection } from "../../App";

interface WordCategorySelectorProps {
  categoryKey: string;
  schema: CategorySchema;
  categorySelection: CategorySelection;
  onToggle: (categoryKey: string, subCategory: 'types' | 'tenses' | 'chainedTenses', id: string) => void;
}

export default function WordCategorySelector({ categoryKey, schema, categorySelection, onToggle }: WordCategorySelectorProps) {
  return (
    <Section title={schema.title}>
      {/* Display types */}
      <div className={styles.subCategory}>
        <h3>Types</h3>
        <div className={styles.toggleContainer}>
          {Object.entries(schema.types).map(([id, label]) => (
              <Toggle
                key={id}
                text={label}
                isToggled={categorySelection.types.includes(id)}
                callback={() => onToggle(categoryKey, 'types', id)}
                />
          ))}
        </div>
      </div>

      {/* Display tenses */}
      <div className={styles.subCategory}>
        <h3>Temps simples</h3>
        <div className={styles.toggleContainer}>
          {Object.entries(schema.values).map(([id, label]) => (
            <Toggle
              key={id}
              text={label}
              isToggled={categorySelection.tenses.includes(id)}
              callback={() => onToggle(categoryKey, 'tenses', id)}
            />
          ))}
        </div>
      </div>

      {/* Display chained tenses */}
      <div className={styles.subCategory}>
        <h3>Combinaisons</h3>
        <div className={styles.toggleContainer}>
          {categorySelection.chainedTenses.map((id) => (
            <Toggle
              key={id}
              text={id} // TODO: Compute id
              isToggled={true} // false = remove
              callback={() => onToggle(categoryKey, 'chainedTenses', id)}
            />
          ))}
          <Button
            text="+ Nouvelle combinaison"
            isDisable={false}
            callback={()=>{}}
            variant="secondary"
          />
        </div>
      </div>
    </Section>
  )
}
