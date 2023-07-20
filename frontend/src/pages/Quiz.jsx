import React, { useState } from "react";
import Question from "../components/Question";
import NavigationContainer from "../components/NavigationContainer";
import { useNavigate, useParams } from "react-router-dom";
import { useQuizStore } from "../store/quiz";
import ErrorPage from "./error-page";

// const questions = [
//   {
//     title: "Who is considered the first programmer?",
//     options: [
//       "Alan Turing",
//       "Ada Lovelace",
//       "Charles Babbage",
//       "Julien Barbier",
//     ],
//     correct: 1,
//     hint: "It was a lady.",
//     point: 1,
//   },
//   {
//     title: "Which is an interpreted programming language?",
//     options: ["Ruby", "Python", "C", "Java"],
//     correct: 1,
//     point: 1,
//   },
//   {
//     title: "Which of these is an interpreted programming language?",
//     options: ["C++", "Python", "C", "FORTRAN"],
//   },
// ];

export default function Quiz() {
  const params = useParams();
  const navigate = useNavigate();
  const { index, questions, setQuestions, selectedOptions } = useQuizStore();
  const [valid, setValid] = useState(true);

  React.useEffect(() => {
    console.log(selectedOptions);
  }, [selectedOptions]);

  React.useEffect(() => {
    const url = `${import.meta.env.VITE_API_URL}/quizzes/${params.quizId}`;
    const fetchQuestions = async () => {
      try {
        const response = await fetch(url, {
          method: "GET",
        });

        if (response.ok) {
          const data = await response.json();
          setQuestions(data.questions);
        } else {
          setValid(false);
        }
      } catch (err) {
        navigate("/");
      }
    };

    fetchQuestions();
  }, []);

  const handleToggle = (e) => {
    e.preventDefault();
    const htmlElement = document.querySelector("html");
    htmlElement.classList.toggle("dark");
  };

  const quiz = (
    <>
      <div className="max-w-[600px] mx-auto px-4 min-w-[320px] pt-4">
        <div>
          <button
            className="block ml-auto border-2 border-red-500 p-1 rounded-md cursor-pointer font-semibold"
            onClick={handleToggle}
          >
            Toggle Mode
          </button>
        </div>
        <div>
          <h1 className="text-2xl mt-5 text-red-600 dark:text-lime-400">
            Question {index + 1}
          </h1>
          <p className="text-lg font-semibold">
            {index + 1} of {questions.length} questions
          </p>
        </div>
        {questions.length !== 0 ? <Question key={questions[index]?.id} /> : ""}
        <NavigationContainer />
      </div>
    </>
  );
  return valid ? quiz : <ErrorPage />;
}
