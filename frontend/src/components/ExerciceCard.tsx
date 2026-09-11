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

  const checkUserInput = () => {
    if (!data.result || !userResponse) return (false);

    const userInputNormalize = userResponse.trim().replace(/\s+/g, ' ').toLowerCase();

    return (userInputNormalize === data.result.toLowerCase());
  }
  const isUserRight = checkUserInput();

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

  const getDisplayWord = () => {
    if (options.displayMode === "romaji") return data.romaji;
    else if (options.displayMode === "kanji") return data.kanji;
    else if (options.displayMode === "traduction") return data.traduction;
    else return "Error";
  }

  const getDisplayWordStyle = (displayWord: string) => {
    if (displayWord.length > 20) return styles.textLong;
    if (displayWord.length > 10) return styles.textMedium;
    return "";
  }

  const displayWord = getDisplayWord();
  const displayWordStyle = getDisplayWordStyle(displayWord);

  return (
    <div className={`${styles.container}`}>
      <div className={`${styles.rules}`}>
        <p className={`${displayWordStyle}`}>{displayWord}</p>
        <p>{data.tense}</p>
        <p>{data.form}</p>
      </div>
      <input
        type="text"
        maxLength={40}
        autoComplete="off"
        autoCorrect="off"
        autoCapitalize="none"
        spellCheck={false}
        readOnly={isValidate}
        value={userResponse}
        onChange={handleInputChange}
        onKeyDown={handleKeyDown}
        autoFocus
        className={`${styles.userResponse}`} />
      {isValidate && isUserRight && <p className={`${styles.right}`}>Bonne réponse !</p>}
      {isValidate && !isUserRight && <p className={`${styles.wrong}`}>Mauvaise réponse ({data.result})</p>}
      {isValidate && !isUserRight && options.displayRules && <p className={`${styles.explanation}`}>{data.rules}</p>}
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
