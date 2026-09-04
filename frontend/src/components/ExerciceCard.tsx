import styles from './ExerciceCard.module.css';
import { useState } from 'react';
import Button from "./Button";

interface ExerciceCardProps {
  data: {
    target: string;
    form: string;
    tense: string;
    result: string;
  };
  onNext: () => void;
}

export default function ExerciceCard({ data, onNext }: ExerciceCardProps) {
  const [isValidate, setValidate] = useState(false);
  const [userResponse, setUserResponse] = useState("");

  const isUserRight = (userResponse.trim().toLowerCase() === data.result.toLowerCase());

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUserResponse(e.target.value)
  };

  // Handle enter to skip button press
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && userResponse.trim() !== "") {
      if (!isValidate) {
        setValidate(true);
      } else {
        setValidate(false);
        setUserResponse("");
        onNext();
      }
    }
  };

  return (
    <div className={`${styles.container}`}>
      <div className={`${styles.rules}`}>
        <p>{data.target}</p>
        <p>{data.form}</p>
        <p>{data.tense}</p>
      </div>
      <input
        type="text"
        readOnly={isValidate}
        value={userResponse}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        autoFocus
        className={`${styles.userResponse}`} />
      {isValidate && isUserRight && <p className={`${styles.right}`}>Bonne réponse !</p>}
      {isValidate && !isUserRight && <p className={`${styles.wrong}`}>Mauvaise réponse ({data.result})</p>}
      {!isValidate && <Button
        text="Valider"
        isDisable={userResponse.trim() === ""}
        callback={() => setValidate(true)}
      />}
      {isValidate && <Button
        text={"Suivant"}
        isDisable={false}
        callback={() => {
          setValidate(false);
          setUserResponse("");
          onNext();
        }}
      />}
    </div>
  )
}