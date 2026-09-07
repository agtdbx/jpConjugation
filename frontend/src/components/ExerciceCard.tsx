import styles from './ExerciceCard.module.css';
import { useState } from 'react';
import Button from "./Button";
import { type Options } from "../App"

interface ExerciceCardProps {
  options: Options;
  data: {
    romaji: string;
    kanji: string;
    traduction: string;
    form: string;
    tense: string;
    rules: string;
    result: string;
  };
  onNext: (isCorrect: boolean) => void;
}

export default function ExerciceCard({ options, data, onNext }: ExerciceCardProps) {
  const [isValidate, setValidate] = useState(false);
  const [userResponse, setUserResponse] = useState("");

  const isUserRight = (data.result !== undefined && userResponse.trim().toLowerCase() === data.result.toLowerCase());

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUserResponse(e.target.value)
  };

  const validateAnswer = () => {
    setValidate(true);
  }

  const nextExercice = () => {
    setValidate(false);
    setUserResponse("");
    onNext(isUserRight);
  }

  // Handle enter to skip button press
  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && userResponse.trim() !== "") {
      if (!isValidate) validateAnswer();
      else nextExercice();
    }
  };

  return (
    <div className={`${styles.container}`}>
      <div className={`${styles.rules}`}>
        {options.displayMode === "romaji" && <p>{data.romaji}</p>}
        {options.displayMode === "kanji" && <p>{data.kanji}</p>}
        {options.displayMode === "traduction" && <p>{data.traduction}</p>}
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
      {isValidate && !isUserRight && options.displayRules && <p className={`${styles.rules}`}>{data.rules}</p>}
      {!isValidate && <Button
        text="Valider"
        isDisable={userResponse.trim() === ""}
        callback={validateAnswer}
      />}
      {isValidate && <Button
        text={"Suivant"}
        isDisable={false}
        callback={nextExercice}
      />}
    </div>
  )
}