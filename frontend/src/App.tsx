import './App.css'
// import Cell from './components/Cell.tsx';
import Grid from './components/Grid.tsx';
import { board } from './boards/2024-12-23.ts';
function App() {
  // console.log(board);
  return (
    <>
      <Grid board={board} />
    </>
  )
}

export default App
