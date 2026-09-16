import styles from './WordCategorySelector.module.css';
import Section from "../../components/Section";
import Toggle from "../../components/Toggle";
import Button from "../../components/Button";
import CombinationModal from "./CombinationModal"
import { useState } from 'react'
import { type ConjugationSchema, type CategorySelection } from "../../App";

interface WordCategorySelectorProps {
  categoryKey: string;
  schema: ConjugationSchema;
  categorySelection: CategorySelection;
  onToggle: (categoryKey: string, subCategory: 'types' | 'tenses' | 'chainedTenses', id: string) => void;
}

export default function WordCategorySelector({ categoryKey, schema, categorySelection, onToggle }: WordCategorySelectorProps) {
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);

  const currentSchema = schema.categories[categoryKey];

  const getChainedTensesName = (id: string) => {
    return id.split('|').map((tenseId) =>
      schema.categories["verbs"]?.values[tenseId] ??
      schema.categories["adjectives"]?.values[tenseId] ??
      'Inconnu'
    ).join(' ');
  }

  return (
    <Section title={currentSchema.title}>
      {/* Display types */}
      <div className={styles.subCategory}>
        <h3>Types</h3>
        <div>
          {Object.entries(currentSchema.types).map(([id, label]) => (
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
        <div>
          {Object.entries(currentSchema.values).map(([id, label]) => (
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
        <div>
          {categorySelection.chainedTenses.map((id) => (
            <Toggle
              key={id}
              text={getChainedTensesName(id)}
              isToggled={true} // false = removed
              callback={() => onToggle(categoryKey, 'chainedTenses', id)}
            />
          ))}
        </div>
        <Button
          text="+ Nouvelle combinaison"
          isDisable={false}
          callback={() => {setIsModalOpen(true)}}
          variant="secondary"
        />
      </div>

      {isModalOpen && <CombinationModal
        schema={schema}
        categoryKey={categoryKey}
        onClose={() => {setIsModalOpen(false);}}
        onSave={(chainedTenses: string) => {
          setIsModalOpen(false);
          onToggle(categoryKey, 'chainedTenses', chainedTenses)
        }}
      />}
    </Section>
  )
}
