import React, { useState } from "react";
import Question from "../components/Question";
import NavigationContainer from "../components/NavigationContainer";
import { useNavigate, useParams } from "react-router-dom";
import { useQuizStore } from "../store/quiz";
import ErrorPage from "./error-page";

export default function Quiz() {
  const params = useParams();
  const navigate = useNavigate();
  const { setId, index, questions, setQuestions } = useQuizStore();
  const [valid, setValid] = useState(true);

  React.useEffect(() => {
    const url = `${import.meta.env.VITE_API_URL}/quizzes/${params.quizId}`;
    const fetchQuestions = async () => {
      try {
        const response = await fetch(url, {
          method: "GET",
        });

        if (response.ok) {
          const data = await response.json();
          setId(params.quizId);
          setQuestions(data.questions);
        } else {
          setValid(false);
        }
      } catch (err) {
        navigate("/");
      }
    };

    fetchQuestions();
    // eslint-disable-next-line react-hooks/exhaustive-deps
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
