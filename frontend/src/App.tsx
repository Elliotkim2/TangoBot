import './App.css'
// import Cell from './components/Cell.tsx';
import Grid from './components/Grid.tsx';
import { board, solvedBoard } from './boards/test.ts';
import { useState } from 'react';
function App() {
  // console.log(board);
  const [solved, setSolved] = useState(false);

  return (
    <>
      <div className="buttons">
        <button onClick={() => setSolved(false)}>Back</button>
        <button onClick={() => setSolved(true)}>Next</button>
      </div>
      {solved ? <Grid board={solvedBoard} /> : <Grid board={board} />}
    </>
  )
}

export default App
