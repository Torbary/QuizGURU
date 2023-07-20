import React, { useState } from "react";
import NavBar from "../components/NavBar";
import { Link } from "react-router-dom";

function PreviewQuiz({ title, description, id }) {
  return (
    <Link to={`/quizzes/${id}`}>
      <div className="border rounded-md p-2 cursor-pointer">
        <h2 className="text-center text-lg font-bold">{title}</h2>
        <p className="p-2 max-h-[14.5em] overflow-hidden text-ellipsis text-sm">
          {description}
        </p>
      </div>
    </Link>
  );
}

function AvailableQuizzes() {
  const [quizzes, setQuizzes] = useState([]);
  React.useEffect(() => {
    const fetchQuizzes = async () => {
      let response = await fetch(`${import.meta.env.VITE_API_URL}/quizzes`, {
        method: "GET",
      });

      if (response.ok) {
        const data = await response.json();

        const sortedQuizzes = data.slice().sort((a, b) => {
          const aTime = new Date(a.created_at).getTime();
          const bTime = new Date(b.created_at).getTime();
          return aTime + bTime;
        });
        setQuizzes(sortedQuizzes);
      }
    };
    fetchQuizzes();
  }, []);
  return (
    <div className="max-w-[80%] mx-auto mb-4 grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-1">
      {quizzes.map((value, index) => {
        return (
          <PreviewQuiz
            key={index}
            title={value.title}
            description={value.description}
            id={value.id}
          />
        );
      })}
    </div>
  );
}

export default function Home() {
  return (
    <div className="">
      <NavBar />
      <div className="min-h-[350px] flex flex-col gap-4 items-center justify-center">
        <p className="text-xl text-center">
          A <span className="text-2xl text-sky-600">PLATFORM</span> to take
          technical quizzes.
        </p>
        <div className="flex gap-3">
          <Link
            to={"/login"}
            className="block border-2 border-red-500 py-1 px-2 rounded-md cursor-pointer font-semibold"
          >
            Login
          </Link>
          <Link
            to={"/register"}
            className="block border-2 border-red-500 py-1 px-2 rounded-md cursor-pointer font-semibold"
          >
            Sign Up
          </Link>
        </div>
      </div>
      <div className="">
        <AvailableQuizzes />
      </div>
    </div>
  );
}
