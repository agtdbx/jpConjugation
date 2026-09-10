import styles from './Session.module.css';
import { useState } from 'react';
import Score from '../pages/Score'
import ExerciceCard from '../components/ExerciceCard';
import { type Options, type ExerciceData } from "../App"

interface SessionProps {
  options: Options;
  exercices: ExerciceData[];
  onFinish: () => void;
}

export default function Session({ options, exercices, onFinish }: SessionProps) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [score, setScore] = useState(0);

  const handleNext = (isCorrect: boolean) => {
    if (isCorrect) setScore(prev => prev + 1)
    if (currentIndex < exercices.length) {
      setCurrentIndex(prev => prev + 1);
    }
  };

  if (currentIndex >= exercices.length) {
    return (<Score
      score={score}
      nbExercices={exercices.length}
      onFinish={onFinish}
    />)
  }


  const currentExercice = exercices[currentIndex];

  return (
    <div className={styles.wrapper}>
      <p className={styles.progressText}>Progression : {currentIndex + 1} / {exercices.length}</p>

      <ExerciceCard
        options={options}
        data={currentExercice}
        onNext={handleNext}
      />
    </div>
  )
}
