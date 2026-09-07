// import styles from './Score.module.css';
import Button from "../components/Button";

interface ScoreProps {
  score: number;
  nbExercices: number;
  onFinish: () => void;
}

export default function Score({ score, nbExercices, onFinish }: ScoreProps) {
  const percentage = Math.round((score / nbExercices) * 100);

  return (
    <div style={{ textAlign: 'center', marginTop: '3rem' }}>
      <h2>Session terminée !</h2>

      <p style={{ fontSize: '1.5rem', color: '#f3f4f6' }}>
        Score : <strong>{score} / {nbExercices}</strong>
      </p>

      <p style={{ color: '#a5b4fc', marginBottom: '1.5rem' }}>
        Taux de réussite : {percentage}%
      </p>

      <progress
        max="100"
        value={percentage}
        style={{ width: '100%', maxWidth: '300px', height: '10px', marginBottom: '2rem' }}
      />

      <div>
        <Button
          text={"Retour au menu"}
          isDisable={false}
          callback={onFinish}
        />
      </div>
    </div>
  )
}