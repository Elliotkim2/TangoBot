import Moon from '../svg/Moon.tsx';
import Sun from '../svg/Sun.tsx';
import Empty from '../svg/Empty.tsx';
import Cross from '../svg/Cross.tsx';
import Equal from '../svg/Equal.tsx';
import './Cell.css';

const Cell = (props: { icon: string, down: string, right: string }) => {
  // console.log(props.icon, props.down, props.right);
  return (
    <div className="cell">
      <div className="cell-content">
        {props.icon === "S" && <Sun />}
        {props.icon === "M" && <Moon />}
        {props.icon === "E" && <Empty />}
      </div>
      {props.down === "Equal" && <div className="cell-down">
        <Equal />
      </div>}
      {props.down === "Cross" && <div className="cell-down">
        <Cross />
      </div>}
      {props.right === "Equal" && <div className="cell-right">
        <Equal />
      </div>}
      {props.right === "Cross" && <div className="cell-right">
        <Cross />
      </div>}

    </div>
  );
}

export default Cell;