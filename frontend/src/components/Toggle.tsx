import styles from './Toggle.module.css';

interface ToggleProps {
  text: string;
  isToggled: boolean;
  callback: () => void;
  className?: string;
}

export default function Toggle({ text, isToggled, callback, className='' }: ToggleProps) {
  const currentModeClass = isToggled ? styles.toggledOn : styles.toggledOff;

  return (
    <div
      onClick={callback}
      className={`${styles.container} ${currentModeClass} ${className}`}
    >
      <p className={styles.text}>{text}</p>
    </div>
  )
}
