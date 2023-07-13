import "./App.css";
import Quiz from "./Quiz";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import { Route, Routes } from "react-router-dom";
function App() {
  const html = document.querySelector("html");
  html.classList.add("dark");

  return (
    <>
      <Routes>
        <Route path="/" element={<Quiz />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<SignUp />} />
      </Routes>

    </>
  );
}

export default App;
