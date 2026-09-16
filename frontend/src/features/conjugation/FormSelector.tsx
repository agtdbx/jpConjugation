import Section from "../../components/Section";
import Toggle from "../../components/Toggle";
import { type FormSchema } from "../../App";

interface FormSelectorProps {
  schema: FormSchema;
  selectedForms: string[];
  onToggle: (id: string) => void;
}

export default function FormSelector({ schema, selectedForms, onToggle }: FormSelectorProps) {
  return (
    <Section title={schema.title}>
      {Object.entries(schema.values).map(([id, label]) => (
          <Toggle
            key={id}
            text={label}
            isToggled={selectedForms.includes(id)}
            callback={() => onToggle(id)}
            />
      ))}
    </Section>
  )
}
