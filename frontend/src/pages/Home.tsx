import styles from './Home.module.css';
import { useState, useEffect } from 'react'
import { useLocalStorage } from "../hooks/useLocalStorage"
import Section from "../components/Section";
import Button from "../components/Button";

interface Options {
  number_conjugation: number;
  sections: Record<string, { types: string[], values: string[] }>;
}

export default function Home() {
  // Create states
  const [schema, setSchema] = useState<any>(null)
  const [options, setOptions] = useLocalStorage<Options>('jp-conjugation-options', {
    number_conjugation: 10,
    sections: {}
  })
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // Setup first call at first page render
  useEffect(() => {
    // Get schema
    fetch(`${import.meta.env.VITE_API_URL}/api/options`)
      .then(res => {
        if (!res.ok) throw new Error("Erreur réseau")
        return res.json()
      })
      .then(fetchedSchema => {
        setSchema(fetchedSchema);

        // Get options
        setOptions(prevOptions => {
          // If options exists, don't overwrite them
          if (Object.keys(prevOptions.sections).length > 0) return prevOptions;

          // Else, create options based on schema
          const initialSections: Record<string, { types: string[], values: string[] }> = {};

          Object.keys(fetchedSchema.sections).forEach(sectionKey => {
            initialSections[sectionKey] = { types: [], values: [] };
          });

          return { ...prevOptions, sections: initialSections };
        });

        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      })
  }, [])

  // Display loading text
  if (loading) return <div>Chargement des options depuis le serveur...</div>
  // Display error
  if (error) return <div>Erreur : {error}</div>

  const handleToggle = (sectionKey: string, category: 'types' | 'values', id: string) => {
    setOptions(prev => {
      const currentList = prev.sections[sectionKey][category];
      // If id is in list, remove it. Else, add it.
      const newList = currentList.includes(id)
        ? currentList.filter(item => item !== id)
        : [...currentList, id];

      // Rebuilt options with modifications
      return {
        ...prev,
        sections: {
          ...prev.sections,
          [sectionKey]: {
            ...prev.sections[sectionKey],
            [category]: newList
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

  const checkIsFormValid = () => {
    // If loading or error, disable
    if (!schema || !options.sections || Object.keys(options.sections).length === 0) return false;

    // If empty, disable
    const sectionKeys = Object.keys(schema.sections);
    if (sectionKeys.length === 0) return false;

    // Validate first section (forms)
    const firstKey = sectionKeys[0];
    const firstSection = options.sections[firstKey];
    if (!firstSection || firstSection.values.length === 0) return false;

    // Validate all other sections
    const remainingKeys = sectionKeys.slice(1);

    const hasValidTarget = remainingKeys.some(key => {
      const sectionOptions = options.sections[key];
      const sectionSchema = schema.sections[key];

      if (!sectionOptions || !sectionSchema) return false;

      // Check if backend have set type
      const requiresTypes = Object.keys(sectionSchema.types).length > 0;

      const hasSelectedTypes = sectionOptions.types.length > 0;
      const hasSelectedValues = sectionOptions.values.length > 0;

      if (requiresTypes) {
        return hasSelectedTypes && hasSelectedValues;
      } else {
        return hasSelectedValues;
      }
    });

    return hasValidTarget;
  };

  const isSubmitDisabled = !checkIsFormValid();

  const hanbleButtonClic = () => {
    fetch(`${import.meta.env.VITE_API_URL}/api/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(options),
    }).then(res => {
        if (!res.ok) throw new Error("Erreur réseau")
        return res.json()
      }).then(exercices => {
        console.log(exercices);
      })
      .catch(err => {
        setError(err.message);
      });
  }

  // Display data
  return (
    <div>
      <h1>Configuration de la session</h1>
      <div className={`${styles.slider}`}>
        <h3>Nombre d'exercices : {options.number_conjugation}</h3>
        <input
          type="range"
          min="1"
          max="50"
          value={options.number_conjugation}
          onChange={handleNumberChange}
        />
      </div>
      {schema && Object.entries(schema.sections).map(([key, sectionData]) => (
        <Section
          key={key}
          sectionKey={key}
          schema={sectionData as any}
          options={options.sections[key]}
          onToggle={handleToggle}
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