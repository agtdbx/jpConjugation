import styles from './Section.module.css';
import Toggle from "./Toggle";

interface SectionProps {
  sectionKey: string;
  schema: {
    title: string;
    types: Record<string, string>;
    values: Record<string, string>;
  };
  options: {
    types: string[];
    values: string[];
  };
  onToggle: (sectionKey: string, category: 'types' | 'values', id: string) => void;
}

export default function Section({ sectionKey, schema, options, onToggle }: SectionProps) {
  return (
    <div className={`${styles.container}`}>
      <h2>{schema.title}</h2>

      {/* Display types if needed */}
      {Object.keys(schema.types).length > 0 && (
        <div className={`${styles.type}`}>
          {Object.entries(schema.types).map(([id, label]) => (
            <Toggle
              key={id}
              text={label}
              isToggled={options.types.includes(id)}
              callback={() => onToggle(sectionKey, 'types', id)}
              />
          ))}
        </div>
      )}

      {/* Display values */}
      <div>
        {Object.entries(schema.values).map(([id, label]) => (
            <Toggle
              key={id}
              text={label}
              isToggled={options.values.includes(id)}
              callback={() => onToggle(sectionKey, 'values', id)}
              />
        ))}
      </div>
    </div>
  )
}