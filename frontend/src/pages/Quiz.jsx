import React from "react";
import Question from "../components/Question";
import NavigationContainer from "../components/NavigationContainer";
import { useParams } from "react-router-dom";

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

function Quiz() {
  const params = useParams();
  const [currentIndex, setCurrentIndex] = React.useState(0);
  const [selectedOptions, setSelectedOptions] = React.useState({});
  const [questions, setQuestions] = React.useState([]);

  React.useEffect(() => {
    const url = `${import.meta.env.VITE_API_URL}/quizzes/${
      params.quizId
    }/questions`;
    const fetchQuestions = async () => {
      const response = await fetch(url, {
        method: "GET",
      });

      if (response.ok) {
        const data = await response.json();
        setQuestions([...data]);
      }
    };

    fetchQuestions();
  }, []);

  const handleOptionChange = (questionIndex, optionId) => {
    setSelectedOptions((prevSelectedOptions) => ({
      ...prevSelectedOptions,
      [questionIndex]: optionId,
    }));
  };

  const handleToggle = (e) => {
    e.preventDefault();
    const htmlElement = document.querySelector("html");
    htmlElement.classList.toggle("dark");
  };

  return (
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
            Question {currentIndex + 1}
          </h1>
          <p className="text-lg font-semibold">
            {currentIndex + 1} of {questions.length} questions
          </p>
        </div>
        {questions.length !== 0 ? (
          <Question
            question={questions[currentIndex]}
            key={questions[currentIndex]?.id}
            onOptionChange={(optionId) =>
              handleOptionChange(currentIndex, optionId)
            }
            selectedOption={selectedOptions[currentIndex] || ""}
          />
        ) : (
          ""
        )}
        <NavigationContainer
          length={questions.length}
          index={currentIndex}
          setIndex={setCurrentIndex}
        />
      </div>
    </>
  );
}

export default Quiz;
