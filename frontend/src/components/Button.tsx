import styles from './Button.module.css';

interface ButtonProps {
  text: string;
  isDisable: boolean;
  callback: () => void;
}

export default function Button({ text, isDisable, callback }: ButtonProps) {
  const currentModeClass = isDisable ? styles.disable : '';
  const onClick = isDisable ? ()=>{} : callback;

  return (
    <div
      onClick={onClick}
      className={`${styles.container} ${currentModeClass}`}
    >
      <p className={styles.text}>{text}</p>
    </div>
  )
}