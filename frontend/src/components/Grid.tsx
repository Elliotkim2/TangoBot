import Cell from './Cell.tsx';
import './Grid.css';
const Grid = (props: { board: { grid: string[], crosses: number[][], equals: number[][] } }) => {
  console.log(props.board.crosses);
  console.log(props.board.equals);
  return (
    <div className="outer-shell">
      <h1>Tango Board</h1>
      <div className="grid">
        {Array.from({ length: 36 }, (_, i: number) => {
          let downcrosses = false;
          if ((props.board.crosses[i]).length > 0) {
            downcrosses = props.board.crosses[i].map((d) => (d === i + 6)).reduce((a, b) => a || b, false)
          }
          let downequals = false;
          if ((props.board.equals[i]).length > 0) {
            downequals = props.board.equals[i].map((d) => (d === i + 6)).reduce((a, b) => a || b, false)
          }
          let rightcrosses = false;
          if ((props.board.crosses[i]).length > 0) {
            rightcrosses = props.board.crosses[i].map((d) => (d === i + 1)).reduce((a, b) => a || b, false)
          }
          let rightequals = false;
          if ((props.board.equals[i]).length > 0) {
            rightequals = props.board.equals[i].map((d) => (d === i + 1)).reduce((a, b) => a || b, false)
          }

          return (
            <Cell
              key={i}
              icon={props.board.grid[i]}
              down={downcrosses ? "crosses" : downequals ? "equals" : ""}
              right={rightcrosses ? "crosses" : rightequals ? "equals" : ""}
            />
          )
        }
        )}
      </div>
    </div>

  )
}

export default Grid;