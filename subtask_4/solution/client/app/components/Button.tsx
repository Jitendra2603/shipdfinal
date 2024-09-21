type ButtonProps = {
  text?: string;
  onClick?: () => void;
  className?: string;
};

export default function Button(props: ButtonProps) {
  return (
    <button
      className={`border-2 border-black m-2 py-1 px-2 ${props.className}`} 
      onClick={props.onClick}
    >
      {props.text ?? "button"}
    </button>
  );
}
