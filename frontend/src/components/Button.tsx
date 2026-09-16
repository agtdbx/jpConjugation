import styles from './Button.module.css';

interface ButtonProps {
  text: string;
  isDisable: boolean;
  callback: () => void;
  variant?: 'success' | 'primary' | 'secondary';
}

export default function Button({ text, isDisable, callback, variant = 'success' }: ButtonProps) {
  const modeClass = isDisable ? styles.disable : styles[variant];
  const onClick = isDisable ? ()=>{} : callback;

  return (
    <div
      onClick={onClick}
      className={`${styles.container} ${modeClass}`}
    >
      <p className={styles.text}>{text}</p>
    </div>
  )
}
