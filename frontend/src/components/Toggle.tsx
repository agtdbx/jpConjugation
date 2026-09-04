import styles from './Toggle.module.css';

interface ToggleProps {
  text: string;
  isToggled: boolean;
  callback: () => void;
}

export default function Toggle({ text, isToggled, callback }: ToggleProps) {
  const currentModeClass = isToggled ? styles.toggledOn : styles.toggledOff;

  return (
    <div
      onClick={callback}
      className={`${styles.container} ${currentModeClass}`}
    >
      <p className={styles.text}>{text}</p>
    </div>
  )
}