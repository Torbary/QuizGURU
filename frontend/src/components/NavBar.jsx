import React, { useState } from "react";
export default function NavBar() {
  const [theme, setTheme] = useState("Dark");
  const handleToggle = (e) => {
    e.preventDefault();
    const htmlElement = document.querySelector("html");
    htmlElement.classList.toggle("dark");

    const toggleTheme = () => {
      if (theme === "Dark") setTheme("Light");
      else setTheme("Dark");
    };

    toggleTheme();
  };

  return (
    <header className="sticky top-0 left-0 right-0 text-slate-100 dark:text-slate-800 dark:bg-yellow-600 bg-slate-800">
      <nav className="max-w-[800px] flex justify-between p-3 mx-auto ">
        <h1 className="font-semibold text-xl">QuizGURU</h1>
        <div>
          <button
            onClick={handleToggle}
            className="block border-2 border-red-500 py-1 px-2 rounded-md cursor-pointer font-semibold"
          >
            {theme}
          </button>
        </div>
      </nav>
    </header>
  );
}
