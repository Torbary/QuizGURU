import { useState } from "react";
import "./App.css";
import Quiz from "./Quiz";
import shortid from "shortid";
function App() {
  const [count, setCount] = useState(0);

  const id = shortid.generate();

  const html = document.querySelector('html')
  html.classList.add('dark')


  return (
    <>
     <Quiz />
    </>
  );
}

export default App;
