import { useState } from "react";
import "./App.css";
import Quiz from "./Quiz";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
function App() {
  const html = document.querySelector('html')
  html.classList.add('light')


  return (
    <>
     <Login />
    </>
  );
}

export default App;
