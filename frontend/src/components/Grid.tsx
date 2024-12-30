import Cell from './Cell.tsx';
import './Grid.css';
const Grid = (props: { board: { grid: string[], cross: number[][], equal: number[][] } }) => {
  console.log(props.board.cross);
  console.log(props.board.equal);
  return (
    <div className="outer-shell">
      <h1>Tango Board</h1>
      <div className="grid">
        {Array.from({ length: 36 }, (_, i: number) => {
          let downcross = false;
          if ((props.board.cross[i]).length > 0) {
            downcross = props.board.cross[i].map((d) => (d === i + 6)).reduce((a, b) => a || b, false)
          }
          let downequal = false;
          if ((props.board.equal[i]).length > 0) {
            downequal = props.board.equal[i].map((d) => (d === i + 6)).reduce((a, b) => a || b, false)
          }
          let rightcross = false;
          if ((props.board.cross[i]).length > 0) {
            rightcross = props.board.cross[i].map((d) => (d === i + 1)).reduce((a, b) => a || b, false)
          }
          let rightequal = false;
          if ((props.board.equal[i]).length > 0) {
            rightequal = props.board.equal[i].map((d) => (d === i + 1)).reduce((a, b) => a || b, false)
          }

          return (
            <Cell
              key={i}
              icon={props.board.grid[i]}
              down={downcross ? "Cross" : downequal ? "Equal" : ""}
              right={rightcross ? "Cross" : rightequal ? "Equal" : ""}
            />
          )
        }
        )}
      </div>
    </div>

  )
}

export default Grid;