import styles from './Score.module.css';
import Button from "../components/Button";

interface ScoreProps {
  score: number;
  nbExercices: number;
  onFinish: () => void;
}

export default function Score({ score, nbExercices, onFinish }: ScoreProps) {
  const percentage = Math.round((score / nbExercices) * 100);

  return (
    <div className={styles.container}>
      <h2 className={styles.title}>Session terminée !</h2>

      <p className={styles.scoreText}>
        Score <strong>{score} / {nbExercices}</strong>
      </p>

      <p className={styles.percentage}>
        Taux de réussite : {percentage}%
      </p>

      <progress
        max="100"
        value={percentage}
        className={styles.progressBar}
      />

      <Button
        text={"Retour au menu"}
        isDisable={false}
        callback={onFinish}
      />
    </div>
  )
}