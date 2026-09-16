import styles from './ConjugationTab.module.css';
import { useState, useEffect } from 'react'
import FormSelector from "./FormSelector";
import WordCategorySelector from "./WordCategorySelector";
import Button from "../../components/Button";
import { type ConjugationOptions, type CategorySelection, type ExerciceData, type ConjugationSchema } from "../../App"

interface ConjugationTabProps {
  options: ConjugationOptions;
  setOptions: (data: React.SetStateAction<ConjugationOptions>) => void;
  onStart: (data: ExerciceData[]) => void;
}

export default function ConjugationTab({ options, setOptions, onStart }: ConjugationTabProps) {
  // Create states
  const [schema, setSchema] = useState<ConjugationSchema | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // Setup first call at first page render
  useEffect(() => {
    // Get schema
    fetch(`${import.meta.env.VITE_API_URL}/api/conjugation/options`)
      .then(res => {
        if (!res.ok) throw new Error("Erreur réseau")
        return res.json()
      })
      .then(fetchedSchema => {
        setSchema(fetchedSchema);

        // Get options
        setOptions(prevOptions => {
          const isOutdated = !prevOptions || !prevOptions.categories || !Array.isArray(prevOptions.forms);

          // If data isn't outdated and not empty, return them
          if (!isOutdated && Object.keys(prevOptions.categories).length > 0) {
            return prevOptions;
          }

          // Else, build default data
          const initialCategories: Record<string, CategorySelection> = {};
          Object.keys(fetchedSchema.categories).forEach(categoryKey => {
            initialCategories[categoryKey] = { types: [], tenses: [], chainedTenses: [] };
          });

          return {
            numberConjugation: prevOptions?.numberConjugation ?? 10,
            displayMode: prevOptions?.displayMode ?? "romaji",
            displayRules: prevOptions?.displayRules ?? true,
            forms: Array.isArray(prevOptions?.forms) ? prevOptions.forms : [],
            categories: initialCategories
          };
        });

        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      })
  }, [setOptions])

  // Display loading text
  if (loading) return <div>Chargement des données depuis le serveur... (~50 secondes)</div>
  // Display error
  if (error) return <div>Erreur : {error}</div>

  const handleFormToggle = (id: string) => {
    setOptions(prev => ({
      ...prev,
      forms: prev.forms.includes(id)
        ? prev.forms.filter(f => f !== id)
        : [...prev.forms, id]
    }));
  };

  const handleCategoryToggle = (categoryKey: string, subCategory: 'types' | 'tenses' | 'chainedTenses', id: string) => {
    setOptions(prev => {
      const currentList = prev.categories[categoryKey][subCategory];
      const newList = currentList.includes(id)
        ? currentList.filter(item => item !== id)
        : [...currentList, id];

      return {
        ...prev,
        categories: {
          ...prev.categories,
          [categoryKey]: {
            ...prev.categories[categoryKey],
            [subCategory]: newList
          }
        }
      };
    });
  };

  const handleNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = parseInt(e.target.value, 10);
    if (!isNaN(value) && value >= 1 && value <= 50) {
      setOptions(prev => ({ ...prev, number_conjugation: value }));
    }
  };

  const handleViewChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setOptions(prev => ({ ...prev, displayMode: e.target.value }));
  };

  const handleSwitchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setOptions(prev => ({ ...prev, displayRules: e.target.checked }));
  };

  const checkIsOptionsValid = () => {
    // If loading or error, disable
    if (!schema || !options.categories || Object.keys(options.categories).length === 0) return false;

    // If no form, disable
    if (options.forms.length === 0) return false;

    // If no category, disable
    const categorieKeys = Object.keys(schema.categories);
    if (categorieKeys.length === 0) return false;

    // Validate categories
    const hasValidTarget = categorieKeys.some(key => {
      const sectionOptions = options.categories[key];
      const sectionSchema = schema.categories[key];

      if (!sectionOptions || !sectionSchema) return false;

      const hasSelectedTypes = sectionOptions.types.length > 0;
      const hasSelectedTenses = sectionOptions.tenses.length > 0;
      const hasSelectedChainedTenses = sectionOptions.chainedTenses.length > 0;

      return (hasSelectedTypes && (hasSelectedTenses || hasSelectedChainedTenses))
    });

    return hasValidTarget;
  };

  const isSubmitDisabled = !checkIsOptionsValid();

  const hanbleButtonClic = () => {
    const formattedCategories = Object.keys(options.categories).reduce((acc, key) => {
      const cat = options.categories[key];

      acc[key] = {
        types: cat?.types ?? [],
        tenses: [
          ...(cat?.tenses ?? []),
          ...(cat?.chainedTenses ?? [])
        ]
      };

      return acc;
    }, {} as Record<string, { types: string[], tenses: string[] }>);

    const sendOptions = {
      ...options,
      categories: formattedCategories
    };

    fetch(`${import.meta.env.VITE_API_URL}/api/conjugation/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(sendOptions),
    }).then(res => {
        if (!res.ok) throw new Error("Erreur réseau")
        return res.json()
      }).then(exercices => {
        onStart(exercices);
      })
      .catch(err => {
        setError(err.message);
      });
  }

  // Display data
  return (
      <div className={styles.container}>
        <h1 className={styles.title}>Configuration de la session</h1>
        <div className={styles.settingsGrid}>

          <div className={`${styles.optionGroup} ${styles.fullWidth}`}>
            <h3>Nombre d'exercices : {options.numberConjugation}</h3>
            <input
              type="range"
              min="1"
              max="50"
              value={options.numberConjugation}
              onChange={handleNumberChange}
              className={styles.slider}
            />
          </div>

          <div className={styles.optionGroup}>
            <h3>Écritures du mot à conjuguer</h3>
            <select
              value={options.displayMode}
              onChange={handleViewChange}
              className={styles.select}
            >
              <option value="romaji">Romaji</option>
              <option value="kanji">Kanji</option>
              <option value="traduction">Traduction</option>
            </select>
          </div>

          <div className={styles.optionGroup}>
            <div className={styles.checkboxWrapper}>
              <h3 style={{ margin: 0 }}>Afficher la règle en cas d'erreur</h3>
              <input
                type="checkbox"
                checked={options.displayRules}
                onChange={handleSwitchChange}
                className={styles.checkbox}
              />
            </div>
          </div>

        </div>

        {schema && <FormSelector
            schema={schema.forms}
            selectedForms={options.forms}
            onToggle={handleFormToggle}
          />
        }

        {schema && Object.entries(schema.categories).map(([key]) => (
          <WordCategorySelector
            key={key}
            categoryKey={key}
            schema={schema}
            categorySelection={options.categories[key]}
            onToggle={handleCategoryToggle}
          />
        ))}

        <Button
          text={"Passer aux exercices"}
          isDisable={isSubmitDisabled}
          callback={hanbleButtonClic}
        />
    </div>
  )
}
