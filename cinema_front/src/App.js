import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import CreateFilme from "./pages/CreateFilme";
import TelaInicial from "./pages/TelaInicial";

function App() {
  return (
    <BrowserRouter>
      <div className='App'>
        <Link to='/'>Home</Link>
        <Link to='/criar_filme'>Criar filme</Link>
      </div>
      <Routes>
        <Route exact path='/' element={<TelaInicial/>} />
        <Route path='/criar_filme' element={<CreateFilme/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
