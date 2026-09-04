import styles from './Session.module.css';
import { useState } from 'react';
import ExerciceCard from '../components/ExerciceCard';

interface SessionProps {
  exercices: any[];
  onFinish: () => void;
}

export default function Session({ exercices, onFinish }: SessionProps) {
  const [currentIndex, setCurrentIndex] = useState(0);

  const handleNext = () => {
    if (currentIndex + 1 < exercices.length) {
      setCurrentIndex(prev => prev + 1);
    } else {
      onFinish();
    }
  };

  const currentExercice = exercices[currentIndex];

  return (
    <div>
      <p>Progression : {currentIndex + 1} / {exercices.length}</p>

      <ExerciceCard
        data={currentExercice}
        onNext={handleNext}
      />
    </div>
  )
}