import "./App.css";
import Quiz from "./pages/Quiz";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import Home from "./pages/Home";
import { Route, Routes } from "react-router-dom";
function App() {
  const html = document.querySelector("html");
  html.classList.add("dark");

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quizzes/:quizId" element={<Quiz />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<SignUp />} />
      </Routes>
    </>
  );
}

export default App;
