import { useState } from 'react';
import styles from './CombinationModal.module.css';
import Button from "../../components/Button";
import Toggle from "../../components/Toggle";
import { type ConjugationSchema } from "../../App";

interface CombinationModalProps {
  schema: ConjugationSchema;
  categoryKey: string;
  onClose: () => void;
  onSave: (chainedTenses: string) => void;
}

export default function CombinationModal({ schema, categoryKey, onClose, onSave }: CombinationModalProps) {
  const [chain, setChain] = useState<string[]>([]);

  // Choose which tenses display
  let tensesToDisplay: Record<string, string> = {};
  if (categoryKey === 'verbs' && chain.includes('de')) {
    tensesToDisplay = { ...schema.categories.adjectives.values };

    chain.forEach(id => {
      if (!tensesToDisplay[id]) {
        tensesToDisplay[id] = schema.categories.verbs.values[id];
      }
    });
  } else {
    tensesToDisplay = { ...schema.categories[categoryKey].values };
  }

  // Get last tense
  const lastTense = chain.length > 0 ? chain[chain.length - 1] : null;

  // Get order number of a tense
  const getWeight = (tenseId: string) => {
    if (schema.categories.adjectives.orders[tenseId] !== undefined) {
      return schema.categories.adjectives.orders[tenseId];
    }
    return schema.categories.verbs.orders[tenseId] ?? 99;
  };

  const currentWeight = lastTense ? getWeight(lastTense) : 99;

  // Handle toggle
  const handleToggle = (id: string) => {
    // Si déjà sélectionné, on coupe la chaîne à partir de cet élément
    if (chain.includes(id)) {
      const index = chain.indexOf(id);
      setChain(chain.slice(0, index));
      return;
    }

    // Sinon on l'ajoute
    setChain([...chain, id]);
  };

  const handleSave = () => {
    if (chain.length > 0) {
      onSave(chain.join('|'));
    }
    onClose();
  };

  return (
    <div className={styles.overlay}>
      <div className={styles.modal}>
        <h2>Nouvelle combinaison</h2>

        <div className={styles.preview}>
          {chain.length === 0 ? (
            <span className={styles.placeholder}>Sélectionnez un temps...</span>
          ) : (
            chain.join(' ➔ ')
          )}
        </div>

        <div className={styles.tenses}>
          {Object.entries(tensesToDisplay).map(([id, label]) => {
            const tenseWeight = getWeight(id);

            const isDisabled = tenseWeight >= currentWeight;
            const isSelected = chain.includes(id);

            const onClick = isDisabled && !isSelected ? () => {} : () => handleToggle(id);

            return (
                <Toggle
                  key={id}
                  text={label}
                  isToggled={isSelected}
                  callback={onClick}
                  className={isDisabled && !isSelected ? styles.disabled : ''}
                />
            );
          })}
        </div>

        <div className={styles.actions}>
          <Button text="Annuler" isDisable={false} callback={onClose} variant="secondary" />
          <Button text="Ajouter" isDisable={chain.length <= 1} callback={handleSave} variant="primary" />
        </div>
      </div>
    </div>
  );
}
