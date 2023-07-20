import "./App.css";
import Quiz from "./pages/Quiz";
import SignUp from "./pages/SignUp";
import Login from "./pages/Login";
import Home from "./pages/Home";
import { Route, Routes } from "react-router-dom";
import ErrorPage from "./pages/error-page";
function App() {
  const html = document.querySelector("html");
  html.classList.add("dark");

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} errorElement={<ErrorPage />} />
        <Route path="/quizzes/:quizId" element={<Quiz />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<SignUp />} />
      </Routes>
    </>
  );
}

export default App;
